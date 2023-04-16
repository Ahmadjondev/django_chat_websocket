from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        print("Connected")
        self.accept()

    def disconnect(self, code):
        print("Disconnected")
        pass

    def receive(self, text_data=None, bytes_data=None):
        print(type(text_data))
        self.send(text_data)
