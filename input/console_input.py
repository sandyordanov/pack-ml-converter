from domain.message import Message

class ConsoleInput:
    def __init__(self):
        pass

    @staticmethod
    def read_console_input():
        print("Please enter a series of simulated values in the format: <name> <start> <stop> <timestamp>.")
        print("Use '1' or '0' for start and stop values, and type 'stop' to end the program.")

        while True:
            user_input = input("Enter your input: ")

            if user_input.lower() == 'stop':
                print("Program stopped.")
                break

            data_split = user_input.split()

            if len(data_split) < 4:
                print("Invalid input format. Please provide <name> <start> <stop> <timestamp>.")
                continue

            name = data_split[0]
            start = (data_split[1] == '1')
            stop = (data_split[2] == '1')
            timestamp = int(data_split[3])

            # Create a Message object with start and stop
            data_var = Message(name, start, stop, timestamp)

            # Process the data here
            print("You entered:", data_var)
            return data_var


