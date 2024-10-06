import json, requests

new_post = {"userId": 1,
            "title" : "Тестовый пост",
            "body" : "Тестовое тело"}

json_response = requests.post('https://jsonplaceholder.typicode.com/posts', json = new_post)
if json_response.ok:
    data = json_response.json()
    print(json.dumps(data, ensure_ascii = False, indent=3))
else:
    print(json_response.status_code)
