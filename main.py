import json
from domain.message import Message
from domain.production_line import ProductionLine
from domain.node import Node
from input.file_input import FileInput
from output.output_processor import OutputProcessor


def input_console(production_line):
    print("Please enter a JSON message or type 'stop' to end the program.")
    prev_start = False
    prev_stop =  False
    while True:
        user_input = input("Enter your input: ")

        if user_input.lower() == 'stop':
            print("Program stopped.")
            break

        try:
            # Parse JSON input
            data = json.loads(user_input)

            # Extract relevant fields
            data_entity_name = data.get("DataEntityName", "")
            node_name, action = data_entity_name.split("_")
            payload = data.get("Payload")  # Get the payload from the JSON
            timestamp = data.get("Timestamp")

            # Determine start and stop based on action
            dataEntity = action.lower()
            if(dataEntity == "stop"):
               stop = payload
               start =  prev_start
            elif (dataEntity == "start"):
                start = payload
                stop = prev_stop

            # Create a Message object with the payload included
            data_var = Message(node_name, start, stop, timestamp, payload)
            prev_start =  start
            prev_stop =  stop
            # Update the corresponding node in the production line
            tag = production_line.update_node(data_var)

            # Print the current state if it was successfully updated
            if tag is not None:
                print(f"Current State of {node_name}: {tag.state}")
                output_procesor = OutputProcessor()
                output_procesor.write_to_file(tag,'output.txt')
        except json.JSONDecodeError:
            print("Invalid input format. Please enter a valid JSON message.")
        except ValueError:
            print("Invalid DataEntityName format. Expected format: '<name>_<action>'.")

import json
import time
from input.file_input import FileInput  # Ensure FileInput is properly implemented and imported
from domain.message import Message
from output.output_processor import OutputProcessor

def automatic_input_console(production_line):
    print("Running Script")
    prev_start = False
    prev_stop = False
    file_reader = FileInput('example.txt')
    
    for line in file_reader.read_lines_with_delay():
        try:
            # Parse the line as JSON to get a dictionary
            data = json.loads(line)

            # Extract relevant fields from the JSON data
            data_entity_name = data.get("DataEntityName", "")
            node_name, action = data_entity_name.split("_")
            payload = data.get("Payload")
            timestamp = data.get("Timestamp")

            # Determine start and stop based on action
            data_entity = action.lower()
            if data_entity == "stop":
                stop = payload
                start = prev_start
            elif data_entity == "start":
                start = payload
                stop = prev_stop

            # Create a Message object with the payload included
            data_var = Message(node_name, start, stop, timestamp, payload)
            prev_start = start
            prev_stop = stop

            # Update the corresponding node in the production line
            tag = production_line.update_node(data_var)
            if tag is not None:
                print(f"Current State of {node_name}: {tag.state}")
                
                # Instantiate OutputProcessor and write to file
                output_processor = OutputProcessor()
                output_processor.write_to_file(tag, 'output.txt')

        except json.JSONDecodeError:
            print("Error: Line is not a valid JSON format.")
        except ValueError:
            print("Error: Invalid DataEntityName format. Expected format: '<name>_<action>'.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")



def main():
    production_line = ProductionLine()

    # Example of adding nodes
    production_line.add_node(Node(name="n105"))
    production_line.add_node(Node(name="n115"))
    production_line.add_node(Node(name="n120"))
    production_line.add_node(Node(name="n125"))
    production_line.add_node(Node(name="n135"))
    production_line.add_node(Node(name="n140"))
    production_line.add_node(Node(name="n145"))
    production_line.add_node(Node(name="n160"))

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
            pass
            #message_creator = MessageCreator()
            #message_creator.get_messages_continually()
        elif choice == '3':
            automatic_input_console(production_line)
        elif choice == '4':

            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()