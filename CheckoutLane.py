"""
CheckoutLane.py
"""
import queue


class CheckoutLane:

    def __init__(self, number):
        self.number = number
        self.num_customers = 0
        self.total_customers = 0
        self.customer_queue = [] * self.number
    
    def customer_exit(self,lane):
        self.customer_queue[lane].pop(0)
        self.num_customers -= 1

    def customer_enter(self, customer):
        self.num_customers += 1
        self.total_customers += 1
        self.customer_queue[customer.lane].append(customer)
        
    def average_customers_waiting(self):
        ct = 0
        for i in self.customer_queue:
            if len(i) >= 1:
                ct += len(i) - 1
        return ct


    
    


