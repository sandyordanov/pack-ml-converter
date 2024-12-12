from faststream import FastStream
from faststream.kafka import KafkaBroker

broker = KafkaBroker("192.168.1.62:9092")  # Kafka broker address
app = FastStream(broker)
print(" sybscribe")
    # Subscribe to 'Dummies' topic
#while True:
@broker.subscriber("Dummies")  
    
def process_kafka_message(message: str) ->str: 
            print(f"Received message: {message}")
            print(" hie")

# import asyncio
# from aiokafka import AIOKafkaConsumer

# async def consume_messages():
#     # Kafka Consumer Configuration
#     consumer = AIOKafkaConsumer(
#         'Dummies',  # Kafka topic to subscribe to (Dummies)
#         bootstrap_servers='192.168.1.62:9092',  # Kafka broker address
#         group_id='test-group'  # Consumer group ID
#     )

#     # Start the consumer
#     await consumer.start()

#     try:
#         # Continuously listen for new messages in the topic
#         async for msg in consumer:
#             # Print the message value
#             print(f"Received message: {msg.value.decode()}")
#     finally:
#         # Make sure to stop the consumer when done
#         await consumer.stop()