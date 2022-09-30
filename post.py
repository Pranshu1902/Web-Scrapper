import json
from lib2to3.pgen2 import token
import requests

URL = "https://money-manager-pranshu1902.herokuapp.com/api-token-auth/"
getURL = "https://money-manager-pranshu1902.herokuapp.com/transactions/"

headersData = {
"accept": "application/json",
"Content-Type": "application/json"
}

params = {
"username": "user",
"password": "corona1902"
}

resp = requests.post(URL, headers = headersData ,data=json.dumps(params))
tk = json.loads(resp.text)['token']

print(tk)

auth = {
"Authorization": str(tk),
"Content-Type": "application/json"
}

data = json.dumps({"amount": 100, "description": "data added from terminal"})
author = json.dumps({"username": "user", "password": "corona1902"})

response = requests.post(getURL, headers=auth, data=data, auth=("user", "corona1902"))
print(response.text)
