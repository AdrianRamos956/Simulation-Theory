"""
CheckoutLane.py
"""
import queue
import Customer
import queue


class CheckoutLane:

    def __init__(self, number):
        self.number = number
        self.num_customers = 0
        self.total_customers = 0
        self.customer_queue = queue.Queue()

    # Called when customer 1 Event is triggered
    def customer_exit(self):
        self.customer_queue.get()
        self.num_customers -= 1

    # Called when customer 0 Event is triggered
    def customer_enter(self, customer):
        self.num_customers += 1
        self.total_customers += 1
        self.customer_queue.put(customer)

    def average_customers_waiting(self):
        """
        Calculates average number of customers waiting in current lanes queue
        :return:
        """
        ct = 0
        for i in self.customer_queue:
            if len(i) >= 1:
                ct += len(i) - 1
        return ct

