from django.shortcuts import render
from django.apps import apps


def home(request):
    Student = apps.get_model('student', 'Student')
    context = {
        'students': Student.objects.all()
    }

    return render(request, "base.html", context)