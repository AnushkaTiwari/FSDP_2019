# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 12:36:28 2019

@author: ANISHKA
"""

# Code Challenge Name: Character Frequency

dict={}
newstr=input("Enter the string: ")
for char in newstr:
    num=newstr.count(char)
    dict[char]=num
print(dict)
    