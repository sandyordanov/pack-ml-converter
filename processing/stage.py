from domain.state import State
import time

from tenacity import sleep

"""
Created by 
Summary: Class that updates PackML state of a stage, as well as calculate time.
"""

class Stage:

#written by Merna

    def __init__(self, name, state=State.Idle):
        self.name = name
        self.start = False
        self.stop = False
        self.error = False
        self.state = state
        self.previous_start = False
        self.previous_stop = False
        self.previous_time = None
        self.execute_time = None

    def get_execute_time(self):
        #by Aleksandar
        while self.state == State.Execute:
            sleep(1)
            self.execute_time +=1
            yield self


    #Created by
    def calculate_time(self, current_time):
        if self.previous_time is not None:
            elapsed_time = current_time - self.previous_time
            print(f"Elapsed Time: {elapsed_time} seconds")
            return elapsed_time

        else:
            print("No previous timestamp to calculate elapsed time.")
            return None
    #Created by
    def update_state(self, message):
     elapsed_time = self.calculate_time(message.timestamp)

     # Update previous_time with the current message's timestamp
     self.previous_time = message.timestamp

     # Update start and stop based on the message
     self.start = message.start
     self.stop = message.stop

     # State transition logic
     if self.start and self.stop:
         # Error condition if both start and stop are active
         self.state = State.Aborted
         self.error = True
     elif self.stop:
         if self.state == State.Stopping:
             # Transition from Execute to Complete after stopping
             self.state = State.Complete
         else:
             # Set state to Stopped when stop is True but not in Execute
             self.state = State.Stopped
     elif self.start:
         if self.state in (State.Idle, State.Stopped):
             # Start operation from Idle or Stopped
             self.state = State.Execute
         elif self.state == State.Execute:
             # Already executing, we could remain in Execute
             pass
     else:
         if self.state == State.Execute:
             # If neither start nor stop is true while executing, transition to Complete
             self.state = State.Idle
         elif self.state == State.Stopped:
             # Default back to Idle if no signals and not in Stopped
             self.state = State.Idle

    

     # Debugging output
     
      # Update previous values for the next call
     self.previous_start = self.start
     self.previous_stop = self.stop
     print(f"Previous Start: {self.previous_start}, Previous Stop: {self.previous_stop}")
     print(f"Current State: {self.state}")
     return self.state
