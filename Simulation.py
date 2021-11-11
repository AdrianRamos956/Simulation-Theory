"""
Simulation.py
"""
import sys


class Simulation:
    logfile = open('logfile.txt', 'a+')

    def __init__(self):
        rand_seed = sys.argv[1]
        sim_duration_minutes = sys.argv[2]
        num_checkout_lanes = sys.argv[3]
        customer_arrival_rate = sys.argv[4]
        customer_service_rate = sys.argv[5]

    def start(self):
        pass
