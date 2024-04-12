from django.shortcuts import render, redirect

from .forms import UserRegisterForm
from django.contrib.messages import success
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            success(request, "Аккаунт упешно создан")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'profile.html')