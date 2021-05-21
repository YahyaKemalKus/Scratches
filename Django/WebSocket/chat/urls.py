from django.urls import path
from .views import *

app_name = 'chat'
urlpatterns = [
    path('<int:room_id>/', chat, name='chat_room'),
    path('', index, name='main_page'),
    path('permission/', permission, name='permission_page'),
    path('permitted/', permitted, name='permitted_page'),
    path('newroom/', newroom, name='newroom_page'),
    path('room_created/', room_created, name='room_created_page')
]
