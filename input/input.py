from processing.message import Message
from processing.production_line import ProductionLine
from processing.stage import Stage
from processing.packtag_converter import PackTagConverter



class Input:
    def __init__(self):
        self.production_line = ProductionLine()
        self.create_NX4()
        pass
    def create_NX4(self):
        # Example of adding nodes
        self.production_line.add_stage(Stage(name="n105"))
        self.production_line.add_stage(Stage(name="n115"))
        self.production_line.add_stage(Stage(name="n120"))
        self.production_line.add_stage(Stage(name="n125"))
        self.production_line.add_stage(Stage(name="n135"))
        self.production_line.add_stage(Stage(name="n140"))
        self.production_line.add_stage(Stage(name="n145"))
        self.production_line.add_stage(Stage(name="n160"))

    def process_data(self, input):
        message = Message()
        packtag_converter = PackTagConverter()
        message.parse_incoming_data(input)

        stage_updated = self.production_line.update_stage(message)
        packtag_converter.convert_stage_to_packtag(stage_updated)

        #add output logic
