import readmenu
import sms
import numberManager as nm
import datetime

def sendMenu():
    # getting the month
    now = datetime.datetime.now()
    year = str(now.year)
    
    month = str(now.month)
    if (len(month) == 1):
        month = "0"+str(now.month)
        
    day = str(now.day)
    if (len(day) == 1):
        day = "0" + str(day)
    
    
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
        

print(nm.getNumberList())
sendMenu()