import requests
import re
import pytz
from urllib.parse import quote_plus
from datetime import datetime, timedelta

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

def get_merchant_order_by_payment(payment_id):
    """
    Busca informações da ordem do Mercado Pago pelo número da transação/pagamento
    """
    try:
        # Primeiro, obtém informações do pagamento
        payment_info = get_payment_info(payment_id)
        
        if 'order' not in payment_info or 'id' not in payment_info['order']:
            print(f"Pagamento {payment_id} não possui ordem associada")
            return None
        
        order_id = payment_info['order']['id']
        
        # Busca a ordem completa
        url = f'https://api.mercadopago.com/merchant_orders/{order_id}'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer APP_USR-7436035612141486-013122-61798ea13f696f8c593ad4e8a37d28f8-1250513859'
        }
        
        response = requests.get(url, headers=headers)
        order_data = response.json()
        
        # Monta o objeto de ordem formatado
        order = {}
        order['payment_id'] = payment_id
        order['order_id'] = order_id
        order['datetime'] = order_data.get('last_updated', '')
        order['date_created'] = order_data.get('date_created', '')
        order['title'] = order_data['items'][0]['title'] if order_data.get('items') else ''
        order['order_status'] = order_data.get('order_status', '')
        order['is_cancelled'] = order_data.get('cancelled', False)
        order['total_amount'] = order_data.get('total_amount', 0)
        
        # Calcula taxas se o pagamento foi aprovado
        if payment_info.get('status') == 'approved':
            total_fees = 0
            for fee in payment_info.get('fee_details', []):
                total_fees += float(fee['amount'])
            order['total_fees'] = total_fees
            order['total'] = order['total_amount'] - order['total_fees']
        else:
            order['total_fees'] = 0
            order['total'] = order['total_amount']
        
        # Extrai informações da notification_url
        notification_url = order_data.get('notification_url', '')
        if notification_url:
            notification_url = notification_url.replace('(', '').replace(')', '').replace(' ', '')
            if 'productId' in notification_url and 'email' in notification_url and 'fone' in notification_url: 
                order['productId'] = re.search(r'productId=(\d+)', notification_url).group(1)
                order['email'] = re.search(r'email=([^&]+)', notification_url).group(1)
                order['phone'] = extract_phone_formatted(notification_url)
        
        # Informações adicionais do pagamento
        order['payment_status'] = payment_info.get('status', '')
        order['payment_type'] = payment_info.get('payment_type_id', '')
        order['payment_method'] = payment_info.get('payment_method_id', '')
        
        # Informações do comprador
        if 'payer' in payment_info:
            payer = payment_info['payer']
            order['payer_email'] = payer.get('email', '')
            order['payer_name'] = payer.get('first_name', '') + ' ' + payer.get('last_name', '')
            order['payer_identification'] = payer.get('identification', {}).get('number', '')
        
        return order
        
    except Exception as e:
        print(f"Erro ao buscar transação {payment_id}: {str(e)}")
        return None

def format_order_display(order):
    """
    Formata a ordem para exibição
    """
    if not order:
        return "Nenhuma informação encontrada"
    
    display = "\n" + "="*60 + "\n"
    display += "INFORMAÇÕES DA VENDA\n"
    display += "="*60 + "\n\n"
    
    display += f"ID do Pagamento: {order.get('payment_id', 'N/A')}\n"
    display += f"ID da Ordem: {order.get('order_id', 'N/A')}\n"
    display += f"Data de Criação: {order.get('date_created', 'N/A')}\n"
    display += f"Última Atualização: {order.get('datetime', 'N/A')}\n\n"
    
    display += f"Produto: {order.get('title', 'N/A')}\n"
    display += f"Status da Ordem: {order.get('order_status', 'N/A')}\n"
    display += f"Status do Pagamento: {order.get('payment_status', 'N/A')}\n"
    display += f"Cancelado: {'Sim' if order.get('is_cancelled') else 'Não'}\n\n"
    
    display += f"Valor Total: R$ {order.get('total_amount', 0):.2f}\n"
    display += f"Taxas: R$ {order.get('total_fees', 0):.2f}\n"
    display += f"Valor Líquido: R$ {order.get('total', 0):.2f}\n\n"
    
    display += f"Método de Pagamento: {order.get('payment_method', 'N/A')}\n"
    display += f"Tipo de Pagamento: {order.get('payment_type', 'N/A')}\n\n"
    
    display += "INFORMAÇÕES DO COMPRADOR:\n"
    display += f"Nome: {order.get('payer_name', 'N/A')}\n"
    display += f"Email: {order.get('payer_email', 'N/A')}\n"
    display += f"CPF/CNPJ: {order.get('payer_identification', 'N/A')}\n\n"
    
    if 'email' in order:
        display += "INFORMAÇÕES DE ENTREGA:\n"
        display += f"Product ID: {order.get('productId', 'N/A')}\n"
        display += f"Email de Entrega: {order.get('email', 'N/A')}\n"
        display += f"Telefone: {order.get('phone', 'N/A')}\n\n"
    
    display += "="*60 + "\n"
    
    return display

# EXEMPLO DE USO
if __name__ == "__main__":
    # Número da transação a ser buscada
    transaction_number = "141604444034"
    
    print(f"Buscando informações da transação: {transaction_number}...")
    order = get_merchant_order_by_payment(transaction_number)
    
    if order:
        print(format_order_display(order))
    else:
        print(f"Não foi possível encontrar a transação {transaction_number}")
