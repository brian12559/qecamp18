'''
Created on Aug 31, 2018

@author: bmurray
'''

from selenium import webdriver
#from pages import *h
from pages.logInPage import LoginPage1, LogoutPage
from pages.base import Page
#from pages.LogInPage import *
import logging, time, sys, os
    #ConfigParser, os
import pytest, unittest
 
# setting the logging module to the console
logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(threadName)-2s) %(message)s', level=logging.INFO ,)

class LicenseCount(unittest.TestCase):
    
    def setUp(self):
        #set variables, load the browser
        logging.info("Function Setup()") 
        logging.info("using default values from here") 
        self.polarion_url = 'https://polarion.engineering.redhat.com' #/polarion/#/project/Polarion'
        self.user = "devops_adminreader"
        self.password = "polarion"
        self.browser="ff"
        #fix url
        self.polarion_url = "%s/polarion/#/administration/license" % self.polarion_url   
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
        logging.info("Function tearDown()")
        self.driver.close()
        
    def test_login(self):
        logging.info("Test logging into Polarion with a valid user and password")
        logging.info("loading url %s" % self.polarion_url)
        self.loader.open(self.polarion_url)
        self.loginPage.login_with_valid_user(self.user, self.password, True)
        #polarion never loads the project in less than 3 seconds
        time.sleep(3)
        loginTime = self.loginPage.waitForPolarion2(30)
        
        #give license info extra time to load.  we are not time dependent here
        time.sleep(10)
        elements = self.driver.find_elements_by_class_name("JSTreeTableCell")
        current = int(elements[1].text) - int(elements[3].text)
        logging.info("Number of current users is %s" % current)

        with open("/home/bmurray/Documents/polarion/LicenseCount.csv", "a") as myfile:
            myfile.write(str(time.time()) + "," + str(current) +  "\n")
        with open("/home/bmurray/Documents/polarion/LoginTime.csv", "a") as myfile:
            myfile.write(str(time.time()) + "," + loginTime +  "\n")
      
if __name__ == "__main__": # allows unittest to start by running this class file
    unittest.main()  
    
    
    