from twilio.rest import TwilioRestClient

account = "AC48601c58e7aab606291b66ea62c3b4da"
token = "9da3a132056c3d049a5b903e3dae1c11"
number = '+13473292301'


def send_sms(receive_num, content):
    """
    Sends a text message to the receiving number.
    """
    message = TwilioRestClient(account, token).create(to=receive_num,
                                                                  from_=number,
                                                                  body=content)
