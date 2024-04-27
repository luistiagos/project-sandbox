import requests
import csv

access_token = "APP_USR-7436035612141486-013122-61798ea13f696f8c593ad4e8a37d28f8-1250513859"
url = "https://api.mercadopago.com/checkout/preferences"

def generate_mp_link(id, title, description, success_url, price): 
    data = {
        "items": [
            {
                "title": title,
                "description": description,
                "quantity": 1,
                "currency_id": "BRL",
                "unit_price": float(price)
            }
        ],
        "notification_url": "http://digitalstoregames.pythonanywhere.com/notification?productId=" + str(id),
        "back_urls": {
            "success":  success_url
            #"pending": "https://seusite.com.br/pending",
            #"failure": "https://seusite.com.br/failure"
        }
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        init_point = response.json()["init_point"]
        #print(f"Link de pagamento gerado com sucesso: {init_point}")
        return init_point
        
    return None


with open('produtoidmp2.csv', mode='r', encoding='utf-8') as csv_file_r:
    with open('fileprodutoidmp3_out.csv', mode='w', encoding='utf-8-sig', newline='') as csv_file_w:
        csv_reader = csv.reader(csv_file_r, delimiter=';')
        csv_writer = csv.writer(csv_file_w, delimiter=';')
        for row in csv_reader:
            if len(row) > 0:
                link = generate_mp_link(row[0], row[1], row[1], row[2], row[3])
                row.append(link)
                csv_writer.writerow(row)