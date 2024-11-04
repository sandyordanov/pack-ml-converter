from domain.message import Message
from domain.production_line import ProductionLine
from domain.node import Node


def input_console(production_line):
    print("Please enter a series of simulated values in the format: <name> <start> <stop> <timestamp>.")
    print("Use '1' or '0' for start and stop values, and type 'stop' to end the program.")

    while True:
        user_input = input("Enter your input: ")

        if user_input.lower() == 'stop':
            print("Program stopped.")
            break
        
        data_splitted = user_input.split()
        
        if len(data_splitted) < 4:
            print("Invalid input format. Please provide <name> <start> <stop> <timestamp>.")
            continue

        name = data_splitted[0]
        start = (data_splitted[1] == '1')
        stop = (data_splitted[2] == '1')
        timestamp = int(data_splitted[3])

        # Create a Message object with start and stop
        data_var = Message(name, start, stop, timestamp)

        # Process the data here
        print("You entered:", data_var)

        # Update the corresponding node in the production line and capture the state
        current_state = production_line.UpdateNode(data_var)
        
        # Print the current state if it was successfully updated
        if current_state is not None:
            print(f"Current State of {name}: {current_state}")


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