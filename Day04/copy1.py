# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 09:53:32 2019

@author: ANISHKA
"""

# Code Challenge : Copy Command

with open("new.txt",'rt') as file:              #opening new.txt in read mode
    with open("new1.txt",'wt') as file1:
        for line in file:
            file1.write(line)