from input.input import Input
from faststream import FastStream
from faststream.kafka import KafkaBroker
import json

# created by Dion

class KafkaInput(Input):
    def __init__(self):
        super().__init__()
        self.broker = KafkaBroker("localhost:9092")
        self.app = FastStream(self.broker)


async def start_processing(self):
        """Start FastStream to listen for Kafka messages."""
        await self.app.start()

        @self.broker.subscriber("omron.packaging.nx-3.teststation.plc.Status.StateCurrent")
        async def process_kafka_message(self, message):
                """Process Kafka message and call self.process_data directly."""
                    # Call the custom method to process the data
                self.send_to_parser(self,message)
#         @broker.subscriber("omron.packaging.nx-3.teststation.plc.Status.StateCurrent")
#         @broker.publisher("omron.packaging.nx-3.teststation.packml.Status.StateCurrentStr")
