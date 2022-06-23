import requests
import json
data = {'user' : 'me@example.com'}
resq = requests.post('http://127.0.0.1:5000/', data=json.dumps(data))
print(resq)