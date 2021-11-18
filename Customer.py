"""
Customer.py
"""
import CheckoutLane as cl
import math


class Customer:

    def __init__(self, time_in, time_service):
        self.time_in = int(time_in)
        # Int Variable
        self.time_out = int()
        # Int Variable
        self.time_waited = int()
        # Int Variable
        self.lane_nr = int()
        # Float Variable
        self.time_service = time_service

    # Sets customers current lane based off of which lane as the shortest queue
    def set_lane_nr(self, lane_list):
        number_of_lanes = len(lane_list)
        shortest_lane_length = math.inf
        shortest_lane_nr = 0
        for i in range(number_of_lanes):
            if lane_list[i].customer_queue.qsize() < shortest_lane_length:
                shortest_lane_nr = i
        self.lane_nr = shortest_lane_nr
        return shortest_lane_nr

    # Writes out to the log file whenever a customer is added
    def log_in(self):
        file1 = open("logfile.txt", "a")
        file1.write("Time: %2f Customer enters check-out lane %d\n" % (self.time_in, self.lane_nr))
        file1.close()

    # Writes out to the log file whenever a customer has left a queue
    def log_out(self, time):
        self.time_out = time
        file1 = open("logfile.txt", "a")
        file1.write("Time: %2f Customer exits check-out lane %d\n" % (self.time_out, self.lane_nr))
        file1.close()

    # Calculates time waited for each customer
    def customer_time_waited_calc(self, time_when_at_front):
        self.time_waited = time_when_at_front - self.time_in
