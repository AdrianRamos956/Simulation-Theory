"""
Checkout Simulation

"""
import sys
import Customer
import CheckoutLane
import Statistics

"""
seed
duration
lanes
customer arrival time
customer service rate

ex. sim1 789 1000 5 4 3
"""


def main():
    read_args()
    Simulation.start()


class Simulation:
    logfile = open('logfile.txt', 'a+')
    rand_seed = sys.argv[1]
    sim_duration_minutes = sys.argv[2]
    num_checkoutlanes = sys.argv[3]
    customer_arrival_rate = sys.argv[4]
    customer_service_rate = sys.argv[5]



    def start(self):
        self.read_args(self)


def read_args(self):
    if len(sys.argv) < 6:
        print("Usage: sim1.py [seed] [duration] [lanes] [customer arrival time] [customer service rate]\n"
              "Ex. sim1 789 1000 5 4 3")



if __name__ == '__main__':
    main()
