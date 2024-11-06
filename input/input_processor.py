import json
from domain.message import Message

class InputStream:
    def __init__(self):
        pass

    def process_data(self, input_string):
        data = json.loads(input_string)

        data_entity_name = data.get("DataEntityName", "")

        node_name, action = data_entity_name.split("_")
        payload = data.get("Payload")  # Get the payload from the JSON
        timestamp = data.get("Timestamp")

        # Determine start and stop based on action
        action = action.lower()
        if (action == "stop"):
            stop = True
            start = False
        elif (action == "start"):
            start = True
            stop = False
        # Create a Message object with the payload included
        message = Message(node_name, start, stop, timestamp, payload)
        return message
