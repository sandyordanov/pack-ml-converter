from input.input import Input
import json
"""
Created by Aga Henriquez
Summary: child class that is called when inputting data from command line
"""
class ConsoleInput(Input):
    def __init__(self):
        super().__init__()

    #Created by Aleksandar
    def input_console(self):
        print("Please enter a JSON message or type 'stop' to end the program.")
        while True:
            user_input = input("Enter your input: ")

            if user_input.lower() == 'stop':
                print("Program stopped.")
                break

            try:
                parsed_data = self.send_to_parser(user_input)
                return parsed_data

            except json.JSONDecodeError:
                print("Invalid input format. Please enter a valid JSON message.")
            except ValueError:
                print("Invalid DataEntityName format. Expected format: '<name>_<action>'.")

