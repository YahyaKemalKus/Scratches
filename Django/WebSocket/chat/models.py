from django.db.models import *
from customauth.models import Usr
from .managers import RoomManager


class Room(Model):
    room_name = CharField(default="",
                          max_length=32,
                          name='name')

    chat_log = TextField()

    class Meta:
        db_table = "AArooms"


class UserRooms(Model):
    user = ForeignKey(Usr,
                      on_delete=CASCADE,
                      related_name='rooms')

    room = ForeignKey(Room,
                      on_delete=CASCADE,
                      related_name='members')

    manager = RoomManager.as_manager()

    class Meta:
        db_table = "AAuserrooms"




