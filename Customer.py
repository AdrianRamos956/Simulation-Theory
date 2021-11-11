"""
Customer.py
"""


class Customer:
    time_in = int()
    time_out = int()
    time_waited = int()
    lane = int()

    def __init__(self, time_in):
        self.time_in = time_in
