import mercadopago

# Your Mercado Pago credentials
ACCESS_TOKEN = 'APP_USR-7436035612141486-013122-61798ea13f696f8c593ad4e8a37d28f8-1250513859'

# The ID of the payment to verify
payment_id = '59106721282'

# Create a Mercado Pago API instance
mp = mercadopago.SDK(ACCESS_TOKEN)

# Get the payment information
payment_info = mp.payment().get(payment_id)

if payment_info['status'] == 200:
    payment_info = payment_info['response']
    # Check if the payment was approved
    if payment_info['status'] == 'approved':
        # Get the email of the client who made the payment
        email = payment_info['payer']['email']
        description = payment_info['description'].strip()
        #title = order['additional_info']['items'][0]['title']
         
         
        print(f"The payment with ID {payment_id} was approved and the client's email is {email}.")
    else:
        print(f"The payment with ID {payment_id} was not approved.")

