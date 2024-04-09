from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.messages import success
from django.contrib.auth.decorators import login_required
from django.apps import apps


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


@login_required
async def start_chat(request, username1, username2):
    Rooms = apps.get_model('rooms', 'Rooms')
    user1 = User.objects.all().filter(username=username1).first()
    user2 = User.objects.all().filter(username=username2).first()

    room = User.objects.all().filter(user1=user1, user2=user2).first()

    print(room.slug)

    return redirect('')