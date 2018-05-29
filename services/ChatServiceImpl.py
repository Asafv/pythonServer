class ChatServiceImpl:

    def __init__(self):
        self.messages = {}

    def get_messages(self):
        return self.messages

    def add_messages(self, message):
        self.messages[message.id] = message
