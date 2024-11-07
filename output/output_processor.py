import os

class OutputProcessor:
    def __init__(self):
        pass

    def write_to_console(self, data):
        # Output to console
        print(data.json())

    def write_to_file(self, tag, file_name):
        # Output to a JSON file
        with open(os.path.join("testData", file_name), 'w') as file:
            string_var = f"{tag.name.upper()},{tag.state.name.upper()}"
            file.write(string_var)

    async def write_to_kafka(self, topic, data):
        pass
        # Publish to a Kafka topic
