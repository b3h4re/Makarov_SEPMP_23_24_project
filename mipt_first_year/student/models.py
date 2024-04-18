from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    field_of_study = models.CharField(max_length=256)
    about = models.TextField(default='')

    def __str__(self):
        return self.user.username