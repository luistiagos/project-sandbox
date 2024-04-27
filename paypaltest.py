import paypalrestsdk

# Replace with your own PayPal credentials
paypalrestsdk.configure({
    "mode": "sandbox",  # "sandbox" for testing, "live" for production
    "client_id": "Ae4jEIUoWygU0sATl3P1CMBpKvLSVBwA4Yk5hbKCfbSIhdIs9_DBaWHdn_TakwIqPUyir2nT1g6jZKB7",
    "client_secret": "EHosEiOT9vBDgk8w6vqhi0OS-NSx03BSizhHZro736FbSWAtLln85DaDWPSpX3OQJAd-tqLrY_WMQN3j"
})

# Create a payment
payment = paypalrestsdk.Payment({
    "intent": "sale",
    "payer": {
        "payment_method": "paypal"
    },
    "transactions": [
        {
            "amount": {
                "total": "10.00",
                "currency": "USD"
            }
        }
    ],
    "redirect_urls": {
        "return_url": "https://www.google.com",
        "cancel_url": "https://www.google.com"
    }
})

if payment.create():
    print("Payment created successfully")
    for link in payment.links:
        if link.rel == "approval_url":
            print("Approval URL: %s" % link.href)
else:
    print("Error while creating payment:", payment.error)
