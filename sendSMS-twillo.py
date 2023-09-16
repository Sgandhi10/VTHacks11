from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()


def sendSMS(_to, _body):
    account_sid = os.environ.get('ACCOUNT_SSID')
    auth_token = os.environ.get('AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='+18662611757',
        body=_body,
        to=_to
    )

    print(message.sid)


if __name__ == "__main__":
    sendSMS('+19732166660', "This is awesome!")
