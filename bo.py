import os
from sendgrid import SendGridAPIClient


sg = SendGridAPIClient(os.environ.get('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'))

data = {
    "email": "example@example.com",
    "source": "signup"
}

response = sg.client.validations.email.post(
    request_body=data
)

print(response.status_code)
print(response.body)
print(response.headers)