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
        self.rand_seed = int(sys.argv[1])
        self.rand = 0
        self.sim_duration_minutes = int(sys.argv[2])
        self.num_checkout_lanes = int(sys.argv[3])
        self.customer_arrival_rate = int(sys.argv[4])
        self.customer_service_rate = int(sys.argv[5])
        self.stats.set_p_no_customers(self.customer_arrival_rate, self.customer_service_rate)
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
        customer_number = 0
        sim_time = 0.0
        self.create_lanes()
        random.seed(self.rand_seed)
        # Service time of customer
        customer_service_time = generate_rand(self.customer_service_rate)
        # Current customer to add to queue
        customer_number = customer_number + 1
        new_customer = Customer.Customer(0.0, customer_service_time, customer_number )
        # Current lane for adding customers to
        current_lane = self.checkout_lanes[0]
        # Add initial customer to Queue at time 0.0
        self.event_queue.put(SimEvent.SimEvent(0, SimEvent.CUSTOMER_READY, current_lane, new_customer))
        self.event_queue.put(
            SimEvent.SimEvent(sim_time + customer_service_time, SimEvent.CUSTOMER_COMPLETE, current_lane, new_customer))
        # Run simulation for specified duration
        while not self.event_queue.empty() and sim_time <= sim_end_time:
            current_event = self.event_queue.get()
            current_event.handle_event()
            sim_time = current_event.time
            # because the next customer's arrival is only based on the previous customer's arrival,
            # only create new events if the event in the eventqueue was an arrival
            if current_event.event_type == SimEvent.CUSTOMER_READY:
                customer_arrival_time = generate_rand(self.customer_arrival_rate)
                customer_service_time = generate_rand(self.customer_service_rate)
                customer_time_in = customer_arrival_time + sim_time
                #print(customer_time_in)
                customer_number = customer_number + 1
                new_customer = Customer.Customer(customer_arrival_time + sim_time, customer_service_time, customer_number )
                current_lane = self.checkout_lanes[new_customer.set_lane_nr(self.checkout_lanes)]
                self.event_queue.put(
                    SimEvent.SimEvent(new_customer.time_in, SimEvent.CUSTOMER_READY, current_lane, new_customer))
                self.event_queue.put(
                    SimEvent.SimEvent(new_customer.time_in + new_customer.time_service, SimEvent.CUSTOMER_COMPLETE, current_lane, new_customer))
                    
        while not self.event_queue.empty():
            current_event = self.event_queue.get()
            current_event.handle_event()
            sim_time = current_event.time
            customer_number = customer_number + 1
            #print(customer_number)

    # Creates lanes based off of the amount of lanes given on the command line
    def create_lanes(self):
        for i in range(self.num_checkout_lanes):
            self.checkout_lanes.append(CheckoutLane.CheckoutLane(i))


# Uniform transformation function for interarrival times
def inv_transform(rand, lam):
    return (-np.log(1 - rand) * 1/lam)


# Random number generator
def generate_rand(rate):
    return inv_transform(random.uniform(0, 1), rate)
