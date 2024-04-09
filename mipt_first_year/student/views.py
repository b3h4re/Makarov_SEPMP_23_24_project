from django.shortcuts import render
from django.contrib.auth.models import User


def user_page(request, user_id):
    user = User.objects.get(id=user_id)

    context = {
        'student': user.student
    }

    return render(request, 'student_profile.html', context)