import requests
import json

def get_payment(id):
    id = '59106721282'

    url = 'https://api.mercadopago.com/v1/payments/' + str(id)
    access_token = 'APP_USR-7436035612141486-013122-61798ea13f696f8c593ad4e8a37d28f8-1250513859'

    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.get(url, headers=headers)

    with open('resposta.json', 'w') as arquivo_json:
        json.dump(response.json(), arquivo_json)

def get_customer(id):
    url = 'https://api.mercadopago.com/v1/customers/' + str(id)
    access_token = 'APP_USR-7436035612141486-013122-61798ea13f696f8c593ad4e8a37d28f8-1250513859'

    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.get(url, headers=headers)

    with open('resposta2.json', 'w') as arquivo_json:
        json.dump(response.json(), arquivo_json)

def list_customers():
    url = 'https://api.mercadopago.com/v1/payments/search'
    access_token = 'APP_USR-7436035612141486-013122-61798ea13f696f8c593ad4e8a37d28f8-1250513859'

    params = {
        'sort': 'date_created',
        'criteria': 'desc',
        'external_reference': 'ID_REF',
        'range': 'date_created',
        'begin_date': 'NOW-30DAYS',
        'end_date': 'NOW'
    }

    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.get(url, params=params, headers=headers)

    print(response.json())
    
    
list_customers()