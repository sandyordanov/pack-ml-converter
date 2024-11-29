import os
import time
from input.input import Input
import json
from processing.parser import Parser
"""
Created by Aga Henriquez Edited by Dion
Summary: child class that is called when inputting data from a file
"""
class FileInput(Input):
    def __init__(self, file_name):
        self.file_path = os.path.join("testData", file_name)
        super().__init__()

    def automatic_input_console(self):
        """
        Reads lines from the file with a delay, parses them, and returns parsed data.
        """
        print("Running Script")
        try:
            with open(self.file_path, 'r') as file:
                for line in file:
                    # Read and strip each line
                    user_input = line.strip()
                    if not user_input:
                        continue  # Skip empty lines

                    try:
                        # Parse the input using the Parser class
                        parsed_data = self.send_to_parser(user_input)

                        if not isinstance(parsed_data, Parser):
                            raise TypeError("Parsed data is not of type Parser.")
                        
                        yield parsed_data  # Yield a Parser object
                    except Exception as e:
                        print(f"Error parsing line: {user_input}. Error: {e}")

                    time.sleep(1)  # Add a delay between lines
        except FileNotFoundError:
            print(f"The file {self.file_path} was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")



