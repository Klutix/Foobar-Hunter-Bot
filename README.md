# Foobar-Hunter-Bot
A python application designed to crawl and hunt for Googles Foobar challenge.

Requirements:
- Minimum python 3.5
- Windows for winbeep(has not been tested with Linux or OSX
- You will need selenium, PIL, and WebColors installed. Can all be installed via pip.
  
How it works:
  FHB runs by running a single instance web crawler that examines each page to see if it contains the foobar challenge. If a match is found an alarm will sound
and the option to either continue and add page to false postive list or turn off bot will appear.(both will kill sound you will be experiencing). If match is not found the bot simply does another search and repeats the process.
  -note The delays between searches are manditory becuase nature of the foobars appearance.
  -note This bot will run in the background. So you are free to care about your business once its in motion.

How to run the bot:
  1. Make sure you have the requirements installed. 
  
  Edit the line below in foobar.py
  
  chromedriver = "C:/Users/kiren/Desktop/Foobar-Hunter-Bot-master/chromedriver.exe" 

  and fix the path to the driver location in bot directory.

  -note if you need different version can be found online. http://chromedriver.chromium.org/downloads

2. Run the script.
  If there are no errors you should see chrome appear and the bot will do its work. Feedback on search should be in output.
  
  
  
  
!!!!!!WARNING!!!!!
  if you find the foobar do not close the driver until you have logged in your google acount.




  
   

