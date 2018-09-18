from twilio.rest import Client 

def sendMessage(number, message):
    
    account_sid = '<Insert SID>' 
    auth_token = '<Insert Token>'
    client = Client(account_sid, auth_token) 

    message = client.messages.create( 
        from_='+12342318928',  
        body=message,      
        to=number 
    ) 

    return (message.sid)