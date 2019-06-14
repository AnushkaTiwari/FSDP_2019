# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 11:29:07 2019

@author: ANISHKA
"""



# Code Challenge : Lastline 

file_name=input("Enter the file name:")

with open( file_name + ".txt" ,'wt') as file:
    file.write("This is the first line\n")
    file.writelines(["Second line\n","Third line\n"])
    file.write("This is the final line\n")
    
with open(file_name +".txt",'rt') as file:
    line=file.readlines()
    str1=line[len(line) - 1]
    print(str1)
    