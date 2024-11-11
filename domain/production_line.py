from domain.message import Message
from domain.stage import stage
from domain.states import State
from processing.packtag_converter import PackTagConverter
from output.output_processor import OutputProcessor
from domain.pack_tag import PackTag


class ProductionLine:
    def __init__(self):
        self.stages = []

    def add_stage(self, stage):
        self.stages.append(stage)

    def update_stage(self, message: Message):
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

    def update_stage2(self, message: Message):
        for stage in self.stages:
            if stage.name == message.name:
                stage_found = True
                stage.update_state(message)
                tag = PackTagConverter.convert_stage(stage)
                return tag