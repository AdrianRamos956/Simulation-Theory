"""
SimEvent.py
"""
import sys

CUSTOMER_READY = 0
CUSTOMER_COMPLETE = 1


# event_type: CUSTOMER_READY | CUSTOMER_COMPLETE
class SimEvent:
    lane = -1

    def __init__(self, event_type):
        self.event_type = event_type
        if event_type == 1:
            print('CUSTOMER_READY event must have a lane.')
            sys.exit()

    def __init__(self, event_type, lane):
        self.event_type = event_type
        self.lane = lane
