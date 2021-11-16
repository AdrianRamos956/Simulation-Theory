"""
SimEvent.py
"""
import sys
import CheckoutLane
import Customer

CUSTOMER_READY = 0
CUSTOMER_COMPLETE = 1


# event_type: CUSTOMER_READY | CUSTOMER_COMPLETE
class SimEvent:
    lane = -1

    def __init__(self, event_type, lane2=None):
        if lane2 is not None:
            lane = lane2
        self.event_type = event_type
        if event_type == 1 and lane2 == None:
            print('CUSTOMER_READY event must have a lane.')
            sys.exit()
        elif event_type == 1 and lane is not None:
            #Remove customer from current lane
            CheckoutLane.CheckoutLane.customer_exit(self, lane)

    def __init__(self, event_type, lane, customer):
        self.event_type = event_type
        self.lane = lane
        if event_type == 0:
            #Place cutomer in lane number
            CheckoutLane.CheckoutLane.customer_enter(self, customer)
        elif event_type == 1 and lane is not None:
        #Remove customer from current lane
            CheckoutLane.CheckoutLane.customer_exit(self, lane)
        

