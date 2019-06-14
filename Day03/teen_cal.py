# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 12:21:57 2019

@author: ANISHKA
"""

# Code Challenge : Teen Calculator
sum1=0
Dict={}
for num in range(3):
    user=input("Enter the user name: ")
    values=int(input("Enter the integer values: "))
    Dict[user]=values
    print(Dict)
    if (values>=13 and values<20  and values!=15 and values!=16):
        values=0
    sum1=sum1+values
print( "Sum : "  + str(sum1))