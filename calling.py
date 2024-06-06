import requests

response=requests.post(
    "http://localhost:8000/India/invoke",
    json={'input':{'topic':"Insurance"}})

print(response.json()['output']['content'])