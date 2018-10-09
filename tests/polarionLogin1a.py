'''
Created on Aug 31, 2018

@author: bmurray
'''

from selenium import webdriver
#from pages import *
from pages.logInPage import LoginPage1, LogoutPage
from pages.base import Page
#from pages.LogInPage import *
import logging, time, sys, ConfigParser, os
import pytest, unittest
 
# setting the logging module to the console
logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(threadName)-2s) %(message)s', level=logging.INFO ,)
configini='tests/test.ini'
Config = ConfigParser.ConfigParser()
Config.read(configini)
Config.sections()

class polarionLogin1(unittest.TestCase):
    
    def setUp(self):
        #set variables, load the browser
        logging.info("Function Setup()") 
        logging.info('Current Working Directory: %s' % os.getcwd())
        if (os.path.isfile(configini)):
            logging.info("retrieving test data from %s" % configini)
            self.browser = self.ConfigSectionMap("TEST_DATA")['browser']
            self.user = self.ConfigSectionMap("TEST_DATA")['user']
            self.password = self.ConfigSectionMap("TEST_DATA")['password']
            self.polarion_url = self.ConfigSectionMap("TEST_DATA")['server']
        else:
            logging.info("using default values from here") 
            self.polarion_url = 'https://polarion.engineering.redhat.com' #/polarion/#/project/Polarion'
            self.user = 'stester1'
            self.password = "polarion"
            self.browser="ff"
        #fix url
        self.polarion_url = "%s/polarion/#/project/Polarion" %self.polarion_url
        logging.info("Launching browser -> %s" % self.browser)
        if self.browser == "ff":
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Chrome()
        
    def ConfigSectionMap(self, section):
        dict1 = {}
        options = Config.options(section)
        for option in options:
            try:
                dict1[option] = Config.get(section, option)
                if dict1[option] == -1:
                    logging.info("skip: %s" % option)
            except:
                logging.info("exception on %s!" % option)
                dict1[option] = None
        return dict1
         
    def tearDown(self):
        #close the browser
        logging.info("Function tearDown()")
        self.driver.close()
        
    def test_login(self):
        logging.info("Test logging into Polarion with a valid user and password")
        logging.info("loading url %s" % self.polarion_url)
        self.driver.get(self.polarion_url)
        
        logging.info("Entering username: %s using %s" %(self.user, "By.XPATH, '//input[contains(@id,\'username\')]'"))
        self.driver.find_element_by_xpath('//input[contains(@id,\'username\')]').send_keys(self.user)
        logging.info("Entering password: %s using %s" %(self.password, "By.ID, 'j_password'"))
        self.driver.find_element_by_id('j_password').send_keys(self.password)
        logging.info("clicking 'LOG IN' button using {0}".format("By.ID, 'submitButton'"))
        self.driver.find_element_by_id('submitButton').click()
        #polarion never loads the project in less than 3 seconds
        time.sleep(3)
        startloading = time.time()  
        maxwaittime=60
        try:  
            self.driver.implicitly_wait(3)
            elapsedtime = time.time() - startloading         
            while (self.driver.find_element_by_xpath("//img[@src[contains(., 'progress.gif')]]") and elapsedtime < maxwaittime): 
                elapsedtime = time.time() - startloading
                logging.info("still waiting...%s" % str(elapsedtime))
                time.sleep(3)
            logging.info("Polarion did not finish loading in %s seconds" % str(maxwaittime))
        except Exception as e:
            #setting default imlicit wait time back to 10
            self.driver.implicitly_wait(10)   
            logging.info("finished loading loading polarion")
            logging.info("time to load Polarion -> %s" % str(time.time() - startloading))
        logging.info("Logging out")
        logging.info("clicking gear icon using {0}".format("By.XPATH, '//img[@src[contains(., \'settings_off\')]]'"))
        self.driver.find_element_by_xpath('//img[@src[contains(., \'settings_off\')]]').click()
        #self.wait_for_settings()
        logging.info("clicking Logout using {0}".format("By.XPATH, '//img[@src[contains(., \'logout\')]]'"))
        self.driver.find_element_by_xpath('//img[@src[contains(., \'logout\')]]').click()
 
      
if __name__ == "__main__": # allows unittest to start by running this class file
    unittest.main()  
    
    
    