# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC2e309bccc7a8232680137162fdd8b55e"
auth_token = os.environ["eae6d51f02535de1718f0b8268906ab9"]
client = Client(account_sid, auth_token)

message = client.messages.create(
  body="Hello from Twilio",
  from_="+17432183246",
  to="+919665539971"
)

print(message.sid)