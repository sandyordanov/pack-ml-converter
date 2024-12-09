from faststream import FastStream
from faststream.kafka import KafkaBroker

broker = KafkaBroker("192.168.1.62:9092")  # Kafka broker address
app = FastStream(broker)
print(" sybscribe")
    # Subscribe to 'Dummies' topic
@broker.subscriber("Dummies")  # Replace with your actual topic name
async def process_kafka_message(message: str):
    """  
    Print the incoming Kafka messages.
    """
    print(f"Received message: {message}")