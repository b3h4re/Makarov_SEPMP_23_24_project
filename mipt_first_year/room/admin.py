from django.apps import apps
from django.contrib import admin


Room = apps.get_model('room', 'Room')
Message = apps.get_model('room', 'Message')
admin.site.register(Room)
admin.site.register(Message)