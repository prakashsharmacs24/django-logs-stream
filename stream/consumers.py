import os
import subprocess
import asyncio

from channels.generic.websocket import AsyncJsonWebsocketConsumer
from .utils import get_last_lines
class StreamConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.accept()
        filename = '/var/log/syslog'
        thefile = open(filename,"rb")

        for line in get_last_lines(thefile, 10):
            if line: 
                await self.send_json(str(line))

        thefile.seek(0, os.SEEK_END)
        # reach the end of file
        while 1:
            line = thefile.readline()
            if not line:
                await asyncio.sleep(3)
            if line:
                await self.send_json(str(line))
