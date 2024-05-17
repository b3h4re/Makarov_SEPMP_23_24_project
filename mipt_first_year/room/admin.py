from django.apps import apps
from django.contrib import admin


Room = apps.get_model('room', 'Room')
admin.site.register(Room)

#Message = apps.get_model('room', 'Message')
#admin.site.register(Message)
