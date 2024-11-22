from enum import Enum

<<<<<<<< HEAD:domain/endCode.py
class endCode(Enum):
    Not_Active = 0
    Normal_End =1
========
class EndCode(Enum):
>>>>>>>> 33f2dc3640fc0aa9d9e22e617e75a8264b87955c:domain/EndCode.py
    Receive_Tasklist_TimeOut =2
    Product_Not_Valid=3
    Operation_Cancelled = 4
    Authorization_TimeOut =5     
    