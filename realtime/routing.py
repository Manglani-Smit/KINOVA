from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    # Room code URL se extract hoga: ws://<host>/ws/kinova/<room_code>/
    re_path(r'ws/kinova/(?P<room_code>\w+)/$', consumers.KinovaConsumer.as_asgi()),
]