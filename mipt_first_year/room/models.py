from django.contrib.auth.models import User
from django.db import models

from config.settings import DEFAULT_USER_ID


def get_slug_from_usernames(username1, username2):
    return hex(hash(username1 + username2))[2:]


def get_default_slug():
    return get_slug_from_usernames(User.objects.get(id=DEFAULT_USER_ID).username,
                                   User.objects.get(id=DEFAULT_USER_ID).username)


class Room(models.Model):

    def get_last_message(self):
        messages = self.messages.get()
        print(messages)
        return messages.first()

    @staticmethod
    def get_default_user():
        return User.objects.get(id=DEFAULT_USER_ID).username

    name = models.CharField(max_length=256)
    slug = models.SlugField(unique=True)
    room_student = models.ForeignKey(User, related_name="room_student", on_delete=models.DO_NOTHING,
                                     default=get_default_user())
    room_user = models.ForeignKey(User, related_name="room_user", on_delete=models.DO_NOTHING,
                                  default=get_default_user())


class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)
