"""
Simulation.py
"""
import sys
import random
import CheckoutLane
import Customer
import SimEvent
import Statistics
import numpy as np


class Simulation:

    checkout_lanes = list()

    def __init__(self):
        self.logfile = open('logfile.txt', 'a+')
        self.stats = Statistics.Statistics()
        self.rand_seed = sys.argv[1]
        self.sim_duration_minutes = sys.argv[2]
        self.num_checkout_lanes = sys.argv[3]
        self.customer_arrival_rate = sys.argv[4]
        self.customer_service_rate = sys.argv[5]
        self.current_customer = Customer.Customer()
        self.current_lane = CheckoutLane.CheckoutLane()

    def start(self):
        """
        begin the simulation
        :return: none
        """
        #TODO SETUP
        sim_time = 0.0
        self.create_lanes(self)
        seed = str(self.rand_seed)
        customer_number = 1
        N = len(seed)
        R = self.generateR(self, N)
        time_service = self.uniTransform(self.customer_service_rate, N)
        self.current_customer = Customer.Customer.__init__(self, 0.0, time_service,customer_number)
        self.current_lane = CheckoutLane.CheckoutLane.__init__(self, 1)
        SimEvent.SimEvent.__init__(self, 0, self.current_lane, self.current_customer)
        while self.sim_duration_minutes != 0:
            customer_number += 1
            customer_entry = self.uniTransform(R, self.customer_arrival_rate, N)
            sim_time += customer_entry
            self.current_customer = Customer.Customer.__init__(self, sim_time, customer_number)
            self.current_lane = Customer.Customer.set_lane(self)
            SimEvent.SimEvent.__init__(self, 0, self.current_lane, self.current_customer)
            
            self.sim_duration_minutes -= 1
        pass

    def create_lanes(self):
        for i in range(self.num_checkout_lanes):
            list.append(CheckoutLane.CheckoutLane(i))
    
    def uniTransform(R, lam, N):
        customerDist = round((-np.log(1-R) * lam), N)
        #customerDist = round((-(1/lam)* np.log(1-R)), N)
        return customerDist

    def generateR(self, N):
        R = round(random.uniform(0,1), N)
        return R



