# jhu-menu-clicker
Conner Delahanty
Fall, 2018

This repository contains the implementation of a JHU menu auto-reader. Executing main parses a list of numbers
stored in an accompanying pickle and sends to each number a copy of the FFC's menu and Nolan's menu
at Johns Hopkins University. 

Additionally:

numberManager.py offers methods regarding adding and removing numbers from the registry. 

sms.py offers a sendMessage method using Twilio

url.py uses BeautifulSoup as an web-scraper

-and finally-

readmenu.py utilized url.py and specifically reads FFC's and Nolan's menu

