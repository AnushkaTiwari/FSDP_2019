# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 11:53:05 2019

@author: ANISHKA
"""

# Code Challenge : Digit Letter Count

newstr=input("Enter the string")


alphabet=list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")

number=list("1234567890")

counter1=0
counter2=0

for num in newstr:
    if num in alphabet:
        counter1 =counter1 + 1
    elif num in number:
        counter2 =counter2 + 1
    else:
        pass


Dict={"Digits" : 0 , "Letters" : 0 }
Dict["Digits"]=counter2
Dict["Letters"]=counter1

for Digits,Letters in Dict.items():
    print(Digits,Letters)
        