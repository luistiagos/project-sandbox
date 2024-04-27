import requests
import csv

access_token = "APP_USR-7436035612141486-013122-61798ea13f696f8c593ad4e8a37d28f8-1250513859"

url = 'https://api.mercadopago.com/v1/customers/search'
headers = {
    'Content-Type': 'application/json',
    'Authorization': access_token
}
params = {
    'email': 'luistiago.andrighetto@gmail.com'
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Erro ao fazer a requisição:', response.status_code)
