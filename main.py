import json
from domain.message import Message
from domain.production_line import ProductionLine
from domain.node import Node
from input.file_input import FileInput

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
            current_state = production_line.update_node(data_var)

            # Print the current state if it was successfully updated
            if current_state is not None:
                print(f"Current State of {node_name}: {current_state}")

        except json.JSONDecodeError:
            print("Invalid input format. Please enter a valid JSON message.")
        except ValueError:
            print("Invalid DataEntityName format. Expected format: '<name>_<action>'.")


def main():
    production_line = ProductionLine()

    # Example of adding nodes
    production_line.add_node(Node(name="n105"))  # Add node n105
    # You can add more nodes as needed

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