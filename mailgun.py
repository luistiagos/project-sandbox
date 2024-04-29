import requests

def send_simple_message():
	return requests.post(
		"https://api.mailgun.net/v3/sandbox2677398c3ff640d899160b5d9bf711e3.mailgun.org/messages",
		auth=("api", "secret"),
		data={"from": "Mailgun Sandbox <postmaster@sandbox2677398c3ff640d899160b5d9bf711e3.mailgun.org>",
			"to": "Luis Tiago <luistiago.andrighetto@gmail.com>",
			"subject": "Hello Luis Tiago",
			"text": "Congratulations Luis Tiago, you just sent an email with Mailgun!  You are truly awesome!"})


 
 
send_simple_message()