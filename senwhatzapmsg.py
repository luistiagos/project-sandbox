import requests
import json

url = 'https://digitalstoregames-be2ff763dd43.herokuapp.com/client/sendMessage/luistiagos'
headers = {
    'accept': '*/*',
    'x-api-key': 'luistiagos',
    'Content-Type': 'application/json'
}
data = {
    "chatId": "554185311304@c.us",
    "contentType": "string",
    "content": "Ola"
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.status_code)
print(response.json())