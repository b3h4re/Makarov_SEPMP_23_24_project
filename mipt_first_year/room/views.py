from django.apps import apps
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from config import urls


# @login_required(login_url=urls.auth_view.)
def room(request, slug):
    room = apps.get_model('room', 'Room').objects.all().get(slug=slug)
    messages = apps.get_model('room', 'Message').objects.all().filter(room=room)[0:25]
    context = {
        "room": room,
        "messages": messages
    }
    return render(request, 'room.html', context)