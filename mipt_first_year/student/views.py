from django.apps import apps
from django.shortcuts import render
from django.contrib.auth.models import User


def user_page(request, username):
    Student = apps.get_model('student', 'Student')
    user = User.objects.all().filter(username=username).first()

    context = {
        'student': user.student
    }

    return render(request, 'student_profile.html', context)