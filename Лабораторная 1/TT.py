import json, requests

post_id = 1
url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

post_data_new = {
    "title": "Обновлённый пост",
    "body": "Тестовое тело",
    "id": post_id
}

response = requests.put(url, json=post_data_new)
post = response.json()

print(json.dumps(post, ensure_ascii=False, indent=4))
