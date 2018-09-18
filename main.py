import readmenu
import sms
import numberManager as nm
import datetime

def sendMenu():
    # getting the month
    now = datetime.datetime.now()
    year = str(now.year)
    if (len(str(now.month)) == 1):
        month = "0"+str(now.month)
    else:
        month = str(now.month)
    day = str(now.day)
    
    
    ffcMenu = readmenu.readFFC(month, day, year)
    nolansMenu = readmenu.readNolans(month, day, year)
    
    message = month + "/" + day + "/" + year + "\n"
    message += "FFC:\n"
    for item in ffcMenu:
        message+=(item+"\n")
        
    message += "\nNolan\'s:\n"
    for item in nolansMenu:
        message+=(item+"\n")
        
    
    numberList = nm.getNumberList()
    for number in numberList:
        print(sms.sendMessage(number, message))
        
sendMenu()