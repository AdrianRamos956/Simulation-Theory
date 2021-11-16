"""
Customer.py
"""
import CheckoutLane as cl
import math

class Customer:
    
    def __init__(self, time_in, time_service, number):
        self.time_in = time_in
        # Int Variable
        self.time_out = None
        # Int Variable
        self.time_waited = None
        # Int Variable
        self.lane = None
        # Float Variable
        self.time_service = time_service
        #Int Variable
        #for log file
        self.number = number
    
    def set_lane(self):
        number_of_lanes = len(cl.queue)
        shortest_lane_length = math.inf
        shortest_lane = 0
        for i in range(number_of_lanes):
            if(len(cl.queue[i])<shortest_lane_length):
                shortest_lane = i
        self.lane = shortest_lane
        return shortest_lane

    def log_in(self):
        file1 = open("log.txt", "a")
        file1.write("Time: %2f Customer %d enters check-out lane %d", (self.time_in, self.number, self.lane))
        file1.close()

    def log_out(self,time):
        self.time_out = time + self.time_service
        file1 = open("log.txt", "a")
        file1.write("Time: %2f Customer %d exits check-out lane %d", (self.time_out, self.number, self.lane))
        file1.close()

    def customer_time_waited_calc(self, time_when_at_front):
        self.time_waited = time_when_at_front - self.time_in


        
        






