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

class polarionLogin(unittest.TestCase):
    
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
        #create instances of the classes we intend to use in the tests
        self.loader = Page(self.driver)
        self.loginPage = LoginPage1(self.driver)
        self.logoutPage = LogoutPage(self.driver)
        
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
        self.loader.open(self.polarion_url)
        self.loginPage.login_with_valid_user(self.user, self.password, True)
        #polarion never loads the project in less than 3 seconds
        time.sleep(3)
        assert self.loginPage.waitForPolarion(30)
        logging.info("Logging out")
        self.logoutPage.logout()
        
    def test_logininvalidpw(self):
        logging.info("Test logging into Polarion with bad password")
        logging.info("loading url %s" % self.polarion_url)
        self.loader.open(self.polarion_url)
        errMess = self.loginPage.login_with_invalid_user(self.user, "bad")
        logging.info(errMess)
        assert errMess == "Sorry, but the Username or Password is invalid."
       
    def test_logininvalidnullname(self):
        logging.info("Test logging into Polarion with bad password")
        logging.info("loading url %s" % self.polarion_url)
        self.loader.open(self.polarion_url)
        errMess = self.loginPage.login_with_invalid_user("", "")
        logging.info(errMess)
        assert errMess == "Please provide user name and password to login to Polarion."
        
    def test_logininvalidname(self):
        logging.info("Test logging into Polarion with bad password")
        logging.info("loading url %s" % self.polarion_url)
        logging.info(self.driver.implicitly_wait)
        self.loader.open(self.polarion_url)
        errMess = self.loginPage.login_with_invalid_user("fred smith", "")
        logging.info(errMess)
        assert errMess == "Sorry, but the expected user does not exist and auto-create cannot be used because the user name contains the following unsupported character(s) ' '." 


    def atest12_numbers_3_4(self):
        assert 6+6 == 12 

      
if __name__ == "__main__": # allows unittest to start by running this class file
    unittest.main()  
    
    
    