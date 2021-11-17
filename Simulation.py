"""
Simulation.py
"""
import sys
import random
import CheckoutLane
import Customer
import SimEvent
import Statistics
import queue
import numpy as np


class Simulation:

    def __init__(self):
        self.logfile = open('logfile.txt', 'a+')
        self.stats = Statistics.Statistics()
        self.rand_seed = sys.argv[1]
        self.sim_duration_minutes = sys.argv[2]
        self.num_checkout_lanes = sys.argv[3]
        self.customer_arrival_rate = sys.argv[4]
        self.customer_service_rate = sys.argv[5]
        self.checkout_lanes = list()
        self.event_queue = queue.Queue()
        # self.current_customer = Customer.Customer()
        # self.current_lane = CheckoutLane.CheckoutLane()

    def start(self):
        """
        begin the simulation
        :return: none
        """
        # TODO SETUP
        # Time used for checking when customers are added to system and when they need to be removed
        sim_end_time = self.sim_duration_minutes
        sim_time = 0.0
        self.create_lanes(self)
        customer_number = 1
        # Random number used for uniform transformation
        rand = self.generate_rand(self.rand_seed)
        # Service time of customer
        time_service = inv_transform(rand, self.customer_service_rate)
        # Current customer to add to queue
        current_customer = Customer.Customer(0.0, time_service, customer_number)
        # Current lane for adding customers to
        current_lane_nr = self.checkout_lanes[0]
        # Add initial customer to Queue at time 0.0
        SimEvent.SimEvent(0, current_lane_nr, current_customer)
        Customer.Customer.log_in(self)
        # Run simulation for specified duration
        while self.sim_duration_minutes != 0:
            if sim_time >= sim_end_time:
                break
            # Add customers to lane in one-time step per the customer arrival rate
            # Create a customer and add them to a lane
            customer_number += 1
            rand = self.generate_rand(self.rand_seed)
            # Perform uniform transformation for customer and add it to current sim_time to accurately detail when
            # it's added to the system
            sim_time += inv_transform(rand, self.customer_arrival_rate)
            rand = self.generate_rand(self.rand_seed)
            time_service = inv_transform(rand, self.customer_service_rate)
            current_customer = Customer.Customer(sim_time, time_service, customer_number)
            current_lane_nr = current_customer.set_lane_nr(self.checkout_lanes)
            SimEvent.SimEvent(0, self.checkout_lanes[current_lane_nr], current_customer)
            Customer.Customer.log_in(self)
            # Check if a customer is ready to be checked out
            for i in range(self.checkout_lanes):
                if self.checkout_lanes[i].checkout_lanes[0].time_ <= sim_time:
                    SimEvent.SimEvent(1, i, current_customer)
                    Customer.Customer.log_out(self, sim_time)
            self.sim_duration_minutes -= 1
        pass

    # Creates lanes based off of the amount of lanes given on the command line
    def create_lanes(self):
        for i in range(self.num_checkout_lanes):
            list.append(CheckoutLane.CheckoutLane(i))


# Uniform transformation function for interarrival times
def inv_transform(rand, lam):
    return round((-np.log(1 - rand) * lam))


# Random number generator
def generate_rand(seed):
    random.seed(seed)
    return random.uniform(0, 1)
