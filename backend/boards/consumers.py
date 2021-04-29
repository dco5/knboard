import json

from channels.generic.websocket import WebsocketConsumer


class BoardConsumer(WebsocketConsumer):
    def connect(self):
        print(f"connected")

        self.channel_layer.group_add()
        self.accept()

    def disconnect(self, code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        print(text_data_json)

        self.send(text_data=json.dumps({"message": text_data_json["message"]}))
