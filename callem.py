"""

You will need to have the twilio API installed on your machine, and you should
have already set up a developer account to get your Twilio number.

This is set up to call all the numbers in the spammer list, 30 seconds apart,
and repeat the process every 10 minutes.  So for 10 numbers, you can expect
to make about 960 calls daily.  At the rates of $0.002 per call, sweet revenge
can be had for under $2 a day.

Note: use the full number of the form +12121234567 for all phone numbers.

"""

from twilio.rest import Client
import time

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "your account ID"
auth_token = "your secret token"
client = Client(account_sid, auth_token)

spammers = [
  "Phone number that spams you 1",
  "Phone number that spams you 2",
  "Phone number that spams you 3",
  "Phone number that spams you 4",
  "Phone number that spams you 5",
  "Phone number that spams you 6"
]

for i in range(30):
  for number in spammers:
    call = client.calls.create(
        to=number,
        from_="your twilio number with country code",
        url="url to your xml file"
    )
    time.sleep(10)

    print("Called {}: {}".format(number,call.sid))
  time sleep(600)
