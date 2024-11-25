import unittest
from domain.state import State
from domain.EndCode import EndCode
from processing.stage import Stage 

class TestStage(unittest.TestCase):
    def test_initialization(self):
        stage = Stage("TestStage")
        self.assertEqual(stage.name, "TestStage")
        self.assertEqual(stage.state, State.Idle)
        self.assertEqual(stage.endState, EndCode.Not_Active)
        self.assertFalse(stage.start)
        self.assertFalse(stage.stop)
        self.assertIsNone(stage.endCode)

    def test_calculate_time(self):
        stage = Stage("TestStage")
        stage.previous_time = 100
        current_time = 200
        elapsed_time = stage.calculate_time(current_time)
        self.assertEqual(elapsed_time, 100)

        # Test without a previous_time
        stage.previous_time = None
        elapsed_time = stage.calculate_time(current_time)
        self.assertIsNone(elapsed_time)
    
    def test_update_state(self):
        class MockMessage:
            def __init__(self, start, stop, endCode, timestamp):
                self.start = start
                self.stop = stop
                self.endCode = endCode
                self.timestamp = timestamp

        stage = Stage("TestStage")

        # Transition from Idle to Execute
        message = MockMessage(start=True, stop=None, endCode=0, timestamp=10)
        state = stage.update_state(message)
        self.assertEqual(state, State.Execute)

     # Transition from Execute to Complete
        message = MockMessage(start=None, stop=True, endCode=0, timestamp=20)
        state = stage.update_state(message)
        self.assertEqual(state, State.Complete)

        # Error condition with high endCode
        message = MockMessage(start=False, stop=None, endCode=2, timestamp=30)
        state = stage.update_state(message)
        self.assertEqual(state, State.Aborted)
        self.assertTrue(stage.error)
   
    
def test_check_endCode(self):
        class MockMessage:
            def __init__(self, endCode):
                self.endCode = endCode

        stage = Stage("TestStage")

        # Valid endCode
        message = MockMessage(endCode=0)
        stage.check_endCode(message)
        self.assertFalse(stage.error)

        # error endCode
        message = MockMessage(endCode=2)
        stage.check_endCode(message)
        self.assertTrue(stage.error)
