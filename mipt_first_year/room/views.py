from django.apps import apps
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

from config import urls


@login_required
def room(request, slug):
    room = apps.get_model('room', 'Room').objects.all().get(slug=slug)
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
        student = user.student
        context = {
            'rooms': user.room_student
        }
    except apps.get_model('student', 'Student').DoesNotExist:
        context = {
            'rooms': user.room_user
        }
    return render(request, 'list_rooms.html', context)