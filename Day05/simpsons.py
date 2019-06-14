import re
lst1=[]
# reading a file
with open("simpsons_phone_book.txt",'rt') as file:
    lst=file.readlines() 
for item in lst:
    if re.search(r'[J][a-z]+\s+Neu',item):          # using regular expression
        item=item.replace('\n','')
        lst1.append(item)

print(lst1)
    