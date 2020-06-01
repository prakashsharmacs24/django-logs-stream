from channels.routing import ProtocolTypeRouter, URLRouter
from stream.consumers import StreamConsumer
from django.conf.urls import url

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        url("ws/stream/", StreamConsumer),
    ])
})
