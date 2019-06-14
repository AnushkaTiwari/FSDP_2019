# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 21:59:07 2019

@author: ANISHKA
"""

# Code challenge : bricks
lst=[]
for n in range(3):
    number=int(input("Enter number of small brick , large brick and target respectively: "))
    lst.append(number)
no_ofsmall_brick=lst[0]
no_oflarge_brick=lst[1]
target_inch=lst[2]
total_inch= no_ofsmall_brick * 1 + no_oflarge_brick * 5
if (total_inch>=target_inch):
    print("True")
else:
    print("False")