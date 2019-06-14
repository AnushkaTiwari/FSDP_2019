# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:25:16 2019

@author: ANISHKA
"""

# Code Challenge : Pangram
def pangram_check():
    string=input("Enter the string : ")
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if (char  not in string.lower()):
            return " Not Pangram"
        
    return "pangram"
        
        
print(pangram_check())
 




    