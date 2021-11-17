"""
Statistics.py
"""


class Statistics:
    avg_customers = float()
    avg_customer_systime = float()
    avg_customer_wait = float()
    avg_customers_waiting = float()
    p_no_customers = float()

    # Calculates average number of customers in the system
    def set_avg_customers(self):
        pass

    # Calculates average time spent in system for customers
    def set_avg_customer_systime(self):
        pass

    # Calculates average waiting time before being serviced for customers for a particular lane
    def set_avg_customer_wait(self):
        pass

    # Calculates average waiting time for customers in system
    def set_avg_customers_waiting(self):
        pass

    # Calculates probability that no customers where in the system at any particular time
    def set_p_no_customers(self):
        pass

    # Writes all the statistics of the system to a file
    def write_stats(self):
        """
        Write the statics to a file
        :return:
        """
