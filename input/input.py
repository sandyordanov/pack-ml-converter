from processing.parser import Parser

"""
Created by Aga Henriquez
Summary: Parent class that holds an object of ProductionLine and processes inputted data by calling various class methods
"""


class Input:
    def __init__(self):
        pass

    #created by Aga
    def send_to_parser(self, raw_data):
        parser = Parser()
        parser.parse_incoming_data(raw_data)

        return Parser

