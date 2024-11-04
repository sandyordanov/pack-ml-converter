import json
from domain.message import Message
from domain.production_line import ProductionLine
from domain.node import Node

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
            current_state = production_line.UpdateNode(data_var)

            # Print the current state if it was successfully updated
            if current_state is not None:
                print(f"Current State of {node_name}: {current_state}")

        except json.JSONDecodeError:
            print("Invalid input format. Please enter a valid JSON message.")
        except ValueError:
            print("Invalid DataEntityName format. Expected format: '<name>_<action>'.")


# The rest of the program remains the same
def input_jsonFile():
    name = input("What is your name? ")
    print(f"Nice to meet you, {name}!")

def input_kafkaTopic():
    color = input("What's your favorite color? ")
    print(f"{color} is a nice color!")

def goodbye():
    print("Goodbye! Have a great day!")

# Main function to control the flow
def main():
    production_line = ProductionLine()

    # Example of adding nodes
    production_line.add_node(Node(name="n105"))  # Add node n105
    # You can add more nodes as needed

    while True:
        print("\n---//PackML Converter\\---")
        print("\nChoose an input option:")
        print("1. Console")
        print("2. Json file")
        print("3. Kafka topic")
        print("4. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == '1':
            input_console(production_line)  # Pass the production_line argument
        elif choice == '2':
            input_jsonFile()
        elif choice == '3':
            input_kafkaTopic()
        elif choice == '4':
            goodbye()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


# #productionLine Object
# void UpdateNode(Message message)
# {
#     For each node in nodes
#     {
#         if node.name == message.name
#             node.UpdateState(message)
#             PackTagConverter.ConvertNodeToPacktag(node)
#     }
#     #error handling
# }


# #PackTagConverter Object
# ConvertNodeToPacktag(node)
# {
    
# }


# #Node Object
# UpdateState(Message message)
# {

#     #insert logic




#     CalculateTime()
# }

# CalculateTime()
# {
#     CalculateElapsedTime()
#     CalculateAverageTime()
# }