import requests, json

R = requests.get('https://jsonplaceholder.typicode.com/posts/')
data = R.json()
m = [i for i in data if i['userId'] % 2 == 0]
print(json.dumps(m, indent=4))
