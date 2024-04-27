import requests
import time

url = "https://graph.facebook.com/v17.0/2120259218170665/events"
access_token = "EABcVzD6vs5sBAENkMQePw1YVrerAWB3hGnF8GIwSmfrEU5WbS2qmL7AKZCBqVeZCQk2Yv9Xq1pDt1jB5u9HmH4j1ypjVy3PZCWmf0lcOdlZAfBsmhRJsvlEAZBEgqSnLHGnLpB1U0q0IZAbS5KbvbikZBWSZAKyYOAzgbS2t4GUMgkva7aHqZCjQeUZAmBdaLY6wGWKDF9c2MEOiYcni9kunvGOcE7IqZC8ml4ZD"

# Dados para enviar na solicitação POST
data = {
    "data": [
        {
            "action_source": "website",
            "event_id": 12345,
            "event_name": "TestEvent",
            "event_time": int(time.time()),  # Timestamp atual em segundos
            "user_data": {
                "client_user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Mobile/15E148 Safari/604.1",
                "em": "f660ab912ec121d1b1e928a0bb4bc61b15f5ad44d5efdc4e1c92a25e99b8e44a"
            }
        }
    ],
    "test_event_code": "TEST93508"
}

# Fazendo a solicitação POST
response = requests.post(url, params={"__cppo": "1", "access_token": access_token}, json=data)

# Obtendo o conteúdo da resposta
content = response.json()

# Exibindo a resposta
print(content)
