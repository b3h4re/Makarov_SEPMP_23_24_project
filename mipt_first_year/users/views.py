from django.shortcuts import render, redirect

from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage

from .tokens import account_activation_token

from .forms import UserRegisterForm
from django.contrib.messages import success
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
        messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
            received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        messages.error(request, f'Problem sending confirmation email to {to_email}, check if you typed it correctly.')


def register(request):
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
    return redirect('home')


@login_required
def profile(request):
    return render(request, 'profile.html')
