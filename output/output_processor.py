import os
from input.input import Input
from faststream import FastStream
from faststream.kafka import KafkaBroker
import json
"""
Created by 
Summary: Class in charge of outputting JSON object to selected output destination
"""
  #Created by Dion
class OutputProcessor:
    def __init__(self):
        pass

  
    def write_to_console(self, data):
        # Output to console
        print(f"Converted JSON PackTag: {data}")

    #written by Dion
    def write_to_file(self, pack_tag_json): # writes packtag to specific file

        output_file_path = './testData/output.txt'
            # # Ensure the directory exists before writing
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

        # # Write the JSON data to the file
        with open(output_file_path, 'w') as output_file:
             output_file.write(pack_tag_json)

    def write_runtime_data_to_file(self, pack_tag_json):  # writes packtag to specific file

        output_file_path = './testData/runtime.txt'
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

        with open(output_file_path, 'w') as output_file:
            output_file.writelines(pack_tag_json)

    async def write_to_kafka(self, topic, data):
        try:
                    # Ensure data is JSON-formatted
                    message = json.dumps(data)

                    # Publish the message to the Kafka topic
                    await self.broker.publish(topic, message)

                    print(f"Message successfully published to topic '{topic}'")

        except Exception as e:
                    print(f"Error publishing message to Kafka: {e}")
        pass
        # Publish to a Kafka topic




