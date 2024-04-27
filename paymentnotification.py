from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook_listener():
    # Verify the webhook signature to ensure it's from PayPal (security check)
    # You can find the code for verifying the signature in PayPal's documentation.

    event_data = request.json
    event_type = event_data['event_type']
    payment_status = event_data['resource']['status']

    if event_type == 'PAYMENT.SALE.COMPLETED' and payment_status == 'completed':
        # User has paid
        # Perform the action for successful payment
        print("Payment completed. Action for successful payment.")

    elif event_type == 'PAYMENT.SALE.DENIED' and payment_status == 'denied':
        # User didn't pay
        # Perform the action for a denied payment
        print("Payment denied. Action for denied payment.")

    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)  # Replace with the port you're using

