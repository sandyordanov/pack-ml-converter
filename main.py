import asyncio
from input.file_input import FileInput
from input.console_input import ConsoleInput
from input.kafka_input import KafkaInput
from processing.production_line import ProductionLine
from processing.stage import Stage
from domain.state import State
from processing.parser import Parser
from processing.packtag_converter import PackTagConverter
from output.output_processor import OutputProcessor
from faststream import FastStream
from faststream.kafka import KafkaBroker


production_line = ProductionLine()
async def run_kafka_input():
    """
    Continuously runs KafkaInput to listen for messages on the 'Dummies' topic.
    """
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

    # Start the FastStream application to listen to Kafka messages
    await app.start()

#created by aleksandar
def main():
    create_NX4_line()
    while True:
        print("\n---//PackML Converter\\---")
        print("\nChoose an input option:")
        print("1. Console")
        print("2. Kafka")
        print("3. File")
        print("4. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == '1':
            console_input = ConsoleInput()
            parsed_data = console_input.input_console()

            handle_parsed_data(parsed_data)
            get_runtime_updates()

        elif choice == '2':
            print("Starting Kafka listener... (Press Ctrl+C to stop)")
            try:
                asyncio.run(run_kafka_input())  # Start the Kafka input in an async loop
            except KeyboardInterrupt:
                print("Kafka listener stopped.")   

        elif choice == '3':
            file_input = FileInput("example.txt")
            
            for parser_object in file_input.automatic_input_console():  
                try:
                    handle_parsed_data(parser_object)
                except Exception as e:
                    print(f"Error while processing parsed data: {e}")

       
                
        elif choice == '4':

            break
        else:
            print("Invalid choice. Please try again.")

def get_runtime_updates():
    packtag_converter = PackTagConverter()
    output_processor = OutputProcessor()
    active_stages_tags = []
    for stage in production_line.stages:
        if stage.state == State.Execute:
            active_stages_tags.append(packtag_converter.convert_stage_to_packtag(stage))
    output_processor.write_runtime_data_to_file(active_stages_tags)

#created by Aga
def handle_parsed_data(data):
    packtag_converter = PackTagConverter()
    output_processor = OutputProcessor()

    stage_updated = production_line.update_stage(data)
    packtag = packtag_converter.convert_stage_to_packtag(stage_updated)
    output_processor.write_to_file(packtag)
    output_processor.write_to_database(packtag)
    #output_processor.write_to_kafka(packtag)
    output_processor.write_to_console(packtag)
    #add output logic

#created by Aleksander | edited by Aga
def create_NX4_line():
    # Example of adding nodes
    production_line.add_stage(Stage(name="n105"))
    production_line.add_stage(Stage(name="n115"))
    production_line.add_stage(Stage(name="n120"))
    production_line.add_stage(Stage(name="n125"))
    production_line.add_stage(Stage(name="n135"))
    production_line.add_stage(Stage(name="n140"))
    production_line.add_stage(Stage(name="n145"))
    production_line.add_stage(Stage(name="n160"))


if __name__ == "__main__":
    main()