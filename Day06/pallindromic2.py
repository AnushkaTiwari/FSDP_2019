# Code Challenge : Pallindromic Integer

    
  
s=input("Enter the integers separated by space:")
s=s.split(" ")
print(any([str(n)==str(n[::-1]) and int(n)>=0 for n in s]))

