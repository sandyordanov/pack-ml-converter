from processing.parser import Parser

"""
Created by 
Summary: class that holds a list of all stages of a production line.
"""

class ProductionLine:
    #written by Dion

    def __init__(self):
        self.stages = []

    #Created by
    def add_stage(self, stage):
        self.stages.append(stage)

    #Created by
    def update_stage(self, message: Parser): # searches stagename and forwards the stage to update_state function.
        stage_found = False
        
        for stage in self.stages:
            if stage.name == message.stage_name:
                stage_found = True
                try:
                    stage.update_state(message)
                    return stage
                except Exception as e:
                    print(f"Error updating stage '{stage.name}': {e}")
                    return  # Exit or skip further processing on failure

                break

        if not stage_found:
            print(f"No stage found with the name '{message.stage_name}'.")
