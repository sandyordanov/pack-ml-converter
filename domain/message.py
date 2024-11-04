class Message:
    def __init__(self, name: str, start: bool, stop: bool, timestamp: int):
        self.name = name
        self.start = start
        self.stop = stop
        self.timestamp = timestamp

    def __repr__(self):
        return f"Data(name={self.name}, start={self.start}, stop={self.stop}, timestamp={self.timestamp})"
