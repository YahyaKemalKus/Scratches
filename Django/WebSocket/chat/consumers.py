import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from .models import UserRooms, Room
from asgiref.sync import sync_to_async
from customauth.models import Sessions
from channels.db import database_sync_to_async

mng = UserRooms.manager
mng2 = Sessions.manager
mng3 = Room.objects


class Chat(AsyncJsonWebsocketConsumer):
    sessions = dict()#key = session_key,  value = {'username': username, 'group': group}

    @database_sync_to_async
    def update_db(self,username , message, room_id):
        room = mng3.get(pk=room_id)
        room.chat_log += "\n" + username + message
        room.save()

    @database_sync_to_async
    def get_chatlog(self, room_id):
        return mng3.get(pk=room_id).chat_log

    async def connect(self):
        room_id = self.scope['url_route']['kwargs']['room_id']
        cookies = self.scope['cookies']
        if 'session_key' in cookies.keys():
            session_key = cookies['session_key']
            is_permitted = await sync_to_async(mng.session_and_room, thread_sensitive=True)(session_key, room_id)
            if is_permitted:
                user_session = await sync_to_async(mng2.get, thread_sensitive=True)(session_key=session_key)
                username = user_session.data['username']
                self.sessions[session_key] = {'username': username, 'group': str(room_id)}

                await self.accept()
                await self.channel_layer.group_add(
                    str(room_id),
                    self.channel_name
                )
                await self.channel_layer.group_send(str(room_id),
                                                    {
                                                        'type': 'send_message',
                                                        'username': username,
                                                        'event': 'Joined'
                                                    })

                await self.send(text_data=json.dumps({'payload':
                    {
                        'type': 'send_message',
                        'username': username,
                        'event': 'userandchatlog',
                        'chatlog': await self.get_chatlog(room_id)

                    }}))

                await self.update_db(username, ' Connected!', room_id)

    async def disconnect(self, close_code):
        room_id = self.scope['url_route']['kwargs']['room_id']
        try:
            session_key = self.scope['cookies']['session_key']
            username = self.sessions[session_key]['username']
            group = self.sessions[session_key]['group']
            self.channel_layer.group_discard(group, self.channel_name)
            self.sessions.pop(session_key)
            await self.channel_layer.group_send(group,
                                                {
                                                    'type': 'send_message',
                                                    'username': username,
                                                    'event': 'Disconnected'
                                                })
            await self.update_db(username, ' Disconnected!', room_id)

        except KeyError:
            print("This user has no permission to join this chat room!")



    async def receive(self, *args, **kwargs):
        response = json.loads(kwargs.get('text_data'))
        room_id = self.scope['url_route']['kwargs']['room_id']
        message = response.get("message", None)
        session_key = self.scope['cookies']['session_key']
        username = self.sessions[session_key]['username']
        await self.channel_layer.group_send(
            str(room_id),
            {
                'type'    : 'send_message',
                'username':  username,
                'message' :  message,
                'event'   : 'NewMessage',

            }
        )
        await self.update_db(username, '-->'+message, room_id)

    async def send_message(self, res):
        await self.send(text_data=json.dumps({
            "payload": res,
        }))
