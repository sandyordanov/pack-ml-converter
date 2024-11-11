from domain.state import State
import json
import os

class PackTagConverter:
    def __init__(self):
        pass


    def convert_stage_to_packtag(self, stage):
        # Convert enum state to its name (string representation of the enum member)
        state_name = stage.state.name if isinstance(stage.state, State) else str(stage.state)

        # Convert PackTag instance to JSON-compatible format (dictionary)
        pack_tag_data = {
            "name": stage.name,  # Replace with actual name if available
            "command": {
                "UnitMode": None,
                "UnitModeChangeRequest": None,  # Example mapping; adapt based on requirements
                "MachSpeed": None,
                "CntrlCmd": None,
                "CmdChangeRequest": None
            },
            "status": {
                "UnitModeCurrent": None,  # Using `state` from Stage, if relevant
                "StateCurrent": state_name,  # Convert enum state to string (name of the enum member)
                "MachSpeed": None,
                "CurMachSpeed": None,
                "EquipmentInterlock.Blocked": None,
                "EquipmentInterlock.Starved": None
            },
            "admin": {
                "StopReason.ID": None,
                "ProdProcessedCount[#].Count": None,
                "ProdDefectiveCount[#].Count": None
            }
        }

               # Convert to JSON string
        pack_tag_json = json.dumps(pack_tag_data, indent=4)  # Adding indent for better readability

        # Debug output (to the console)
        print(f"Converted JSON PackTag: {pack_tag_json}")

        # Write the JSON string to the output file
        output_file_path = './testData/output.txt'

        # Ensure the directory exists before writing
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

        # Write the JSON data to the file
        with open(output_file_path, 'w') as output_file:
            output_file.write(pack_tag_json)
