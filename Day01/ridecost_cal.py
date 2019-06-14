# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 11:23:36 2019

@author: ANISHKA
"""

#Code Challenge : Ride Cost Calculator
# Assume you travel 80km to and fro in a day
my_dist = 80
# cost of diesel per litre is 80INR
cost_of_diesel = 80
#vehicle fuel avg is 18km/litre
my_avg = 18
my_avg1 = 1 / 18        # average for 1 km 
fuel_used= 80 * my_avg1  # fuel used for 80 km
# total cost of driving 
total_cost = fuel_used * 80 
print (total_cost)
