import json
from lib2to3.pgen2 import token
import requests

URL = "http://money-manager-pranshu1902.herokuapp.com/api-token-auth/"
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
