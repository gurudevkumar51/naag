# import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# os.environ['TWILIO_ACCOUNT_SID']
account_sid = "AC63b3b166b4f1bddfa39880b081e3c33c"
# os.environ['TWILIO_AUTH_TOKEN']
auth_token = "44fedc368df80653361c1904a11a41f2"
client = Client(account_sid, auth_token)

# message = client.messages \
#                 .create(
#                      to='9472532596',
#                      from_='9110517331',
#                      body="Guru Earth's mightiest heroes."
#                  )

# print(message.sid)
client = Client(account_sid, auth_token)

# service = client.messaging \
#                 .services \
#                 .create(friendly_name='My First Messaging Service')

# message = client.messages.create(
#          body='Guru test.',
#          messaging_service_sid="MG540eed784f5ebf1b604bfebdadc7b8b1",
#          to='+919472532596'
#      )
message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                    #  messaging_service_sid="MG540eed784f5ebf1b604bfebdadc7b8b1",
                     from_='+919110517331',
                     to='+919472532596'
                 )

# print(service.sid)
print(message)
