from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class NewConsumer(WebsocketConsumer):

    def connect(self):
        
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

        self.send(text_data = json.dumps({'message' : 'You are connected to Django'}))
    
    def receive(self , text_data):
        #text_data = json.loads(text_data)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,{
                'type' : 'send_message',
                'payload' : text_data
            }
        )

        #self.send(text_data = json.dumps({'answer' : text_data }))


    def disconnect(self, *args , **kwargs):
        print('Disconnected')

    def send_message(self , event):
        data = event['payload']
        data = json.loads(data)
        self.send(text_data = json.dumps({'answer' : data }))

