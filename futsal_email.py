import smtplib
from email.message import EmailMessage
import os
import random


def email_attachements_main(email_to):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login('rohithravi2015@gmail.com', '')
        # https://myaccount.google.com/apppasswords
        otp = random.randint(1000, 9999)
        email = EmailMessage()
        email['Subject'] = 'Futsal: Login with otp.'
        email['From'] = 'rohithravi2015@gmail.com'
        email['To'] = email_to
        email.set_content(f'''
        Hello,
        Your One Time Password (OTP) to Login on Futsal is {otp}.
        Please note, this OTP is valid only for mentioned transaction 
        and cannot be used for any other transaction.
        Please do not share this One Time Password with anyone.

        ''')

        smtp.send_message(email)
        return otp


def booking_confirmation(email_to, slot_date_str, slot_time):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login('rohithravi2015@gmail.com', '')
        # https://myaccount.google.com/apppasswords
        email = EmailMessage()
        email['Subject'] = 'Futsal: Booking confirmation.'
        email['From'] = 'rohithravi2015@gmail.com'
        email['To'] = email_to
        email.set_content(f'''
        Hello,
        This is a confirmation mail for the booking done for
        {slot_date_str} : {slot_time}:00 hr.
        
        Thank you

        ''')

        smtp.send_message(email)


def email_welcome(email_to):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login('rohithravi2015@gmail.com', '')
        # https://myaccount.google.com/apppasswords
        email = EmailMessage()
        email['Subject'] = 'Welcome to Futsal'
        email['From'] = 'rohithravi2015@gmail.com'
        email['To'] = email_to
        email.set_content(f'''
        Hello,
        You have successfully signed up for Futsal.
        Please use "{email_to}" as username to login.

        Thank you

        ''')

        smtp.send_message(email)






