from django.db.models import QuerySet
from customauth.models import Sessions
from django.core.exceptions import ObjectDoesNotExist

class RoomManager(QuerySet):
    def get_users_of(self, room_name):
        return super().filter(room_name=room_name)

    def user_and_room(self, username, room_id):
        auth = super().filter(user__username=username, room=room_id).exists()
        if auth:
            return True
        return False

    def session_and_room(self, session_key, room_id): #using to check if user have permission to view chat room.
        session = Sessions.manager.exist(session_key) #via user's session key
        if session:
            session_user = session.data.get('username')
            return self.user_and_room(session_user, room_id)
        return False

    def give_permission(self, username, room_id): #giving user a permission to view given chat room.
        from .models import Usr, Room
        user = Usr.manager.get(username=username)
        room = Room.objects.get(pk=room_id)
        try:
            exist = super().get(user=user, room=room)
        except ObjectDoesNotExist:
            exist = False

        if not exist:
            super().create(user=user, room=room)



