"""
Simulation.py
"""
import sys
import random
import CheckoutLane
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

    def start(self):
        """
        begin the simulation
        :return: none
        """
        #TODO SETUP
        self.create_lanes(self)
        seed = str(self.rand_seed)
        N = len(seed)
        R = self.generateR(self, N)
        self.uniTransform(R, self.customer_arrival_rate, N)
        pass

    def create_lanes(self):
        for i in range(self.num_checkout_lanes):
            list.append(CheckoutLane.CheckoutLane(i))
    
    def uniTransform(R, lam, N):
        customerDist = round((-(1/lam)* np.log(1-R)), N)
        return customerDist

    def generateR(self, N):
        R = round(random.uniform(0,1), N)



