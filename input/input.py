from processing.parser import Parser

"""
Created by Aga Henriquez
Summary: Parent class that holds an object of ProductionLine and processes inputted data by calling various class methods
"""


class Input:
    def __init__(self):
        pass

<<<<<<< HEAD
    #Created by
    def process_data(self, input):
        message = Message()
        message.parse_incoming_data(input)
        packtag_converter = PackTagConverter()
        
        output = OutputProcessor()
        
        stage_updated = self.production_line.update_stage(message)
        packtag = packtag_converter.convert_stage_to_packtag(stage_updated)
        output.write_to_file(packtag)
        #output_processor.write_to_kafka(packtag)
        output.write_to_console(packtag)
        #add output logic
=======
    #created by Aga
    def send_to_parser(self, raw_data):
        parser = Parser()
        parser.parse_incoming_data(raw_data)

        return Parser

>>>>>>> develop
