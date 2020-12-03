import asyncio
import aiohttp
import argparse
from json import dumps
from time import time
from re import sub
from config import Config

config = Config()

class Server:
    def __init__(self, name, port, servers=list(), ip='127.0.0.1'):
        self.name=name
        self.port=port
        self.ip=ip
        self.record = dict()
        self.neighbor_server=dict()
        self.server = None
        for name, port in servers:
            self.neighbor_server[port]=name

    def start(self):
        try:
            asyncio.run(self.run())
        except KeyboardInterrupt:
            self.make_log(f"Close server {self.name} by KeyboardInterrupt")
            self.server.close()  # Check this

    async def handle_connection(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        message = (await reader.read(config.MAX_LEN)).decode()
        self.make_log(f"{self.name} Received: {message}")
        await self.handle_message(message, writer)

    async def handle_message(self, message, writer):
        result = None
        try:
            arguments = message.split()
            result = await self.message_handler(arguments[0], arguments[1:], writer)
        except (IndexError, KeyError):
            await self.respondas(f"? {message}", writer)
        finally:
            writer.close()
            await writer.wait_closed()
            try:
                assert result is None
            except AssertionError:
                await self.forwardas(result)

    async def forwardas(self, message):
        await asyncio.gather(*map(lambda port_name: self._forwardas(message, *port_name), self.neighbor_server.items()))

    async def _forwardas(self, message, port, name):
        try:
            await self.send(message, port)
            self.make_log(f"{self.name} connects to {name}")
            self.make_log(f"{self.name} forward {str(message)}")
        except IOError:
            self.make_log(f"{self.name} failed to connect to {name}")

    async def send(self, message, port):
        reader, writer = await asyncio.open_connection(port=port)
        writer.write(message.encode())
        await writer.drain()
        writer.close()
        await writer.wait_closed()

    async def run(self):
        self.server = await asyncio.start_server(self.handle_connection, self.ip, self.port)
        self.make_log(f'{self.name} start serving')
        print(f"{self.name} initiated Successfully")
        async with self.server:
            await self.server.serve_forever()

    def message_handler(self, messageID, content, writer):
        if messageID == "IAMAT":
            return self.IA_handler(content, writer)
        if messageID == "WHATSAT":
            return self.WH_handler(content, writer)
        if messageID == "AT":
            return self.AT_handler(content, writer)

    async def IA_handler(self, content, writer):
        client, coord, client_time = content
        message = f"AT {self.name} {str(time() - float(client_time))} {client} {coord} {client_time}"
        self.record[client] = f"{client} {coord} {client_time}"
        await self.respondas(message, writer)
        return message

    async def WH_handler(self, content, writer):
        client, radius, count = content
        message = self.record[client]
        coord = message.split()[1]
        jsons = await self.location_search(coord, radius, count)
        await self.respondas(f'{message}\n{jsons}', writer)

    async def AT_handler(self, content, writer):
        _, time_diff, client, coord, client_time = content
        message = f"AT {self.name} {str(time() - float(client_time))} {client} {coord} {client_time}"
        try:
            assert f"{client} {coord} {client_time}" == self.record[client]
        except (KeyError, AssertionError):
            self.record[client] = f"{client} {coord} {client_time}"
            return message
        finally:
            await self.respondas(message, writer)

    @staticmethod
    async def location_search(coord, radius, count):
        results = await Server.make_request(coord, radius, config.APIKey)
        assert results['status'] == 'OK'
        del results['results'][int(count):]
        jsons = dumps(results, indent=4)
        return jsons

    @staticmethod
    async def make_request(loc, rad, key):
        lat_long = sub('([+-][0-9]+.[0-9]+)([+-][0-9]+.[0-9]+)', r'\1,\2', loc)
        async with aiohttp.ClientSession() as session:
            async with session.get("{}?key={}&location={}&radius={}".format(
                    config.URL, key, lat_long, int(rad)*1000)) as response:
                return await response.json()

    @staticmethod
    def make_log(message):
        with open("log.txt", "a+") as f:
            f.write(message + "\n")

    async def respondas(self, message, writer):
        self.make_log(f'{self.name} responds {message}')
        writer.write(str(message).encode())
        await writer.drain()



def initiate_servers(name):
    edge_index = list()
    for neighbor_server in config.connections[name]:
        edge_index.append((neighbor_server, config.ports[neighbor_server]))
    Server(name, config.ports[name], servers=edge_index).start()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--server_name', default='Hill', type=str)
    args = parser.parse_args()
    initiate_servers(args.server_name)