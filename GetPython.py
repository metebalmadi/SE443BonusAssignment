

import json
import requests



url = "https://reqres.in/api/users/2"
headers = {'Content-Type': 'application/json'}

response = requests.get(url, headers=headers)
myjson = response.json()
personName = myjson['data']['first_name']



if response.status_code == 200 : 
    print("200 response: OK")
    
elif response.status_code == 404 :
    print("404 response: Not Found")
    
elif response.status_code == 400 :
    print("400 response: Bad Request")


print('First name: ',personName,'\n')
