from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "XXXXXXXX"
auth_token  = "XXXXXXXX"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="HELLOOOOOOOOOOO???!?!?!",
    to="XXXXXXXXXX",    # Replace with your phone number
    from_="XXXXXXXXXX") # Replace with your Twilio number
print message.sid
