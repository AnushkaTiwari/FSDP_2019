#  Code Challenge : use Post Method

import json
import requests

Host="https://en4hny6p7w1t8.x.pipedream.net/"
data= {"FirstName" : "Anushka" , "LastName" : "Tiwari"}
headers= {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}

def post_method():
    response=requests.post(Host,data,headers)
    return response

print( post_method().text)