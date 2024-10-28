from faststream import Producer

class OutputLayer:
    def __init__(self):
        self.kafka_producer = Producer(broker_url="kafka://localhost:9092")

    def write_to_console(self, data):
        # Output to console
        print(data.json())

    def write_to_file(self, data, file_path):
        # Output to a JSON file
        with open(file_path, 'w') as file:
            file.write(data.json())

    async def write_to_kafka(self, topic, data):
        # Publish to a Kafka topic
        await self.kafka_producer.publish(data.json(), topic=topic)