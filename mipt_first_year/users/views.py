from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage

from .tokens import account_activation_token

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.messages import success, error
from django.contrib.auth.decorators import login_required


def activate_email(request, user, to_email):
    mail_subject = 'Подтверждение почты.'
    message = render_to_string('activate_account.html', {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
            received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        error(request, f'Problem sending confirmation email to {to_email}, check if you typed it correctly.')


def register(request):
    if request.user.is_authenticated:
        return render(request, 'already_logged_in.html')
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            username = form.cleaned_data.get('username')
            success(request, "Аккаунт упешно создан")
            activate_email(request, user, form.cleaned_data.get('email'))
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        success(request, 'Thank you for your email confirmation. Now you can login your account.')
        return render(request, 'activate_account_done.html')
    else:
        error(request, 'Activation link is invalid!')
    return redirect('home')


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            success(request, "Профиль успешно обновлённ.")
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        "u_form": u_form,
        "p_form": p_form
    }

    return render(request, 'profile.html', context)
