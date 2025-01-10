from faststream import FastStream
from faststream.kafka import KafkaBroker
from confluent_kafka import Consumer
import subprocess


def run_kafka_input():
    """
    Continuously listens for messages on the 'Dummies' Kafka topic and prints them to the console.
    """
    consumer = Consumer({
        'bootstrap.servers': '192.168.1.62:9092',  # Kafka broker's IP and port
        'group.id': 'my-group',
        'auto.offset.reset': 'earliest',  # Start reading from the earliest available message
    })

    # Subscribe to the topic
    consumer.subscribe(['Dummies'])

    print("Listening to Kafka topic 'Dummies'... Press Ctrl+C to stop.")
    try:
        while True:
            msg = consumer.poll(1.0)  # Poll for messages
            if msg is None:
                continue  # No messages available, keep polling
            if msg.error():
                print(f"Consumer error: {msg.error()}")
                continue

            # Decode and print the message
            print(f"Received message: {msg.value().decode('utf-8')}")
    except KeyboardInterrupt:
        print("\nStopping Kafka consumer...")
    finally:
        consumer.close()

def consume_kafka_messages():
    # Run kafkacat as a subprocess to consume messages from the 'Dummies' topic
    command = ["kafkacat", "-b", "192.168.1.62:9092", "-t", "Dummies", "-C"]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    try:
        # Read the messages as they come in
        while True:
            output = process.stdout.readline()
            if output == b'' and process.poll() is not None:
                break
            if output:
                print(f"Received message: {output.decode().strip()}")
    except KeyboardInterrupt:
        print("\nStopping Kafka consumer...")
    finally:
        process.terminate()  # Terminate kafkacat process when done

def main():
    """
    Entry point of the script.
    """
    consume_kafka_messages()
    #run_kafka_input()


if __name__ == "__main__":
    main()
