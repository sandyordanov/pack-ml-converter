from domain.state import State
import json
import os

class PackTagConverter:

    #written by Aga
    
    def __init__(self):
        pass


    def convert_stage_to_packtag(self, stage): # converts update stage info to packtag
        # Convert enum state to its name (string representation of the enum member)
        state_name = stage.state.name if isinstance(stage.state, State) else str(stage.state)

        # Convert PackTag instance to JSON-compatible format (dictionary)
        pack_tag_data = {
            "name": stage.name,
            "command": {
                "UnitMode": None,
                "UnitModeChangeRequest": None,  
                "MachSpeed": None,
                "CntrlCmd": None,
                "CmdChangeRequest": None
            },
            "status": {
                "UnitModeCurrent": None,  
                "StateCurrent": state_name,  
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
        return pack_tag_json
