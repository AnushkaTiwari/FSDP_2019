# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 23:19:46 2019

@author: ANISHKA
"""

# Code Challenge : Translate


def translate(string):
    consonants = 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ'
    list = []
    
    for element in string:
        if element in consonants:
            list.append(element + "o" + element)
            
            
        else:
            list.append(element)
    print(list)
            
        
string = input("Enter string to Translate: ")

print (translate(string))
