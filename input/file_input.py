import os
import time
from input.input import Input
import json
"""
Created by Aga Henriquez
Summary: child class that is called when inputting data from a file
"""
class FileInput(Input):
    def __init__(self, file_name):
        # Construct the file path to the testData folder
        self.file_path = os.path.join("testData", file_name)
        super().__init__()

    #Created by Aleksandar
    def automatic_input_console(self):
        print("Running Script")
        file_reader = FileInput('example.txt')

        for line in file_reader.read_lines_with_delay():
            try:
                # Parse the line as JSON to get a dictionary
                file_data = json.loads(line)
                self.process_data(file_data)

            except json.JSONDecodeError:
                print("Error: Line is not a valid JSON format.")
            except ValueError:
                print("Error: Invalid DataEntityName format. Expected format: '<name>_<action>'.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

    #Created by Aleksandar
    def read_lines_with_delay(self):
        try:
            with open(self.file_path, 'r') as file:
                for line in file:
                    yield line.strip()  # Return the line value as a generator
                    time.sleep(1)       # Wait 5 seconds before proceeding to the next line
        except FileNotFoundError:
            print(f"The file {self.file_path} was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")