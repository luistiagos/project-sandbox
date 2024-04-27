import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='contato@digitalstoregames.com',
    to_emails='luistiago.andrighetto@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient('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')
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)