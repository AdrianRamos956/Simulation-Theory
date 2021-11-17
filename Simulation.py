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
        self.rand = 0
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
        random.seed(self.rand_seed)
        # Service time of customer
        time_service = inv_transform(self.customer_service_rate)
        # Current customer to add to queue
        new_customer = Customer.Customer(0.0, time_service)
        # Current lane for adding customers to
        current_lane = self.checkout_lanes[0]
        # Add initial customer to Queue at time 0.0
        self.event_queue.put(SimEvent.SimEvent(0, SimEvent.CUSTOMER_READY, current_lane, new_customer))
        self.event_queue.put(SimEvent.SimEvent(sim_time + time_service, SimEvent.CUSTOMER_COMPLETE, current_lane, new_customer))
        # Run simulation for specified duration
        while not self.event_queue.empty() and sim_time >= sim_end_time:
            current_event = self.event_queue.get()
            current_event.handle_event()
            sim_time = current_event.time
            customer_arrival = self.generate_rand(self.customer_arrival_rate)
            time_service = generate_rand(self.customer_service_rate)
            new_customer = Customer.Customer(customer_arrival + sim_time, time_service)
            current_lane = self.checkout_lanes[new_customer.set_lane_nr(self.checkout_lanes)]
            self.event_queue.put(SimEvent.SimEvent(sim_time, SimEvent.CUSTOMER_READY,customer_arrival, current_lane, new_customer))
            self.event_queue.put(SimEvent.SimEvent(sim_time + time_service, SimEvent.CUSTOMER_COMPLETE, current_lane, new_customer))
        pass

    # Creates lanes based off of the amount of lanes given on the command line
    def create_lanes(self):
        for i in range(self.num_checkout_lanes):
            list.append(CheckoutLane.CheckoutLane(i))


# Uniform transformation function for interarrival times
def inv_transform(rand, lam):
    return round((-np.log(1 - rand) * lam))


# Random number generator
def generate_rand(rate):
    return inv_transform(random.uniform(0, 1), rate)
    
