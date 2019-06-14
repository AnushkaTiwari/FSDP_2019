# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 11:37:06 2019

@author: ANISHKA
"""

# Code Challenge : Intersection

s1=[1,3,6,78,35,55]
s2=[12,24,35,24,88,120,155]

set1=set(s1)
set2=set(s2)

set3=set1.intersection(set2)
intersected_list=list(set3)
print(intersected_list)
