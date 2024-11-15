from enum import Enum

class errorCause(Enum):
    Receive_Tasklist_TimeOut =2
    Product_Not_Valid=3
    Operation_Cancelled = 4
    Authorization_TimeOut =5     
    