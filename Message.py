from abc import ABC


class Message(ABC):
    def __init__(self, src=None, payload=None, dest=None, stamp=None):
        self.src = src # Le processus qui envoie le message
        self.payload = payload # Le contenu du message
        self.dest = dest # Le processus destinataire
        self.stamp = stamp # L'horloge de Lamport au moment de l'envoi

class BroadcastMessage(Message):
    def __init__(self, src, payload, stamp):
        super().__init__(src=src, payload=payload, stamp=stamp)


class MessageTo(Message):
    def __init__(self, timestamp, payload, sender, receiver):
        super().__init__(src=sender, payload=payload, stamp=timestamp)
        self.receiver = receiver  # Destinataire
    
    def getSender(self):
        return self.src 
    
    def getReceiver(self):
        return self.receiver
