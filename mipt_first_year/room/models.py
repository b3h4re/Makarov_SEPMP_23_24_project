from django.contrib.auth.models import User
from django.db import models
from config.settings import DEFAULT_USER_ID


class Room(models.Model):
    def get_last_message(self):
        return self.messages.all().first()

    @staticmethod
    def get_default_user():
        return User.objects.get(id=DEFAULT_USER_ID).username

    name = models.CharField(max_length=256)
    slug = models.SlugField(unique=True)
    room_student = models.ForeignKey(User, related_name="room_student", on_delete=models.CASCADE,
                                     default=get_default_user())
    room_user = models.ForeignKey(User, related_name="room_user", on_delete=models.CASCADE,
                                  default=get_default_user())

    def __str__(self):
        return self.room_user.username + " " + self.room_student.username


class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)
