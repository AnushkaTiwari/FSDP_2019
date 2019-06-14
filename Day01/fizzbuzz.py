# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 22:12:40 2019

@author: ANISHKA
"""

# Code Challenge : Fizz Buzz
n=1
while (n<=100):
    if (n % 3==0 and n % 5==0                   # checking if no. is multiple of both 3 and 5
        print("FizzBuzz")
    elif (n % 5==0):                            # if no is multiple of 5
        print("Buzz")
    elif (n % 3==0 ):                           #  if no is multiple of 3
        print("Fizz")
    else:
        print(n)
    n=n+1