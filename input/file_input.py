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
        self.file_path = os.path.join("testData", file_name)
        super().__init__()

    def automatic_input_console(self):
        print("Running Script")
        for line in self.read_lines_with_delay():
            try:
                yield line  # Yield raw JSON lines to the caller
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

    def read_lines_with_delay(self):
        try:
            with open(self.file_path, 'r') as file:
                for line in file:
                    yield line.strip()  # Return lines one by one
                    time.sleep(1)       # Add a delay between lines
        except FileNotFoundError:
            print(f"The file {self.file_path} was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
