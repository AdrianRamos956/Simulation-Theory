"""
SimEvent.py
"""
import sys
import CheckoutLane

CUSTOMER_READY = 0
CUSTOMER_COMPLETE = 1


# event_type: CUSTOMER_READY | CUSTOMER_COMPLETE
class SimEvent:

    def __init__(self, event_type, lane_nr, customer):
        self.event_type = event_type
        self.lane = lane_nr
        if event_type == CUSTOMER_READY:
            # Place customer in lane number
            CheckoutLane.CheckoutLane.customer_enter(self, customer)
        elif event_type == CUSTOMER_COMPLETE:
            # Remove customer from current lane
            CheckoutLane.CheckoutLane.customer_exit(self, lane_nr)
