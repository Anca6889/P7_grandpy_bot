from app.config import config as c

class Parser:
    """ This class is parsing the message of the user """

    def __init__(self):
        pass

    def split_message(self, message):

        for words in message.split():
            print(words)

