# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 10:28:56 2019

@author: ANISHKA
"""

# Code Challenge : Romeo and Juliet

lst=[]

Dict={}
with open("romeo.txt",'rt') as file:
    lst=file.readlines()
print(lst)
lst2=[]

for i in range(4):
    lst1=lst[i].split()
    for z in lst1:
        lst2.append(z)


print(lst2)
count=1
for char in lst2:
    if char not in Dict:
        Dict[char]=int(count)
        
    else:
        Dict[char]+=int(count)
        
for char,num in Dict.items():
    print(char + " " + str(num))
        
    
        
    
    
