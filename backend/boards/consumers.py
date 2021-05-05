import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class BoardConsumer(WebsocketConsumer):

    @staticmethod
    def _get_group_name(group_id):
        return f"board-{group_id}"

    def connect(self):
        print(f"connected")

        board_id = self.scope["url_route"]["kwargs"]["board_id"]
        try:
            async_to_sync(self.channel_layer.group_add)(
                self._get_group_name(board_id), self.channel_name
            )
        except Exception as e:
            print(e)

        self.accept()

    def disconnect(self, code):
        print("disconnect")
        super().disconnect(code)

    def receive(self, text_data=None, bytes_data=None, **kwargs):
        try:
            text_data_json = json.loads(text_data)
            print(text_data_json)
            async_to_sync(self.channel_layer.group_send)(
                self._get_group_name(2),
                {
                    'type': 'new.column',
                    'data': text_data_json,
                    'sender_channel': self.channel_name
                }
            )
        except Exception as e:
            print(e)

    def new_column(self, event):
        try:
            print(event)
            if self.channel_name != event['sender_channel']:
                self.send(text_data=json.dumps(event))
        except Exception as e:
            print(e)
