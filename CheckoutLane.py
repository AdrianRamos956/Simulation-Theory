"""
CheckoutLane.py
"""
import queue


class CheckoutLane:
    num_customers = int()
    customer_queue = queue.Queue()

    def __init__(self, number):
        self.number = number
