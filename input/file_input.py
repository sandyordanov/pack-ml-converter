import os
import time

class FileInput:
    def __init__(self, file_name):
        # Construct the file path to the testData folder
        self.file_path = os.path.join("testData", file_name)

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