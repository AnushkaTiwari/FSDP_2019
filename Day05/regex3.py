# Code Challenge: Regular Expression 3

import re

num=int(input("Enter the no of credits you want to enter:"))

lst=[]
lst1=[]
# It must NOT have 4 or more consecutive repeated digits 
def leng(val):                                                      #(\d)\1{3,}
    for i,n in enumerate(val):
        try:
            if (val[i],val[i+1],val[i+2],val[i+3]) == (n,n,n,n):
                return False
        except IndexError:
                pass
for i in range(num):
    str1=input("Enter the credit numbers: ")            # taking input from user
    lst.append(str1)
    
for val in lst:
    # using regular expession to check whether given credit no is valid or not
    if re.findall(r'^([456]\d{3})\-?(\d{4})\-?(\d{4})\-?(\d{4})$',val):         
        if leng(val)==True:
            print("Valid")
        else:
            print("Not Valid")
