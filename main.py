from domain.message import Message
def input_console():
    print("Please enter a series of simulated values separated by spaces. Type 'stop' to end the program.")

    while True:
        # Get the user input
        user_input = input("Enter your input: ")

        # Check if the input is 'stop' to end the program
        if user_input.lower() == 'stop':
            print("Program stopped.")
            break
        
        #Data processing
        data_splitted = user_input.split()
        name = data_splitted[0]
        payload = (data_splitted[1] == '1')
        timestamp = int(data_splitted[2])

        data_var = Message(name,payload,timestamp)
        # Process the data here
        print("You entered:", data_var.__repr__)
        # production_line.UpdateNode(data_var)



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
    while True:
        print("\n---//PackML Converter\\---")
        print("\nChoose an input option:")
        print("1. Console")
        print("2. Json file")
        print("3. Kafka topic")
        print("4. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == '1':
            input_console()
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