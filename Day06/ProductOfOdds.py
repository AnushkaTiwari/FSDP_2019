"""
This Python function accepts a list of numbers and computes the product of all the odd numbers:

def productOfOdds(list):
    result = 1
    for i in list:
        if i % 2 == 1:
            result *= i
    return result
    
Rewrite the Python code using map, filter, and reduce:

def productOfOdds(list):
    return reduce(r_func, filter(f_func, map(m_func, list)))

    
"""

from functools import reduce

s=input("Enter the numbers seprated by space: ")
s=s.split(" ")
def m_func(x):
    return int(x)

def f_func(d):
    return d%2==1

def r_func(y,z):
    y = y * z
    return y

def ProductOfOdds(s):
    return reduce(r_func ,filter(f_func, map(m_func,s)))

print(ProductOfOdds(s))