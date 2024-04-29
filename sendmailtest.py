from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import logging

logging.basicConfig(filename="mail.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.INFO)


def sendemails(ffrom, to, subject, msg):
    logging.info('enviando email: ' + to)
    message = Mail(
    from_email=ffrom,
    to_emails=to,
    subject=subject,
    html_content=msg)
    try:
        sg = SendGridAPIClient('secret')
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)
        
        
sendemails('luistiago.andrighetto@gmail.com', 'luistiago.andrighetto@gmail.com', "Acesso a Nuvem Digital", "ola")