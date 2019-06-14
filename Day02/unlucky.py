# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 23:29:16 2019

@author: ANISHKA
"""

# Code Challenge : unlucky 13

lst = []
num = int(input('How many numbers: '))
for n in range(num):
    number=int(input("Enter Number: "))
    lst.append(number)
counter = 0   
for i in num:
    if num==13:
        

    
for num in lst:
    index1=lst.index(13)
    if (index1 + 1 < len(lst)):
        lst.pop()
    else:
        lst.pop(index1 + 1)
        lst.pop(index1)
        print(lst)
        