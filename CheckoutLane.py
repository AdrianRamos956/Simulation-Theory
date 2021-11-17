"""
CheckoutLane.py
"""
import queue
import Customer


class CheckoutLane:

    def __init__(self, number):
        self.number = number
        self.num_customers = 0
        self.total_customers = 0
        self.customer_queue = [] * self.number

    # Called when customer 1 Event is triggered
    def customer_exit(self, lane):
        self.customer_queue[lane].pop(0)
        self.num_customers -= 1

    # Called when customer 0 Event is triggered
    def customer_enter(self, customer):
        self.num_customers += 1
        self.total_customers += 1
        self.customer_queue[customer.lane_nr].append(customer)

    # Calculates average number of customers waiting in current lanes queue
    def average_customers_waiting(self):
        ct = 0
        for i in self.customer_queue:
            if len(i) >= 1:
                ct += len(i) - 1
        return ct

    def get_first_customer(self):
        return self.customer_queue[0]


    
    


