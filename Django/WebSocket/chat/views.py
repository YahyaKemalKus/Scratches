from django.shortcuts import render, redirect
from django.http import Http404
from customauth.decorators import valid_session, admin
from customauth.models import Usr
from .models import Room, UserRooms


@valid_session
def chat(request, room_id):
    return render(request, "chat/chat.html", context={'room_id': room_id})


@valid_session
def index(request):
    rooms = Room.objects.all()
    return render(request, "chat/index.html", context={'rooms': rooms})


@admin
def permission(request):
    users = Usr.manager.all()
    rooms = Room.objects.all()
    return render(request, "chat/permission.html", context={'users': users, 'rooms': rooms})


@admin
def permitted(request):
    username = request.POST['user']
    room_id = request.POST['room']
    room_name = Room.objects.get(pk=room_id).name
    UserRooms.manager.give_permission(username, int(room_id))

    return render(request, "chat/permitted.html", context={'username': username, 'room_name': room_name})


@admin
def newroom(request):
    return render(request, "chat/newroom.html", context={})


@admin
def room_created(request):
    room_name = request.POST['room_name']
    Room.objects.create(name=room_name)
    return render(request, "chat/room_created.html",context={'room_name': room_name})
