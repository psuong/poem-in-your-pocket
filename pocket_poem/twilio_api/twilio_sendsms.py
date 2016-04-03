from twilio.rest import TwilioRestClient


account = "AC48601c58e7aab606291b66ea62c3b4da"
token = "9da3a132056c3d049a5b903e3dae1c11"
number = '+13473292301'
# Generate a client object to send SMS
client = TwilioRestClient(account, token)


def send_sms(receiver_number, context):
    """
    Input a number to get a text using the TwilioRestClient.
    :param receiver_number: string, number to send to
    :param context: string, haiku to generate
    """
    message = client.messages.create(to=receiver_number,
                                     from_=number,
                                     body=context)
