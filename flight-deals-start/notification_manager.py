from twilio.rest import Client
import os
class NotificationManager:
    def __init__(self) -> None:
        
        self.account_sid = os.environ['TWILIO_ACCOUNT_SID']
        self.auth_token = os.environ['TWILIO_AUTH_TOKEN']
        self.twilio_num = os.environ['TWILIO_NUM']
        self.client = Client(self.account_sid, self.auth_token)
    
    def generating_message(self):
        message = self.client.messages \
            .create(
                body=full_text,
                from_=twilio_num,
                to='+11111111'
            )
        #This class is responsible for sending notifications with the deal flight details.
    pass