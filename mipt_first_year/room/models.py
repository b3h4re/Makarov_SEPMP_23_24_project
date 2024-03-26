from django.contrib.auth.models import User
from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(unique=True)
    # user1 = models.ForeignKey(User, related_name="rooms", on_delete=models.DO_NOTHING)
    # user2 = models.ForeignKey(User, related_name="rooms", on_delete=models.DO_NOTHING)


class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)