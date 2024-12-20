from domain.state import State
from domain.EndCode import EndCode

import time

#from tenacity import sleep

"""
Created by Merna
Summary: Class that updates PackML state of a stage, as well as calculate time.
"""

class Stage:

#written by Merna

    def __init__(self, name, state=State.Idle ,endState = EndCode.Not_Active):
        self.name = name
        self.start = False
        self.stop = False
        self.endCode = None
        self.endState = endState
        self.error = False
        self.state = state
        self.previous_start = False
        self.previous_stop = False
        self.previous_time = None
        self.execute_time = None

    #def set_execute_time(self):
        #by Aleksandar
        while self.state == State.Execute:
            sleep(1)
            self.execute_time +=1


    #Created by Merna
    def calculate_time(self, current_time):
        if self.previous_time is not None:
            elapsed_time = current_time - self.previous_time
            print(f"Elapsed Time: {elapsed_time} seconds")
            return elapsed_time

        else:
            print("No previous timestamp to calculate elapsed time.")
            return None
    #Created by Merna
    def update_state(self, message):
     
     #elapsed_time = self.calculate_time(message.timestamp)
     self.endCode = message.endCode
     check_endCode(self,message)
     # Update previous_time with the current message's timestamp
     self.previous_time = message.timestamp

     # Update start and stop based on the message
     update_start_stop(self, message)
     print(f"ERROR : {self.error}")
     # State transition logic
     if self.error:
        if self.stop == False and self.start == False:
            self.state = State.Idle       
        else:
            self.endState = EndCode
            self.state = State.Aborted
          
     else:
        if self.start and self.stop:
         # Error condition if both start and stop are active
            if self.state == State.Execute:
                self.state = State.Complete
                self.execute_time = 0
                pass
            elif self.state == State.Aborted:
                self.state = State.Aborted
        elif self.stop:
            if self.state ==State.Execute :             
                self.state = State.Complete
                self.execute_time = 0
            elif self.state ==State.Complete :
                pass
            else:
                self.state = State.Aborted
        elif self.start:
            if self.state == State.Idle or self.state == State.Aborted :
                
                self.state = State.Execute
                #self.set_execute_time()
            elif self.state == State.Execute :
                self.state = State.Aborted
        else:
            if self.state == State.Aborted:
                self.state = State.Aborted
            else:
             self.state = State.Idle
             self.execute_time = 0
      # Update previous values for the next call
     self.previous_start = self.start
     self.previous_stop = self.stop
     print(f" Start: {self.start}, Stop: {self.stop}")
     print(f"Current State: {self.state}")
     return self.state
def check_endCode(self,message):
   
    if self.endCode is not None:
     if self.endCode >1:
            self.error = True
            print(f"End code: {message.endCode}")
     else:
            self.error = False
            print(f"End code is FALSE")
            print(f"self End code: {self.endCode}")
            print(f"message End code: {self.endCode}")
    else:
         print(f"End code is none")
def update_start_stop(self, message):
     if message.start == None :
         self.start = self.previous_start
         self.stop = message.stop
     elif message.stop ==  None:
         self.stop = self.previous_stop
         self.start = message.start
     elif message.stop ==  None and message.start ==  None:
          self.stop = self.previous_stop
          self.start = self.previous_start