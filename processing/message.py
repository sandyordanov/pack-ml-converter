import json

"""
Created by 
Summary: class that parses and stores incoming data for processing
"""

class Message:
    def __init__(self):
        self.stage_name = None
        self.start = False
        self.stop = False
        self.timestamp = None
        self.payload = None

    #Created by
    def __repr__(self):
        return f"Message(name={self.stage_name}, start={self.start}, stop={self.stop}, timestamp={self.timestamp}, payload={self.payload})"

    #Created by
    def parse_incoming_data(self, input_string):

        data = json.loads(input_string)

        data_entity_name = data.get("DataEntityName", "")
        self.stage_name, action = data_entity_name.split("_")
        self.payload = data.get("Payload")
        self.timestamp = data.get("Timestamp")

        self.start_stop_decision(action)

    #Created by
    def start_stop_decision(self, action):
        data_entity = action.lower()
        if data_entity == 'stop':
            self.stop = True

        elif data_entity == "start":
            self.start = True