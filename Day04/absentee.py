# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 10:00:03 2019

@author: ANISHKA
"""

# Code Challenge : Create a list of absentee

n=0

with open("absentee.txt",'wt') as file:
    while (n<25):
        name=input("Enter the name of absentee: ")
        file.write(name+'\n')
        
        if not name:
            break
        
with open("absentee.txt",'rt') as absentee:
    file_content=absentee.readlines()
    print(file_content)
        
        