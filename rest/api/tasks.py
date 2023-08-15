from .service import send_otp_via_email
from rest.celery import app


@app.task
def send_otp_email(email):
    send_otp_via_email(email)
