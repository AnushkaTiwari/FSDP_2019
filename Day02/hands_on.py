# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 10:28:29 2019

@author: ANISHKA
"""

"""
Hands On 1
"""
# Create a list of number from 1 to 20 using range function. 
# Using the slicing concept print all the even and odd numbers from the list 

my_list = list(range(1,20))
print(my_list)
print(my_list[1:20:2])          # printing even no
print(my_list[0:20:2])          #printing odd no



"""
Hands On 2
"""
# Make a function to find whether a year is a leap year or no, return True or False


def leap_func(year):                            #creating a function
    if (year % 4==0):                           # condition to check whether the year is a leap year or not
        return True
    else:
        return False
    
print(leap_func(year=2019))                     # printing of calling function




"""
Hands On 3
"""
# Make a function days_in_month to return the number of days in a specific month of a year



def days_in_month(month):
    if(month=="january")
    