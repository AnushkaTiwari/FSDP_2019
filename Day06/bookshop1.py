#Code Challenge : Book Shop


for i in range(1):
    s=input("Enter the book order no,title,author name,Quantity , price seprated by comma : ")
    s=s.split(",")
    lst.append(s)

for item in lst:
    item=item[-1]
    print( "price :" + str(item))
    
    
    
