from twilio.rest import Client


def send_sms(phone, text):
    account_sid = "AC9fc8bf64e0f96d06e254e9962a6f0a6f"
    auth_token = "46d6c4f7b46652dfe1420cd5179bfcd8"

    client = Client(account_sid, auth_token)

    client.messages.create(
        to = phone,
        from_ = "+16148812580",
        body = text
    )
