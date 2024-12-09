from input.input import Input
from faststream import FastStream
from faststream.kafka import KafkaBroker
import json
from processing.parser import Parser

class KafkaInput(Input):
    def __init__(self):
        super().__init__()
        self.broker = KafkaBroker("192.168.1.62:9092")  # Updated to connect to the remote Kafka broker
        self.app = FastStream(self.broker)

    async def start_processing(self):
        """
        Start the Kafka listener using FastStream.
        """
        @self.broker.subscriber("Dummies")
        async def process_kafka_message(message: str):
            """
            Process each Kafka message and send it to the parser.
            """
            print(f"Received message: {message}")  # Debugging line
            try:
                parsed_data = self.send_to_parser(message)
                print(f"Parsed data: {parsed_data}")
                # Here, you can add logic to handle the parsed data (e.g., update stages, etc.)
            except Exception as e:
                print(f"Error processing message: {e}")

        # Start the FastStream application to listen to Kafka messages
        await self.app.start()
