import requests
import json


url = "https://reqres.in/api/login"
login_info = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}
response = requests.post(url, json = login_info)

myjson = response.json()



if response.status_code == 201 : 
    print("201 response: Created success")
    print('Token: ', myjson['token'])
    
elif response.status_code == 200 :
    print("200 response: OK success")
    print('Token: ', myjson['token'])
    
elif response.status_code == 400 :
    print("400: Bad Request")




