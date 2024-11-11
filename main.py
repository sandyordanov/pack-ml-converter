import json
from domain.message import Message
from domain.production_line import ProductionLine
from domain.stage import Stage
from input.file_input import FileInput
from output.output_processor import OutputProcessor

def input_console(production_line):
    print("Please enter a JSON message or type 'stop' to end the program.")
    while True:
        user_input = input("Enter your input: ")

        if user_input.lower() == 'stop':
            print("Program stopped.")
            break

        try:
            message = Message()
            message.parse_incoming_data(user_input)

            stage_updated = production_line.update_stage(message)

            # Print the current state if it was successfully updated
            if tag is not None:
                print(f"Current State of {node_name}: {tag.state}")
                output_procesor = OutputProcessor()
                output_procesor.write_to_file(tag,'output.txt')
        except json.JSONDecodeError:
            print("Invalid input format. Please enter a valid JSON message.")
        except ValueError:
            print("Invalid DataEntityName format. Expected format: '<name>_<action>'.")


def main():
    production_line = ProductionLine()

    # Example of adding nodes
    production_line.add_stage(Stage(name="n105"))
    production_line.add_stage(Stage(name="n115"))
    production_line.add_stage(Stage(name="n120"))
    production_line.add_stage(Stage(name="n125"))
    production_line.add_stage(Stage(name="n135"))
    production_line.add_stage(Stage(name="n140"))
    production_line.add_stage(Stage(name="n145"))
    production_line.add_stage(Stage(name="n160"))

    while True:
        print("\n---//PackML Converter\\---")
        print("\nChoose an input option:")
        print("1. Console")
        print("2. MessageCreator")
        print("3. File")
        print("4. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == '1':
            input_console(production_line)  # Pass the production_line argument
        elif choice == '2':
            message_creator = MessageCreator()
            message_creator.get_messages_continually()
        elif choice == '3':
            file_reader = FileInput('example.txt')

            for line in file_reader.read_lines_with_delay():
                print(line)  # Or process the line in some other way
        elif choice == '4':

            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()