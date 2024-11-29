import json

"""
Created by ?? edited by Dion
Summary: class that parses and stores incoming data for processing
"""

class Parser:
    def __init__(self):
        self.stage_name = None
        self.start = False
        self.stop = False
        self.timestamp = None
        self.payload = None
        self.endCode = -1
    #Created by
    def __repr__(self):
        return f"Message(name={self.stage_name}, start={self.start}, stop={self.stop}, timestamp={self.timestamp}, payload={self.payload}, endcode={self.endCode})"

    #Created by 
    def parse_incoming_data(self, input_string):

        print(f"Parsing incoming data in parser: {input_string} (Type: {type(input_string)})")  # Debugging line
        if isinstance(input_string, str):  # Ensure it's a string
            try:
                data = json.loads(input_string)  # This will raise an exception if the string is not valid JSON
            except json.JSONDecodeError as e:
                print(f"JSONDecodeError: {e} - The string could not be parsed into JSON")
                raise
        else:
            raise TypeError(f"Expected input_string to be a string, got {type(input_string)}")




        #data = json.loads(input_string)

        data_entity_name = data.get("DataEntityName", "")
        stage_name, action = data_entity_name.split("_")
        self.stage_name = stage_name
        self.payload = data.get("Payload")
        self.timestamp = data.get("Timestamp")
        #self.endCode = data.get("EndCode")
        data_entity = action.lower()
        if data_entity == 'stop':
         self.stop = self.payload
         self.start = None
         #self.endCode = -1
        elif data_entity == "start":
         self.start = self.payload
         self.stop = None
         #self.endCode = -1
        elif data_entity == "end":
          self.endCode = self.payload
   
        
            
            