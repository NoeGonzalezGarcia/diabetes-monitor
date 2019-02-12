# we import the Twilio client from the dependency we just installed
from twilio.rest import Client


def send_sys_admin_text():
    # the following line needs your Twilio Account SID and Auth Token
    client = Client("AC794b3655c6fbb6eec16b6b5a3bbc756b", "73aea0612e7057b63809b6224a6f9d86")

    # change the "from_" number to your Twilio number and the "to" number
    # to the phone number you signed up for Twilio with, or upgrade your
    # account to send SMS to any phone number
    client.messages.create(to="+12626616910",
                           from_="+12622791818",
                           body="SYSTEM DISCONNECT. SYSTEM ADMIN ATTENTION REQUIRED")