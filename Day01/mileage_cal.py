# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 11:15:33 2019

@author: ANISHKA
"""

# Code Challenge : Gas Mileage Calculator
# Assume a car travels 100km after putting 5l of fuel
car_dist = input ("Enter distance travel by car> ")
fuel =  input ("Enter fuel used by car> ")
# typecasting :
car_dist = int(car_dist)
fuel= int (fuel)
# Average mileage of car 
car_avg = car_dist / fuel
print (car_avg)
