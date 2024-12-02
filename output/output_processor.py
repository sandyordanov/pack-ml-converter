import os
from input.input import Input
#from faststream import FastStream
#from faststream.kafka import KafkaBroker
import json
"""
Created by Dion van der Broek
Summary: Class in charge of outputting JSON object to selected output destination
Reviewed & Edited by Aga Henriquez
"""
# Created by Dion
class OutputProcessor:
    def __init__(self, broker=None):
        self.broker = broker  # Optional broker (used for Kafka if available)

    def write_to_console(self, data):
        # Output to console
        print(f"Converted JSON PackTag: {data}")

    def write_to_file(self, pack_tag_data):  # Writes packtag to a specific file
        """
        Write JSON data to a file (pretty-printed).
        """
        output_file_path = './testData/output.txt'

        # Ensure the directory exists before writing
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

        # Write the JSON data to the file
        with open(output_file_path, 'w') as output_file:
            # Pretty print JSON data
            json.dump(pack_tag_data, output_file, indent=4)

    def write_runtime_data_to_file(self, pack_tag_data):  # Writes packtag to a runtime file
        """
        Write runtime JSON data to a different file (pretty-printed).
        """
        output_file_path = './testData/runtime.txt'

        # Ensure the directory exists before writing
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

        with open(output_file_path, 'w') as output_file:
            # Pretty print JSON data
            json.dump(pack_tag_data, output_file, indent=4)

    async def write_to_kafka(self, topic, data):
        """
        Publish the data to a Kafka topic.
        """
        try:
            if not self.broker:
                print("Kafka broker is not initialized.")
                return

            # Ensure data is JSON-formatted
            message = json.dumps(data)

            # Publish the message to the Kafka topic
            await self.broker.publish(topic, message)

            print(f"Message successfully published to topic '{topic}'")

        except Exception as e:
            print(f"Error publishing message to Kafka: {e}")