# This file contains an array of helper funtions for BotScriptMain.py


import datetime

def timeHelper():
    dateData = datetime.datetime.now()
    formattedTime = str(dateData.month) + '/' + str(dateData.day) + '/' + str(dateData.year)
    return 

def quoteParser(inputString):
    body, author = inputString.split("-")
    return body
