import requests


def send_email(email):
    email = email.strip()
    url = 'https://digitalstoregames.pythonanywhere.com/manualdeliver'
    data = {
        'productId':21111,
        'email':email
    }

    response = requests.get(url, params=data)
    return response.json()

# Lista de endereços de e-mail
emails = [
   'r.joselucio@yahoo.com'
]


# Iterar sobre cada endereço de e-mail e chamar o serviço REST
for email in emails:
   print(send_email(email))
