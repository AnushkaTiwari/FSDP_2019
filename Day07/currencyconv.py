# Code Challenge : Currency Converter Convert  from USD to INR

import requests


Dollar=int(input("Enter the amount of dollar:"))

url="https://free.currconv.com/api/v7/convert?q=USD_PHP&compact=ultra&apiKey=3cf4a0d43b2f98241754"

response=requests.get(url)
response.content
jsondata=response.json()
value=jsondata["USD_PHP"]
INR=value * Dollar
print("Amount in INR :" + str(INR))