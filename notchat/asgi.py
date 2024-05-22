import os

from django.core.asgi import get_asgi_application

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

import rooms.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "notchat.settings")

# application = get_asgi_application()
application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            URLRouter(rooms.routing.websocket_urlpatterns)
        ),
    }
)

app = application


# import os
# import sys
# from django.core.asgi import get_asgi_application

# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter

# import rooms.routing

# # add your project directory to the sys.path
# project_home = '/home/ahosseini/notchat'
# if project_home not in sys.path:
#     sys.path.insert(0, project_home)

# # set environment variable to tell django where your settings.py is
# os.environ['DJANGO_SETTINGS_MODULE'] = 'notchat.settings'


# # serve django via WSGy
# application = ProtocolTypeRouter(
#     {
#         "http": get_asgi_application(),
#         "websocket": AuthMiddlewareStack(
#             URLRouter(rooms.routing.websocket_urlpatterns)
#         ),
#     }
# )
