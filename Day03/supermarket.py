# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 10:39:23 2019

@author: ANISHKA
"""

# Code Challenge : Supermarket


from collections import OrderedDict
od=OrderedDict()

num = int(input("Enter the no of total items: "))

for item in range(num):
    item_name,price=input().rsplit( ' ' , 1)
    if item_name not in od:
        od[item_name]=int(price)
    else:
        od[item_name]+=int(price)
        
        
for item_name,price in od.items():
    print( item_name + " " + str(price))
                
    



    
    