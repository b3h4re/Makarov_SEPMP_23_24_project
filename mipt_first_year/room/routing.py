from django.urls import path
from . import consumers


websocket_urlpatterns = [
    path('ws/<str:slug>/', consumers.ChatConsumer.as_asgi()),
]
