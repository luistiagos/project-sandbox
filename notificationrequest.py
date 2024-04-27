import requests
import json

# The URL of the API endpoint you want to send the POST request to
url = " http://digitalstoregames.pythonanywhere.com/notification3?productId=2,9,10,11,6&email=luistiago.andrighetto@gmail.com&fone=&service=upsell&ids=2,9,10,11,6&email=luistiago.andrighetto@gmail.com&telefone=&offers=&index=0&test=1"

# Data to be sent in the POST request, in JSON format
data = {}

# Convert the data dictionary to JSON format
payload = json.dumps(data)

# Set the headers to indicate that we are sending JSON data
headers = {'Content-Type': 'application/json'}

# Send the POST request
response = requests.post(url, data=payload, headers=headers)

# Check the response from the server
if response.status_code == 200:
    print("POST request was successful!")
    print("Response:", response.text)
else:
    print(f"POST request failed with status code {response.status_code}")
    print("Response:", response.text)
