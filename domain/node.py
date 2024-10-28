from domain.states import State
class Node:
    def __init__(self,name, state=State.Off):
        self.name = name
        self.start = False
        self.stop = False
        self.error = False
        self.state = state

    def set_state(self):
        # Example logic to return current state based on start/stop conditions
        if self.start:
            self.state = State.Execute
        elif self.stop:
            self.state = State.Idle
        elif self.error:
            self.state = State.Aborted
        else:
            self.error = True
            self.state = State.Aborted

        