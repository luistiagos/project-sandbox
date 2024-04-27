import requests

# Replace the URL with the endpoint you want to send the POST request to
#url = "http://digitalstoregames.pythonanywhere.com/notification3?productId=9&email=luistiago.andrighetto@gmail.com&fone=4198443522&service=upsell&ids=9&email=luistiago.andrighetto@gmail.com&telefone=4198443522&offers=6;9;11;10&index=1&test=1"
#url = "http://digitalstoregames.pythonanywhere.com/notification3?data.id=73823339307&productId=9&email=tiago.hablich%40gmail.com&fone=&productId=300000&type=payment&test=1"

url = 'http://digitalstoregames.pythonanywhere.com/notification3?data.id=73824732287&email=luistiago.andrighetto%40gmail.com&fone=&productId=300000&type=payment&test=1'

# Replace this dictionary with the data you want to send in the POST request
data = {
  
}

# Make the POST request
response = requests.post(url, data=data)

# Check the status code of the response
if response.status_code == 200:
    print("POST request was successful!")
    print("Response content:")
    print(response.text)
else:
    print(f"POST request failed with status code {response.status_code}")
    print("Response content:")
    print(response.text)
