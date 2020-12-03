import asyncio
import argparse
from config import Config

config = Config()

class Client():
    def __init__(self, args):
        self.ip='127.0.0.1'
        self.port=args.port
        self.name=args.name

    async def srio(self, message):
        reader, writer = await asyncio.open_connection(self.ip, self.port)
        writer.write(message.encode())
        resp = await reader.read(config.MAX_LEN)
        print(resp.decode())
        writer.close()

    def run_forever(self):
        while True:
            message = input("Next message: ")
            if message == "quit":
                break
            else:
                asyncio.run(self.srio(message))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=12245)
    parser.add_argument('--name', type=str, default='client')
    args=parser.parse_args()
    client = Client(args)
    client.run_forever()
