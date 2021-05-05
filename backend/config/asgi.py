import os

from channels import routing
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application

from backend.boards import routing as boards_routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")

application = routing.ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            routing.URLRouter(boards_routing.websocket_urlpatterns)
        ),
    }
)
