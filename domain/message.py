class Message:
    def __init__(self, name: str, payload: bool, timestamp: int):
        self.name = name
        self.payload = payload
        self.timestamp = timestamp

    def __repr__(self):
        return f"Data(name={self.name}, payload={self.payload}, timestamp={self.timestamp})"