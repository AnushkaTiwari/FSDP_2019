# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 12:30:18 2019

@author: ANISHKA
"""

# Code challenge : replacing of character  
string = input("Enter the string>")         # enter string RESTART
string2= string[1:7]                        # slicing restart 
string3= string2.replace('R' , '$')         # repalcing R with $
print ('R' + string3)