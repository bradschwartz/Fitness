import smtplib
from email.mime.text import MIMEText
import scrape
import logging
import os

logging.basicConfig(format='"%(asctime)s - %(name)-12s  %(levelname)-8s %(message)s"', level=logging.INFO)
logger = logging.getLogger('email_summary')


def construct_email(workouts):
    logger.info('Constructing email')
    email = MIMEText(workouts, 'html')
    email['Subject'] = "Today's Daily Workouts"
    email['From'] = 'baschwa@umich.edu'
    email['To'] = 'baschwa@umich.edu'

    return email


def send_email(email):
    try:
        password = os.environ['EMAIL_PASSWORD']
        logger.info('Attempting to send email')
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp_client:
            smtp_client.starttls()
            smtp_client.login(user='baschwa@umich.edu', password=password)
            smtp_client.send_message(email)
    except Exception as err:
        logger.error('Problem sending email: %s' % err)
    else:
        logger.info('Email sent successfully')


def main():
    workouts = scrape.main()
    email = construct_email(workouts)

    send_email(email)


if __name__ == '__main__':
    main()