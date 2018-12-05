'''
Created on Nov 29, 2018

@author: bmurray
'''

from selenium import webdriver
#from pages import *
#from pages.logInPage import LoginPage1, LogoutPage
from pages.base import Page
#from pages.LogInPage import *
import logging, time, sys, ConfigParser, os
import pytest, unittest
from selenium.webdriver.common.by import By
import random
 
# setting the logging module to the console
logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(threadName)-2s) %(message)s', level=logging.INFO ,)
configini='tests/test.ini'
Config = ConfigParser.ConfigParser()
Config.read(configini)
Config.sections()

class amazing(unittest.TestCase):
    
    def setUp(self):
        #set variables, load the browser
        logging.info("Function Setup()") 
        logging.info('Current Working Directory: %s' % os.getcwd())
        logging.info("using default values from here") 
        self.test_url = 'https://www.amazon.com/' 
        #self.user = 'stester1'
        #self.password = "polarion"
        self.browser="ff"
        logging.info("Launching browser -> %s" % self.browser)
        #profile = webdriver.FirefoxProfile("default")
        if self.browser == "ff":
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Chrome()
        #create instances of the classes we intend to use in the tests
        self.loader = Page(self.driver)
       
         
    def tearDown(self):
        #close the browser
        logging.info("Function tearDown()")
        self.driver.close()
        #notes
        #click result 6
        #css=#result_6 .a-size-base
        
        #click result 9 in drop down list
        #css=#issDiv9 > .s-heavy:nth-child(2)
        
    def test_login(self):
        #time to think before choosing result
        think_time = 3
        #time to read about product
        read_time = 5
        #how many loops
        my_loops = 10
        #The list of shit
        my_items1 = ['photo album','tooth picks','candy wrapper','model car','bananas','water bottle','lace','money','desk','pool stick','canvas','camera','thermostat','sidewalk','screw','tire swing','keyboard','spoon','watch','nail file','doll','chalk','truck','table','sticky note','bookmark','headphones','checkbook','coasters','car','flag','bowl','clamp','zipper','face wash','picture frame','stop sign','greeting card','shirt','television','helmet','mirror','pen','tree','tv','balloon','cookie jar','buckel','charger','tissue box','clothes','outlet','scotch tape','hair tie','beef','keys','CD','grid paper','knife','floor','boom box','bread','bed','twister','nail clippers','bow','piano','playing card','glass','plastic fork','cork','ipod','spring','air freshener','leg warmers','teddies','soap','glow stick','deodorant ','drawer','towel','cell phone','shoes','chapter book','slipper','vase','house','credit card','sandal','wagon','blouse','door','bag','purse','controller','thread','rubber duck','pencil','pillow','perfume','mp3 player','clock','carrots','window','magnet','bottle','fork','mop','pants','lotion','shovel','fridge','toothbrush','milk','lip gloss','sand paper','eraser','tomato','ice cube tray','flowers','washing machine','lamp','sketch pad','puddle','shampoo','button','socks','bracelet','cup','glasses','conditioner','video games','monitor','speakers','newspaper','fake flowers','stockings','sailboat','seat belt','eye liner','soda can','chair','cinder block','soy sauce packet','thermometer','blanket','book','white out','shawl','ring','cat','toe ring','shoe lace','sharpie','mouse pad','hair brush','plate','remote','toilet','candle','sponge','box','radio','couch','USB drive','apple','street lights','key chain','paint brush','lamp shade','sun glasses','brocolli','rug','computer','clay pot','packing peanuts','needle','twezzers','wallet','rubber band','paper','rusty nail','bottle cap','drill press','sofa','toothpaste','chocolate','phone','food','hanger',]
 
        logging.info("loading url %s" % self.test_url)
        self.loader.open(self.test_url)
        time.sleep(5)
        #search
        for x in range(0, my_loops):
            try:
                this_loop = random.choice(my_items1)
                logging.info("searching for %s" % this_loop)
                self.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(this_loop)
                time.sleep(2)
                rand_item = random.randint(1,9)
                #just use main search if 1
                if rand_item > 1:
                    logging.info("selecting item %s in the drop down list" % rand_item)
                    self.driver.find_element(By.CSS_SELECTOR, '#issDiv%s > .s-heavy:nth-child(2)' % rand_item).click()
                #otherwise use a random item in the list
                else:
                    logging.info("clicking search")
                    self.driver.find_element(By.CSS_SELECTOR, 'input.nav-input').click()
     
                logging.info("getting results for %s" % self.driver.find_element(By.ID, 'twotabsearchtextbox').get_attribute("value")) 
                time.sleep(think_time)  
                #let's look at one of the results
                rand_result = random.randint(1,10)
                logging.info("selecting item %s in the results" % rand_result)
                self.driver.find_element(By.CSS_SELECTOR, '#result_%s .a-size-base' % rand_result).click()
                time.sleep(read_time)
                self.driver.find_element(By.ID, 'twotabsearchtextbox').clear()
            except:
                self.driver.find_element(By.ID, 'twotabsearchtextbox').clear()
                logging.info("Result not found, resume with next search")
       
if __name__ == "__main__": # allows unittest to start by running this class file
    unittest.main()  
    
    
    