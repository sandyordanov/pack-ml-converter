from input.file_input import FileInput
from input.console_input import ConsoleInput
from input.kafka_input import KafkaInput
from processing.production_line import ProductionLine
from processing.stage import Stage
from domain.state import State
from processing.packtag_converter import PackTagConverter
from output.output_processor import OutputProcessor

production_line = ProductionLine()

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
            #kafka_input = KafkaInput();
            
            pass

        elif choice == '3':
            file_input = FileInput("example.txt")
            parsed_data = file_input.automatic_input_console()
            handle_parsed_data(parsed_data)
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
    #output_processor.write_to_kafka(packtag)
    #output_processor.write_to_console(packtag)
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