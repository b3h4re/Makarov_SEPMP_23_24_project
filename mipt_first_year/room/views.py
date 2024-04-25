from django.apps import apps
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from config import urls


@login_required
def room(request, slug):
    room = apps.get_model('room', 'Room').objects.get(slug=slug)
    if request.user.id != room.room_user.id and request.user.id != room.room_student.id:
        return redirect('home')

    messages = apps.get_model('room', 'Message').objects.all().filter(room=room)
    context = {
        "room": room,
        "messages": messages
    }
    return render(request, 'room.html', context)


@login_required
def list_rooms(request, user_id):
    user = User.objects.get(id=user_id)
    try:
        rooms = apps.get_model('room', 'Room').objects.all().filter(room_user=user)
    except apps.get_model('room', 'Room').DoesNotExist:
        try:
            rooms = apps.get_model('room', 'Room').objects.all().filter(room_student=user)
        except apps.get_model('room', 'Room').DoesNotExist:
            rooms = apps.get_model('room', 'Room').objects.none()
    context = {
        'rooms': rooms
    }
    return render(request, 'list_rooms.html', context)
