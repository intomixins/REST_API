from django.core.mail import send_mail
from random import randint
from django.conf import settings
from .models import User


def send_otp_via_email(email):
    subject = f'Your account verification email'
    otp = randint(10 ** 5, 10 ** 6 - 1)
    email_from = settings.EMAIL_HOST
    message = f'Your otp is {otp}'
    send_mail(subject, message, email_from, [email])
    return email, otp
