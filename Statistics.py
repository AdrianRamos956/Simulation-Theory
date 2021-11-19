"""
Statistics.py
"""

class Statistics:

    def __init__(self):
      self.avg_customers = float(0)
      self.avg_customer_systime = float(0)
      self.avg_customer_wait = float(0)
      self.avg_customers_waiting = float(0)
      self.p_no_customers = float(0)
      self.cus_coutner = 0
    
    #Total_cus = Take the duration of the simulation in minutes and multiply it by The customer arrival rate in customers per minute to get the total customers

    #Calculates average number of customers in the system
    def set_avg_customers(self,total_time, customer_number):
        self.cus_coutner = customer_number
        self.avg_customers = self.cus_coutner / total_time
        
    #Calculates average time spent in system for customers
    def set_avg_customer_systime(self, sim_time, sim_end_time):
        #print(sim_end_time - sim_time)
        self.avg_customer_systime = (sim_end_time - sim_time) + self.avg_customer_systime
        
    #Calculates average waiting time before being serviced for customers for a particular lane
    def set_avg_customer_wait(self, sim_time, sim_waiting_time):
        self.avg_customer_wait = (sim_waiting_time - sim_time) + self.avg_customer_wait
        print(self.avg_customer_wait)
        
    #Calculates average waiting time for customers in system
    def set_avg_customers_waiting(self, sim_time, time_till_front_of_line):
        pass
        
    #Calculates probability that no customers were in the system at any particular time
    def set_p_no_customers(self, Arrival_Rate, Service_Rate):
        p = int(Service_Rate) / int(Arrival_Rate)
        self.p_no_customers = ( 1 - p ) * 1
        #print(self.p_no_customers)
    

    #Writes all the statistics of the system to a file
    def write_stats(self):
       with open("statistics.txt", "a") as s:
         percentage = "{:.2%}".format(self.p_no_customers)
         avg_time_per = self.avg_customer_systime / self.cus_coutner
         avg_time_wait = self.avg_customer_wait / self.cus_coutner
         s.write("The average number of customers in the system at any particular time is %.2f \n" % (self.avg_customers))
         s.write("The average time each customer spent in the system is %.2f \n" % (avg_time_per))
         s.write("The average time each customer waited before being served is %.2f \n" % (avg_time_wait))
         #s.write("The average number of customers waiting to be served in all check-out lanes at any particular time %2f \n" % (self.avg_customers_waiting))
         s.write("The probability that no customers were in the system at any particular moment is %s \n" % (percentage))
         
