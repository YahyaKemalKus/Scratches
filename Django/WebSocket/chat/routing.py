from django.urls import path

from .consumers import Chat

websocket_urlpatterns = [
    path("chat/<int:room_id>/", Chat.as_asgi()),
]