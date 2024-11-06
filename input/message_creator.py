import time

class MessageCreator:
    def __init__(self):
        self.switch = 0

    @staticmethod
    def create_message_N105start_false():
        # Each time we create a message, we assign a new timestamp
        return {
            "DataEntityName": "N105_Start",
            "Payload": 0,
            "PayloadModelName": "bool",
            "PayloadModelVersion": "",
            "Timestamp": 1717144039141,
            "version": "1.0.0"
        }

    @staticmethod
    def create_message_N105start_true():
        # Each time we create a message, we assign a new timestamp
        return {
            "DataEntityName": "N105_Start",
            "Payload": 1,
            "PayloadModelName": "bool",
            "PayloadModelVersion": "",
            "Timestamp": 1717144039141,
            "version": "1.0.0"
        }

    @staticmethod
    def create_message_N105stop_false():
        # Each time we create a message, we assign a new timestamp
        return {
            "DataEntityName": "N105_Stop",
            "Payload": 0,
            "PayloadModelName": "bool",
            "PayloadModelVersion": "",
            "Timestamp": 1717144039141,
            "version": "1.0.0"
        }

    @staticmethod
    def create_message_N105stop_true():
        # Each time we create a message, we assign a new timestamp
        return {
            "DataEntityName": "N105_Stop",
            "Payload": 1,
            "PayloadModelName": "bool",
            "PayloadModelVersion": "",
            "Timestamp": 1717144039141,
            "version": "1.0.0"
        }
