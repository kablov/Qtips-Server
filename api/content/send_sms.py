from twilio.rest import Client
from qtips import settings


def send_sms(phone, text):
    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN

    client = Client(account_sid, auth_token)

    client.messages.create(
        to=phone,
        from_=settings.TWILIO_FROM_NUMBER,
        body=text
    )
