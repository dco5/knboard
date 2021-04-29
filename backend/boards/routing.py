from django.urls import path

from . import consumers

websocket_urlpatterns = [path("ws/board/<board_id>", consumers.BoardConsumer.as_asgi())]
