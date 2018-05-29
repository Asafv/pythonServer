"""
chat_server.py is used like Socket.IO chat
"""

from flask import Flask
from concurrent import futures
from config import Config

import proto.chat_pb2_grpc as rpc
import proto.chat_pb2 as chat
from services.ChatServiceImpl import ChatServiceImpl as chatService

import grpc
import time

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/keep-alive")
def keep_alive():
    return "Alive!"


@app.route("/getAllMessages")
def get_all_messages():
    return chatService.get_messages(chatServiceImpl)


class ChatServer(rpc.ChatServerServicer):
    def __init__(self):
        self.chat_messages = []

    def ChatStream(self, request, context):
        last_index = 0

        while True:
            while len(self.chat_messages) > last_index:
                n = self.chat_messages[last_index]
                last_index += 1
                yield n

    def SendText(self, request: chat.Text, context):
        print("SendText: {} {}".format(request.name, request.msg))
        self.chat_messages.append(request)
        return chat.Empty()


if __name__ == '__main__':
    app.run(port=3000)
    port = Config.PORT
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    rpc.add_ChatServerServicer_to_server(ChatServer(), server)
    print("chat server listening... {}".format(port))
    server.add_insecure_port('[::]:' + str(port))
    server.start()
    while True:
        time.sleep(64 * 64 * 100)
