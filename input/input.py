from domain.message import Message
from domain.production_line import ProductionLine
from domain.stage import Stage



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
        message.parse_incoming_data(input)

        stage_updated = self.production_line.update_stage(message)

        #add output logic
