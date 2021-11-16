"""
Simulation.py
"""
import sys
import random
from typing_extensions import Self
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
        #Time used for checking when customers are added to system and when they need to be removed 
        sim_time = 0.0
        self.create_lanes(self)
        seed = str(self.rand_seed)
        customer_number = 1
        #Length of seed for random number generation
        N = len(seed)
        #Random number used for uniform transformation
        R = self.generateR(N)
        #Service time of customer
        time_service = self.uniTransform(self.customer_service_rate, N)
        #Current customer to add to queue
        self.current_customer = Customer.Customer.__init__(self, 0.0, time_service,customer_number)
        #Current lane for adding customers to
        self.current_lane = CheckoutLane.CheckoutLane.__init__(self, 1)
        #Add initial customer to Queue at time 0.0
        SimEvent.SimEvent.__init__(self, 0, self.current_lane, self.current_customer)
        Customer.Customer.log_in(self)
        #Run simulation for specified duration 
        while self.sim_duration_minutes != 0:
            #Add customers to lane in one-time step per the customer arrival rate
            for i in range(self.customer_arrival_rate):  
                #Create a customer and add them to a lane  
                customer_number += 1
                R = self.generateR(N)
                #Perform uniform transformation for customer and add it to current sim_time to accurately detail when it's added to the system
                sim_time += self.uniTransform(R, self.customer_arrival_rate, N)
                time_service = self.uniTransform(self.customer_service_rate, N)
                self.current_customer = Customer.Customer.__init__(self, sim_time, time_service,customer_number)
                self.current_lane = Customer.Customer.set_lane(self)
                SimEvent.SimEvent.__init__(self, 0, self.current_lane, self.current_customer)
                Customer.Customer.log_in(self)
                #Check if a customer is ready to be checked out
                if self.current_customer < sim_time:
                    SimEvent.SimEvent.__init__(self, 1, self.current_lane, self.current_customer)
                    Customer.Customer.log_out(self, sim_time)
            self.sim_duration_minutes -= 1
        pass

    def create_lanes(self):
        for i in range(self.num_checkout_lanes):
            list.append(CheckoutLane.CheckoutLane(i))
    #Uniform transformation function for interarrival times
    def uniTransform(R, lam, N):
        customerDist = round((-np.log(1-R) * lam), N)
        #customerDist = round((-(1/lam)* np.log(1-R)), N)
        return customerDist
    #Random number generator 
    def generateR(N):
        R = round(random.uniform(0,1), N)
        return R



