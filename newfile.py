import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email):
    # Your email credentials
    sender_email = "luistiago,andrighetto@gmail.com"
    sender_password = "@Lt057869701625"

    # Create the email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = to_email
    message["Subject"] = subject

    # Attach the body of the email
    message.attach(MIMEText(body, "plain"))

    # Connect to the SMTP server (in this case, Gmail's SMTP server)
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        # Start TLS for security
        server.starttls()

        # Login to your Gmail account
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, to_email, message.as_string())

    print("Email sent successfully!")

# Example usage
subject = "<your_subject>"
body = "Hello, this is the body of the email."
recipient_email = "luistiago.andrighetto@gmail.com"

send_email(subject, body, recipient_email)


