import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync,sync_to_async
from .models import Message
from user.models import MyUser
from channels.db import database_sync_to_async
# from django.contrib.auth.models import User	
class ChatConsumer(AsyncWebsocketConsumer):
	async def connect(self):
		self.room_name = self.scope['url_route']['kwargs']['room_name']
		self.room_group_name = 'chat_%s' % self.room_name

		await self.channel_layer.group_add(
			self.room_group_name,
			self.channel_name
		)

		await self.accept()

	async def disconnect(self, close_code):
		await self.channel_layer.group_discard(
			self.room_group_name,
			self.channel_name
		)

	async def receive(self, text_data):
		text_data_json = json.loads(text_data)
		message = text_data_json['message']
		username = text_data_json['username']
		receiver = MyUser.objects.get(
            username=self.room_group_name.replace('chat_', '')
                                    .replace(self.scope['user'].username, '')
                                    .replace('-', ''))
		Message(sender=self.scope['user'], receiver=receiver, content=message).save()

		await self.channel_layer.group_send(
			self.room_group_name,
			{
				'type': 'chat_message',
				'message': message,
				'username':username
			})

	async def chat_message(self, event):
		message = event['message']

		await self.send(text_data=json.dumps({
			'message': message,
			'username':event['username']
		}))
