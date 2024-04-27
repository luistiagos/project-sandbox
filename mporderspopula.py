from mysql.connector import pooling
import logging, requests
from datetime import datetime
import re

logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.INFO)

config = {
    "user": "digitalstoregame",
    "password": "@Lt057869",
    "host": "digitalstoregames.mysql.pythonanywhere-services.com",
    "database": "digitalstoregame$digitalstoregames",
    "autocommit": True
}

# Create a connection pool with a maximum of 5 connections
pool = None

try:
    pool = pooling.MySQLConnectionPool(pool_name="my_pool", pool_size=4, connection_timeout=30, **config)
except Exception as e:
    print(e)

def add_merchant_order(productid, email, phone, datetime, title, order_status, is_cancelled):
    if pool:
        connection = pool.get_connection()
        cursor = None
        try:
            cursor = connection.cursor()
            insert_query = "INSERT INTO merchant_orders(email, phone, datetime, title, order_status, is_cancelled) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            order_data = (productid, email, phone, datetime, title, order_status, is_cancelled)
            cursor.execute(insert_query, order_data)
            connection.commit()  # Não se esqueça de cometer a transação
        except Exception as e:
            # Ocorreu uma exceção, e a mensagem de erro está armazenada na variável 'e'
            logger.error('Erro: ' + str(e), exc_info=True)
            return False
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()  # Feche a conexão
                logger.info('Conexão fechada.')
        return True
    return False

def format_datetime(current_datetime):
    formatted_datetime = current_datetime.strftime('%Y-%m-%dT%H:%M:%S.%f')
    return formatted_datetime

def extract_phone_formatted(notification_url):
    phone_match = re.search(r'fone=([^&]+)', notification_url)
    phone = phone_match.group(1) if phone_match else ''
    if phone != None and '-' in phone:
        phone = phone.replace('-', '')
    return phone

def get_merchant_orders(datetime_init, datetime_end, offset=0):

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
        notification_url = item['notification_url']
        if notification_url != None:
            notification_url = notification_url.replace('(', '').replace(')', '').replace(' ', '')
            if 'productId' in notification_url and 'email' in notification_url and 'fone' in notification_url:
                order = {}
                try:
                    order['productId'] = re.search(r'productId=(\d+)', notification_url).group(1)
                    order['email'] = re.search(r'email=([^&]+)', notification_url).group(1)
                    order['phone'] = extract_phone_formatted(notification_url)
                    order['datetime'] = item['last_updated']
                    order['title'] = item['items'][0]['title']
                    order['order_status'] = item['order_status']
                    order['is_cancelled'] = item['cancelled']
                    insert = add_merchant_order(order['productId'].strip(), order['email'].strip(), order['phone'], order['datetime'], order['title'], order['order_status'], order['is_cancelled'])
                    print(insert)
                except:
                    pass

    get_merchant_orders(datetime_init, datetime_end, next_offset)

datetime_base = datetime.now()
dt = format_datetime(datetime_base.replace(hour=0, minute=0, second=0, microsecond=0))
datetime_init =  format_datetime(datetime_base.replace(day=1, month=1, year=2023, hour=0, minute=0, second=0, microsecond=0)) + '-04:00'
datetime_end  =  format_datetime(datetime_base.replace(day=31,month=8, year=2023, hour=23, minute=59, second=59, microsecond=999999)) + '-04:00'

get_merchant_orders(datetime_init, datetime_end)
print('Complet!')
