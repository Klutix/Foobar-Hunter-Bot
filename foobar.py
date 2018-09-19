import time
import os
import random
import winsound
from random import randint
from threading import Thread
from selenium import webdriver
from PIL import Image
#from twilio.rest import Client
from selenium.webdriver.chrome.options import Options
from ProgrammingTerms import *
from ImageProcessor import ImageProcessor

#Twilio Cilent setup
#client = Client("AC***********************", "**********************") #This is for twilio account

#Chrome Driver Setup
_chrome_options = Options()
#_chrome_options.add_argument('user-data-dir=C:/Users/kiren/AppData/Local/Google/Chrome/User Data')
#_chrome_options.add_argument('disable-infobars')
chromedriver = "C:/Users/kiren/Desktop/Foobar-Hunter-Bot-master/chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver,chrome_options=_chrome_options)

def AddToFalsePositiveList(phrase):
    with open('FPlist.txt','a') as file:
        file.write(phrase + ",")  
        file.close()

def isInFalsePostitiveList(phrase):
    if os.path.isfile('FPlist.txt'): 
        with open('FPlist.txt','r') as file:
            FalsePList = file.read()
            file.close()
        FalsePList = FalsePList.split(",")
        if phrase in FalsePList:
            return True
    return False

##def NotifyFoundMatch(): #This is for twilio account
##    client.messages.create(to="+1303-******", 
##                       from_="+720*******", 
##                       body="Found It!")
def Search():
    iterations = 1 
    while True:
        #phrase = GeneratePhrase(randint(1,2))
        phrase = get_from_winning_list()
        if isInFalsePostitiveList(phrase):
            continue
        print('Iteration: ' + str(iterations) + " Search-Criteria: " + phrase)
        driver.get('https://www.google.com/search?q='+ phrase)
        print("waiting for foo...")
        time.sleep(12)
        driver.save_screenshot("ScreenShot.png")
        ip = None
        ip = ImageProcessor("ScreenShot.png")
        print("    Processing Image...")
        ip.process()
        if ip.isMatch():
            winsound.Beep(1000,300000)#<---------This Needs Better solution
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("!! --             !!Match Found!! --               !!")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ")
            print("_____________________________________________________")
            print("Press FPC to add to FALSE POSITIVE LIST and Continue")
            print("Press FPQ to add to FALSE POSITIVE LIST and Quit & Close Browser")
            Input = input()
            if Input.upper() == "FPC":
                  AddToFalsePositiveList(phrase)
                  print('SEARCH CRITERIA: '+ phrase + 'Added to FPList.txt')
                  continue
                  iterations+=1
            elif Input.upper() == "FPQ":
                  AddToFalsePositiveList(phrase)
                  print('SEARCH CRITERIA: '+ phrase + 'Added to FPList.txt')
                  sys.exit()
                  return 0
            else:
                  break
        else:
            iterations+=1
            sleepTime = randint(3,3)
            print('    Next search in ' + str(sleepTime) + " seconds...")
            time.sleep(sleepTime)
#--------------------------------------------------------------------------                  
#------Find the FooBar-- solve the foobar            
Search()
                 



