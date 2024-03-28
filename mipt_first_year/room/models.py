from django.contrib.auth.models import User
from django.db import models


class Room(models.Model):

    @staticmethod
    def default_user():
        return User.objects.filter(username="default_user___________").first().username

    name = models.CharField(max_length=256)
    slug = models.SlugField(unique=True)
    user1 = models.ForeignKey(User, related_name="user1", on_delete=models.DO_NOTHING, default=default_user())
    user2 = models.ForeignKey(User, related_name="user2", on_delete=models.DO_NOTHING, default=default_user())


class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)
