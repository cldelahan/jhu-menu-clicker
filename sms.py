from twilio.rest import Client 
import json

def sendMessage(number, message):
    with open ("account.json", 'r') as f:
        data = json.load(f)    
        account_sid = data["account_sid"]
        auth_token = data["auth_token"]
        from_num = data["phone"]   
    
    client = Client(account_sid, auth_token) 

    message = client.messages.create( 
        from_=from_num,  
        body=message,      
        to=number 
    ) 

    return (message.sid)