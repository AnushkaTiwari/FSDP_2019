# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 11:39:27 2019

@author: ANISHKA
"""

# Code Challenge : Duplicates
list2=[]
list1=[12,24,35,24,88,120,155,88,120,155]
for num in list1:
    if num not in list2:
        list2.append(num)
print(list2)
        
