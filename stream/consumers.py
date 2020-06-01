import os
import subprocess
import asyncio

from channels.generic.websocket import AsyncJsonWebsocketConsumer

class StreamConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.accept()
        filename = '/var/log/syslog'
        lines = subprocess.check_output(['tail', '-10', filename])
        # for line in (thefile.readlines() [-10:]):
        for line in lines.decode().split('\n'):
            if line: 
                await self.send_json(str(line))

        thefile = open(filename,"r")
        thefile.seek(0, os.SEEK_END)
        # reach the end of file
        while 1:
            line = thefile.readline()
            if not line:
                await asyncio.sleep(3)
            if line:
                await self.send_json(str(line))
