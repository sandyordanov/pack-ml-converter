# domain/message.py
class Message:
    def __init__(self, name, start, stop, timestamp, payload):
        self.name = name
        self.start = start
        self.stop = stop
        self.timestamp = timestamp
        self.payload = payload  # New attribute

    def __repr__(self):
        return f"Message(name={self.name}, start={self.start}, stop={self.stop}, timestamp={self.timestamp}, payload={self.payload})"
