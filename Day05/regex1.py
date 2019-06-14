# Code Challenge : Regular Expression 1


import re

lst=[]
#taking input from user
str1=input("Enter the string:")
lst=str1.split(" ")

#checking whether given no. is valid or not i.e it is a floating point number
for val in lst:
    if re.findall(r'[+-.]?\d?\.\d',val):
        print("True")
    else:
        print("False")