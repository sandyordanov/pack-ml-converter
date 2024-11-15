import os

"""
Created by 
Summary: Class in charge of outputting JSON object to selected output destination
"""

class OutputProcessor:
    def __init__(self):
        pass

    #Created by
    def write_to_console(self, data):
        # Output to console
        print(data.json())

    #Created by
    def write_to_file(self, tag, file_name):
        # Output to a JSON file
        with open(os.path.join("testData", file_name), 'w') as file:
            string_var = f"{tag.name.upper()},{tag.state.name.upper()}"
            file.write(string_var)

    #Created by
    async def write_to_kafka(self, topic, data):
        pass
        # Publish to a Kafka topic
