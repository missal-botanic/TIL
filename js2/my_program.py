import requests

url = "http://127.0.0.1:8000/articles/json-drf/"
response = requests.get(url) 

print(response)
print(response.json())