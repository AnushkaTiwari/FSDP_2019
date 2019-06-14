# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 22:29:29 2019

@author: ANISHKA
"""

# Code Challenge : operation function
def Print():
    
    
    print(Sum(lst))
    print(Multiply(lst))
    print(Smallest(lst))
    print(largest(lst))
    print(Sort(lst))
    
    

list=[]
for n in range(5):
    number=int(input("Enter the values: "))
    list1=list.append(number)

print(list1)
    
print(Print(lst))
    


def Sum(lst):
    Sum =sum(lst)
    return Sum

def Multiply(lst):
    for n in lst:
        Multiply = Multiply * n
    return Multiply

def Smallest(lst):
    Smallest=min(lst)
    return Smallest

def largest(lst):
    largets=max(lst)
    return largest


def Sort(lst):
    Sort=lst.sort(lst)
    return Sort


