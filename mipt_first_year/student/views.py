from django.apps import apps
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def user_page(request, user_id):
    user = User.objects.get(id=user_id)

    context = {
        'student': user.student
    }

    return render(request, 'student_profile.html', context)


@login_required
def start_chat(request, student_id, user_id):
    if user_id == student_id:
        return redirect(f'/user/{user_id}')

    student = User.objects.get(id=student_id)
    user = User.objects.get(id=user_id)

    #print(user.username, student.username)

    try:
        room = apps.get_model('room', 'Room').objects.get(name=student.username + user.username)
        slug = room.slug
    except apps.get_model('room', 'Room').DoesNotExist:
        slug = hex(hash(user.username + student.username))[2:]
        apps.get_model('room', 'Room').objects.create(room_user=user, room_student=student, slug=slug,
                                                      name=student.username + user.username)

    print(slug)

    return redirect(f'/room/{slug}')
