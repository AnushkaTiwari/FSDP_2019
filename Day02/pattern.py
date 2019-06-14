# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 10:49:20 2019

@author: ANISHKA
"""

# Code Challenge : Pattern Builder

num=input("Enter the number")
num=int(num)
for i in  range (0,num):
    for j in range (0,i+1):
        print("*", end= ' ')
    print('\r')                     #adding new line

for i in range (num , 0,- 1):
    for j in range (0,i-1):
        print("*", end= ' ')
    print('\r')
        
        

    