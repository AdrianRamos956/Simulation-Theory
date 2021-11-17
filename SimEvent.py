"""
SimEvent.py
"""
import sys
import CheckoutLane

CUSTOMER_READY = 0
CUSTOMER_COMPLETE = 1


# event_type: CUSTOMER_READY | CUSTOMER_COMPLETE
class SimEvent:

    def __init__(self, time, event_type, lane, customer):
        self.event_type = event_type
        self.lane = lane
        self.customer = customer
        self.time = time

    def handle_event(self):
        """
        Perform the action associated with this event.

        :return: none
        """
        if self.event_type == CUSTOMER_READY:
            self.lane.customer_enter(self.customer)
        elif self.event_type == CUSTOMER_COMPLETE:
            self.lane.customer_exit()

