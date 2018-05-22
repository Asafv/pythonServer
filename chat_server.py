"""
chat_server.py is used like Socket.IO chat
"""

from flask import Flask
from concurrent import futures

import proto.chat_pb2_grpc as rpc
import proto.chat_pb2 as chat

import grpc
import time

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


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
    port = 11912
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    rpc.add_ChatServerServicer_to_server(ChatServer(), server)
    print("chat server listening... {}".format(port))
    server.add_insecure_port('[::]:' + str(port))
    server.start()
    while True:
        time.sleep(64 * 64 * 100)