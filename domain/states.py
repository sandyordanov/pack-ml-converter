from enum import Enum

# class syntax
class State(Enum):
    Off = 1
    Idle = 2
    Starting = 3 
    Execute = 4
    Complete = 5
    Stopping = 6
    Aborting = 7
    Aborted = 8 
    Clearing = 9
    Stopped = 10
    Resetting = 11 
    Held = 12
    Holding = 13
    Unholding = 14
    Suspended =15
    Suspending = 16
    Unsuspending =17