# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 12:36:30 2019

@author: ANISHKA
"""

# Code Challenge : Centered Average 
""" maximum length of list is 5 """
lst = []
num = int(input('How many numbers: '))
for n in range(num):
    number=int(input("Enter Number: "))
    lst.append(number)
lst.sort()
min1=lst[0]
max1=lst[num - 1]
index1=lst.index(min1)
index2=lst.index(max1)
lst.pop(index2)
lst.pop(index1)
sum=sum(lst)
len=len(lst)
avg=sum / len
print(avg)

   


            
    