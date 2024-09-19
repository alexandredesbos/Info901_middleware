from abc import ABC


class Message(ABC):
    def __init__(self, src=None, payload=None, dest=None, stamp=None):
        self.src = src
        self.payload = payload
        self.dest = dest
        self.stamp = stamp

class BroadcastMessage(Message):
    def __init__(self, src, payload, stamp):
        super().__init__(src=src, payload=payload, stamp=stamp)


class MessageTo(Message):
    def __init__(self, timestamp, payload, sender, receiver):
        super().__init__(src=sender, payload=payload, stamp=timestamp)
        self.receiver = receiver
    
    def getSender(self):
        return self.src 
    
    def getReceiver(self):
        return self.receiver
    
class Token:
    def __init__(self, holder_id):
        self.holder_id = holder_id

    def getHolder(self):
        return self.holder_id

    def setHolder(self, holder_id):
        self.holder_id = holder_id
