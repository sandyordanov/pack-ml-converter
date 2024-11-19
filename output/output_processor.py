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
        print(f"Converted JSON PackTag: {data}")

    #written by Dion
    def write_to_file(self, pack_tag_json): # writes packtag to specific file

        output_file_path = './testData/output.txt'
            # # Ensure the directory exists before writing
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

        # # Write the JSON data to the file
        with open(output_file_path, 'w') as output_file:
             output_file.write(pack_tag_json)


    async def write_to_kafka(self, topic, data):
        pass
        # Publish to a Kafka topic




