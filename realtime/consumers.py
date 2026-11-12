# realtime/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class KinovaConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Handle both room_name and room_code safely
        url_kwargs = self.scope.get('url_route', {}).get('kwargs', {})
        room = url_kwargs.get('room_name') or url_kwargs.get('room_code') or 'ALPHA'
        self.room_name = room.upper()
        self.room_group_name = f'kinova_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        if hasattr(self, 'room_group_name'):
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )

    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
            action = data.get('action')
            payload = data.get('payload', {})

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'kinova_broadcast',
                    'action': action,
                    'payload': payload
                }
            )
        except Exception as e:
            print(f"[Kinova WS Error]: {e}")

    async def kinova_broadcast(self, event):
        await self.send(text_data=json.dumps({
            'action': event['action'],
            'payload': event['payload']
        }))