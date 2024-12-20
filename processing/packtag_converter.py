from domain.state import State
from domain.EndCode import EndCode
import os

"""
Created by Aga Henriquez
Summary: Class in charge of converting a Stage Object into a JSON Object
"""

class PackTagConverter:
    def __init__(self):
        pass

    # Created by Aga Henriquez
    def convert_stage_to_packtag(self, stage):
        # Check if stage is None
        if stage is None:
            raise ValueError("The 'stage' object is None. Please ensure it is properly initialized.")

        # Convert enum state to its name (string representation of the enum member)
        state_name = stage.name
        exec_time = stage.execute_time
        endcode_name = stage.endCode.name if isinstance(stage.endCode, EndCode) else str(stage.endCode)
        state_name = stage.state.name if isinstance(stage.state, State) else str(stage.state)

        # Capitalize the state_name

        state_name = state_name.upper()

        # Create pack tag data
        pack_tag_data = {
            "name": stage.name.upper(),
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
                "ExecuteTime": exec_time,
                "MachSpeed": None,
                "CurMachSpeed": None,
                "EquipmentInterlock.Blocked": None,
                "EquipmentInterlock.Starved": None
            },
            "admin": {
                "StopReason.ID": endcode_name,
                "ProdProcessedCount[#].Count": None,
                "ProdDefectiveCount[#].Count": None
            }
        }

        # Return the pack tag data as a JSON object (Python dictionary)
        return pack_tag_data
