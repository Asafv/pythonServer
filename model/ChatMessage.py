import uuid


class ChatMessage:

    def __init__(self):
        self.id = uuid.uuid4()
        self.name = ""
        self.msg = ""
        self.timestamp = ""
