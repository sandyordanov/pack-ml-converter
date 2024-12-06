from processing.parser import Parser
import json
"""
Created by Aga Henriquez
Summary: Parent class that holds an object of ProductionLine and processes inputted data by calling various class methods
"""


class Input:
    def __init__(self):
        pass

    #created by Aga edited by Dion

    def send_to_parser(self, raw_data):
        #print(f"Raw data before parsing: {raw_data} (Type: {type(raw_data)})")  # Debugging line
        parser = Parser()  # Create a Parser instance
        parser.parse_incoming_data(raw_data)  # Populate the Parser instance
        return parser

   

