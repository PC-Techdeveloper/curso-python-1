# Como hacer peticiones APIS con Python
# con y sin dependencias

# 1. Sin dependencias (dificil y sin dependencias)
import urllib.request
import json

DEEPSEEK_API_KEY = "xxx"

api_post = "https://jsonplaceholder.typicode.com/posts"

try:
    response = urllib.request.urlopen(api_post)
    data = response.read()
    json_data = json.loads(data.decode("utf-8"))
    print(json_data)
    response.close()
except urllib.error.URLError as err:
    print(f"Error en la solicitud: {err}")

# 2. Con dependencias (request)

import requests

print("\nGET:")
api_post = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(api_post)
reponse_json = response.json()  # Convert to JSON

# 3. Un POST
print("\nPOST:")
try:
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json={"title": "foo", "body": "hola", "userId": 1},
    )
    print(response.status_code)
except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud: {e}")

# 4. Un PUT
print("\nPUT:")
try:
    response = requests.put(
        "https://jsonplaceholder.typicode.com/posts/1",
        json={
            "title": "foo",
            "body": "bar",
            "userId": 1,
        },
    )

    print(response.status_code)
except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud: {e}")

# Usar la API de GPT-4o de OpenAI
# Ref: https://platform.openai.com/docs/api-reference/making-requests

OPENAI_KEY = "sk-XXXXXXXX"

import json


def call_openai_gpt(api_key, prompt):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
    data = {"model": "gpt-4o-mini", "messages": [{"role": "user", "content": prompt}]}

    response = requests.post(url, json=data, headers=headers)
    return response.json()


api_response = call_openai_gpt(
    OPENAI_KEY, "Escribe un breve poema sobre la programación"
)

# print(json.dumps(api_response, indent=2))

print(api_response["choices"][0]["message"]["content"])

# Llamar a la API de DEEPSEEK

import json


def call_deepseek(api_key, prompt):
    url = "https://api.deepseek.com/chat/completions"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
    data = {"model": "deepseek-chat", "messages": [{"role": "user", "content": prompt}]}

    response = requests.post(url, json=data, headers=headers)
    print(response.json())
    return response.json()


api_response = call_deepseek(
    DEEPSEEK_API_KEY, "Escribe un breve poema sobre la programación"
)

# print(json.dumps(api_response, indent=2))

print(api_response["choices"][0]["message"]["content"])
