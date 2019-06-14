# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 12:36:22 2019

@author: ANISHKA
"""

# Code Challenge : Word Count

file_name=input("Enter the file name:")

lst2=[]
lst3=[]
final_list=[]

with open( file_name + ".txt" ,'wt') as file:
    file.write("This is the first line\n")
    file.writelines(["Second line\n","Third line\n"])
    
    
with open(file_name + ".txt" ,'rt') as file:
        lst=file.readlines()
        no_of_lines=len(lst)
        for line in lst:
            for word in line:
                lst2.append(word)
            print(lst2)
            no_of_char=len(lst2)
        for i in range(no_of_lines):
            lst1=lst[i].split()
            for z in lst1:
                lst3.append(z)
        count=0
        print(lst3)
        no_of_words=len(lst3)
        for char in lst3:
            num=lst3.count(char)
            print(char,num)
        for char in lst3:
            if (num==1):
                count+=1
        print(count)
        