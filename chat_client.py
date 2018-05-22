import threading
from datetime import datetime
from tkinter import *
from tkinter import simpledialog

import grpc
import proto.chat_pb2_grpc as rpc
import proto.chat_pb2 as chat

address = 'localhost'
port = 11912


def get_time():
    d = datetime.now()
    return d.strftime("%H:%M")


class ChatClient:

    def __init__(self, u: str, window):
        # frame for UI
        self.window = window
        self.username = u
        # create a gRPC channel + stub
        channel = grpc.insecure_channel(address + ':' + str(port))
        self.conn = rpc.ChatServerStub(channel)
        # create new listening thread for when new message streams come in
        threading.Thread(target=self.__listen_for_messages, daemon=True).start()
        self.__init_ui()
        self.window.mainloop()

    def __listen_for_messages(self):
        for text in self.conn.ChatStream(chat.Empty()):
            print("Receive: [{}] {}".format(text.name, text.msg))
            self.chats.insert(END, "({}) [{}]: {}\n".format(text.timestamp, text.name, text.msg))

    def send_text(self, event):
        msg = self.entry_msg.get()
        if msg is not '':
            t = chat.Text()
            t.name = self.username
            t.msg = msg
            t.timestamp = get_time()
            print("Send: [{}] {} --> {}".format(t.name, t.msg, t.timestamp))
            self.conn.SendText(t)

    def __init_ui(self):
        self.chats = Text()
        self.chats.pack(side=TOP)
        self.lbl_username = Label(self.window, text=self.username)
        self.lbl_username.pack(side=LEFT)
        self.entry_msg = Entry(self.window, bd=5)
        self.entry_msg.bind('<Return>', self.send_text)
        self.entry_msg.focus()
        self.entry_msg.pack(side=BOTTOM)


if __name__ == '__main__':
    root = Tk()
    frame = Frame(root, width=300, height=300)
    frame.pack()
    root.withdraw()
    username = None
    while username is None:
        username = simpledialog.askstring("Username", "What's your username?", parent=root)
    root.deiconify()
    c = ChatClient(username, frame)
