import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'test'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
    
    async def websocket_receive(self, event):
        text_data_json = json.loads(event['text'])
        message = text_data_json['message']
        print("----------------------------------------------------Recieve")
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat.message',
                'message': message
            }
        )
    # async def receive(self, text_data=None, bytes_data=None):
    #     print(help(self))
    #     text_data_json = json.loads(text_data)
    #     message = text_data_json['message']
    #     print("----------------------------------------------------Recieve")
    #     await self.channel_layer.group_send(
    #         self.room_group_name,
    #         {
    #             'type': 'chat.message',
    #             'message': message
    #         }
    #     )

    async def chat_message(self, event):
        message = event['message']
        print("----------------------------------------------------chat_message")
        await self.send(text_data=json.dumps({"type":"chat","message":message}))
        
    async def disconnect(self, event):
        print("______________________Channels Disconnected__________________________")
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        
        
        
        

#------------------------------------Don't look down here, in bangla: Sorom kore---------------------------------------------------

# import json
# from channels.generic.websocket import AsyncConsumer
# from asgiref.sync import async_to_sync


# class ChatConsumer(AsyncConsumer):
#     async def websocket_connect(self, event):
#         self.room_group_name = 'test'

#         await self.channel_layer.group_add(
#             self.room_group_name,
#             self.channel_name
#         )

#         await self.send({'type':'websocket.accept'})

#     async def websocket_receive(self, event):
#         text_data_json = json.loads(event['text'])
#         message = text_data_json['message']
#         print("----------------------------------------------------Recieve")
#         await self.channel_layer.group_send(
#             self.room_group_name,
#             {
#                 'type': 'chat.message',
#                 'message': message
#             }
#         )

#     async def chat_message(self, event):
#         print(help(event))
#         message = event
#         print("----------------------------------------------------chat_message")
#         await self.send({
#             'type': 'websocket.send',
#             'text': json.dumps({"message":message})
#         })
        
#     async def websocket_disconnect(self, event):
#         print("______________________Channels Disconnected__________________________")
#         await self.channel_layer.group_discard(
#             self.room_group_name,
#             self.channel_name
#         )