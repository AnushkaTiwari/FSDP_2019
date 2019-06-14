# Code Challenge : Regular Expression 2

#importing re module
import re

print("Enter the email addresses(max 3)")
lst=[]
lst1=[]

for i in range(3):
    str1=input("Email:")                    # taking input from user
    lst.append(str1)

for val in lst:  
    if re.match(r'[a-zA-Z0-9_-]+\@+[0-9a-zA-Z]+\.+[a-z]{2,4}$',val):            # using regular expression
        lst1.append(val)
        
sorted(lst1)                        #sorting list in alphabetical order

