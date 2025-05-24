from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # 接受 WebSocket 连接
        await self.accept()

    async def disconnect(self, close_code):
        # 断开连接时的处理
        pass

    async def receive(self, text_data):
        # 接收客户端消息
        text_data_json = json.loads(text_data)
        print(text_data_json)
        message = text_data_json["message"]

        # 发送消息回客户端
        await self.send(text_data=json.dumps({
            "message": f"You said: {message}"
        }))