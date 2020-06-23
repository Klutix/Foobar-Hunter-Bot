from selenium.webdriver.chrome.options import Options
from ProgrammingTerms import *
from ImageProcessor import ImageProcessor
from selenium.webdriver.common.by import By

#Chrome Driver Setup
_chrome_options = Options()
chromedriver = "chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver



def check_page_for_foobar():
    try:
        driver.find_element(By.XPATH, '//div[contains(@data-url,"foobar")]')
        input("Found it")
    except:
        pass

def Search(): 
    iterations = 1
    driver = webdriver.Chrome(chromedriver,chrome_options=_chrome_options)
    driver.delete_all_cookies()
    while True:
        #phrase = "python command line arguments"
        phrase = get_from_winning_list()
        #phrase = GeneratePhrase(randint(1,2))
        print('Iteration: ' + str(iterations) + " Search-Criteria: " + phrase)
        driver.get('https://www.google.com/search?q='+ phrase)
        check_page_for_foobar()
        sleepTime = randint(5,30)
        print("Sleeping for {}".format(sleepTime))
        time.sleep(SleepTime)
        iterations+=1
#------Find the FooBar-- solve the foobar            
Search()
