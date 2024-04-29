import requests


def send_email(email):
    email = email.strip()
    url = 'https://digitalstoregames.pythonanywhere.com/manualdeliver'
    data = {
        'productId':921110,
        'email':email
    }

    response = requests.get(url, params=data)
    return response.json()

# Lista de endereços de e-mail
emails = [
   'junior.bnm@hotmail.com'
]


# Iterar sobre cada endereço de e-mail e chamar o serviço REST
for email in emails:
   print(send_email(email))
