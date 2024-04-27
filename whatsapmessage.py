import requests

# API endpoint
api_url = "https://api.whatsapp.com/v1/messages"

# Replace with your API token and phone number
api_token = "your_api_token"
phone_number = "whatsapp:1234567890"

# Replace with your message template and dynamic parameters
message_template = "Hello, {{name}}! Your order {{order_number}} is confirmed."

# Replace with actual dynamic data
dynamic_data = {
    "name": "John",
    "order_number": "12345"
}

# Build the message
message = {
    "phone_number": phone_number,
    "message": {
        "template_name": "order_confirmation",
        "language": "en",
        "components": [
            {
                "type": "body",
                "parameters": dynamic_data
            }
        ]
    }
}

# Send the message using POST request
response = requests.post(api_url, json=message, headers={"Authorization": f"Bearer {api_token}"})

# Check the response
if response.status_code == 200:
    print("Message sent successfully!")
else:
    print("Message sending failed:", response.text)
