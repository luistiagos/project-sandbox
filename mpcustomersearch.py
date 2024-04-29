import requests
import re
import pytz
from urllib.parse import quote_plus
from datetime import datetime, timedelta

def add_sent(productid,email,phone,sent_email,sent_whats,campaing):
    url = 'https://digitalstoregames.pythonanywhere.com/add_sent'
    data = {    
        'productid':productid,    
        'email':email,
        'phone':phone,
        'sent_email':sent_email,
        'sent_whats':sent_whats,
        'campaing': campaing
    }
    response = requests.get(url, params=data)
    return response.text

def send_email(productId, email):
    email = email.strip()
    url = 'https://digitalstoregames.pythonanywhere.com/manualdeliver'
    data = {
        'productId':productId,
        'email':email
    }
    response = requests.get(url, params=data)
    return response.json()

def find_email_not_delivery(productId, email):
    email = email.strip()
    url = 'https://digitalstoregames.pythonanywhere.com/find_email_not_delivery'
    data = {
        'productid':productId,
        'email':email
    }
    response = requests.get(url, params=data)
    return int(response.text)

def find_email_not_deliveryc(productId, email):
    email = email.strip()
    url = 'https://digitalstoregames.pythonanywhere.com/find_email_not_delivery'
    data = {
        'productid':productId,
        'email':email
    }
    response = requests.get(url, params=data)
    return int(response.text)


def format_datetime(current_datetime):
    formatted_datetime = current_datetime.strftime('%Y-%m-%dT%H:%M:%S.%f')
    return formatted_datetime

def extract_phone_formatted(notification_url):
    phone_match = re.search(r'fone=([^&]+)', notification_url)
    phone = phone_match.group(1) if phone_match else ''
    if phone != None and '-' in phone:
        phone = phone.replace('-', '')
    return phone

def get_payment_info(paymentid): 
    url = 'https://api.mercadopago.com/v1/payments/' + str(paymentid)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer APP_USR-7436035612141486-013122-61798ea13f696f8c593ad4e8a37d28f8-1250513859'
    }

    response = requests.get(url, headers=headers)
    return response.json()

#order_status= paid, payment_required, reverted, payment_in_process
def get_merchant_orders(orders, datetime_init, datetime_end, offset=0, canceled=False, order_status='paid'):

    url = 'https://api.mercadopago.com/merchant_orders/search'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer APP_USR-7436035612141486-013122-61798ea13f696f8c593ad4e8a37d28f8-1250513859'
    }

    data = {
        "offset": offset,
        "limit": 50,
        "last_updated_from": datetime_init,
        "last_updated_to": datetime_end
    }

    response = requests.get(url, headers=headers, params=data)
    responseJson = response.json()
    total = responseJson['total']
    next_offset = responseJson['next_offset']
    itens = responseJson['elements']

    if total == 0:
        return
    
    for item in itens:
        if item['cancelled'] == canceled:
            if item['order_status'] == order_status:
                order = {}
                order['datetime'] = item['last_updated']
                order['title'] = item['items'][0]['title']
                order['order_status'] = item['order_status']
                order['is_cancelled'] = item['cancelled']
                order['total_amount'] = item['total_amount']
                
                if order_status == 'paid':
                    total_fees = 0
                    payment_info = get_payment_info(item['payments'][0]['id'])
                    for fee in payment_info['fee_details']:
                        total_fees +=  float(fee['amount'])
                    order['total_fees'] = total_fees
                    order['total'] = order['total_amount'] - order['total_fees']
                
                notification_url = item['notification_url']
                if notification_url != None:
                    notification_url = notification_url.replace('(', '').replace(')', '').replace(' ', '')
                    if 'productId' in notification_url and 'email' in notification_url and 'fone' in notification_url: 
                        order['productId'] = re.search(r'productId=(\d+)', notification_url).group(1)
                        order['email'] = re.search(r'email=([^&]+)', notification_url).group(1)
                        order['phone'] = extract_phone_formatted(notification_url)
                        
                orders.append(order)
                        
                    
    get_merchant_orders(orders, datetime_init, datetime_end, next_offset)                
                    
                
datetime_base = datetime.now()
dt = format_datetime(datetime_base.replace(hour=0, minute=0, second=0, microsecond=0))
datetime_init =  format_datetime(datetime_base.replace(day=28, hour=0, minute=0, second=0, microsecond=0)) + '-03:00' 
datetime_end  =  format_datetime(datetime_base.replace(day=28, hour=23, minute=59, second=59, microsecond=999999)) + '-03:00'
                
orders = []               
get_merchant_orders(orders, datetime_init, datetime_end)

total_plataforma = 0
total_ps2 = 0
total_xbox360 = 0
total_unknow = 0
count_plataforma = 0
count_ps2 = 0
count_xbox360 = 0  
count_unknow = 0
total_geral = 0
count_geral = 0
for order in orders:
    total_geral += order['total']
    count_geral += 1
    if 'Plataforma Multigames' in order['title']:
        total_plataforma += order['total']
        count_plataforma += 1
    elif 'Plataforma PS2' in order['title'] or 'Emulador PS2' in order['title']:
        total_ps2 += order['total']
        count_ps2 += 1
    elif 'Xbox 360' in order['title']:
        total_xbox360 += order['total']
        count_xbox360 += 1
    else:
        total_unknow += order['total']
        count_unknow += 1
    
print(round(total_geral, 2))
print(count_geral)
print(round(total_plataforma, 2))
print(round(total_ps2, 2))
print(round(total_xbox360, 2))
print(round(total_unknow,2))
print(count_plataforma)
print(count_ps2)
print(count_xbox360)
print(count_unknow)


#    if find_email_not_delivery(order['productId'], order['email']) == 0:
#        if order['email'] == 'luistiago.andrighetto@gmail.com':
#            print(order)
#        send_email(order['productId'], order['email'])
#        add_sent(order['productId'], order['email'], order['phone'], True, False, 'notsent')



