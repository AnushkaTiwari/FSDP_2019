import json
import requests

Host="http://13.127.155.43/api_v0.1/sending"
data= {"Phone_Number" : "51415645" , "Name" : "Anushka", "College_Name" : "PCE","Branch" : "Cs"}
headers= {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}

def post_method():
    response=requests.post(Host,data,headers)
    return response

print( post_method().text)

def get_method():
    response = requests.get("http://13.127.155.43/api_v0.1/recieving/get?q=PhoneNumber")
    return response

print (get_method().text)
