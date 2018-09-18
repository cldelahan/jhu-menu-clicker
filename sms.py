from twilio.rest import Client 

def sendMessage(number, message):
    
    account_sid = 'AC75768e84a6059146bc2bc95a4e3dfbf3' 
    auth_token = '935b65e2e66fa16b6e143d1f133fbbb4' 
    client = Client(account_sid, auth_token) 

    message = client.messages.create( 
        from_='+12342318928',  
        body=message,      
        to=number 
    ) 

    return (message.sid)