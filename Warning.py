from twilio.rest import Client


account_sid = '****************************************'
auth_token = '*****************************'
twilio_number = '************'
recipient_number = '**********'


client = Client(account_sid, auth_token)

message = client.messages.create(
	body='Tsunami warning in effect until further notice. Please evacuate to higher ground immediately.',
	from_=twilio_number,
	to=recipient_number
)

print(f"Message sent with SID: {message.sid}")
