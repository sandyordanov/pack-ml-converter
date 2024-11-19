from enum import Enum

class endCode(Enum):
    Not_Active = 0
    Normal_End =1
    Receive_Tasklist_TimeOut =2
    Product_Not_Valid=3
    Operation_Cancelled = 4
    Authorization_TimeOut =5     
    