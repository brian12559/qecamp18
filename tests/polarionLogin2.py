'''
Created on Aug 31, 2018

@author: bmurray
'''

from selenium import webdriver
#from pages import *
from pages.logInPage import LoginPage1, LogoutPage
from pages.base import Page
#from pages.LogInPage import *
import logging, time, sys
import pytest, unittest
 
# setting the logging module to the console
logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(threadName)-2s) %(message)s', level=logging.INFO ,)


class polarionLogin2(unittest.TestCase):

    def setUp(self):
        #set variables, load the browser
        logging.debug("Function Setup()") 
        self.polarion_url = 'https://polarion.engineering.redhat.com/polarion/#/project/Polarion'
        self.polarion_url2 = 'https://polarion.engineering.redhat.com/polarion'  
        self.user = 'stester1'
        self.password = "polarion"
        self.browser="ff"
        self.browser="chrome"
        logging.info("Launching browser -> %s" % self.browser)
        if self.browser == "ff":
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Chrome()
        #create instances of the classes we intend to use in the tests
        self.loader = Page(self.driver)
        self.loginPage = LoginPage1(self.driver)
        self.logoutPage = LogoutPage(self.driver)
         
    def tearDown(self):
        #close the browser
        logging.debug("Function tearDown()")
        self.driver.close()
        

    def test_login(self):
        logging.info("Test logging into Polarion specifying the project")
        logging.info("loading url %s" % self.polarion_url)
        self.loader.open(self.polarion_url) #or this
        #self.driver.get(self.polarion_url)
        self.loginPage.login_with_valid_user(self.user, self.password, True)
        #polarion never loads the project in less than 3 seconds
        time.sleep(3)
        self.loginPage.waitForPolarion(30)
        logging.info("Logging out")
        self.logoutPage.logout()
        
    def test_logininvalid(self):
        logging.info("Test logging into Polarion with bad pw")
        logging.info("loading url %s" % self.polarion_url)
        self.loader.open(self.polarion_url) #or this
        #self.driver.get(self.polarion_url)
        errMess = self.loginPage.login_with_invalid_user(self.user, "bad", True)
        logging.info(errMess)
        assert errMess == "Sorry, but the Username or Password is invalid."


    def atest12_numbers_3_4(self):
        assert 6+6 == 12 

      
if __name__ == "__main__": # allows unittest to start by running this class file
    unittest.main()  
    
    
    