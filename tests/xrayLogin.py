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
from optparse import OptionParser
import pytest, unittest
 
# setting the logging module to the console
logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(threadName)-2s) %(message)s', level=logging.INFO ,)


class xrayLogin(unittest.TestCase):

    def setUp(self):
        #set variables, load the browser
        logging.debug("Function Setup()") 
        self.xray_url = 'https://sandbox.xpand-it.com/secure/Dashboard.jspa'
        self.xray_url = "https://sandbox.xpand-it.com/projects/TOOL1?selectedItem=com.xpandit.plugins.xray:test-panel"
        self.user = 'user27'
        self.password = "rhtoolnext"
        self.browser="ff"
        #self.browser="chrome"
        logging.info("Launching browser -> %s" % self.browser)

         
    def tearDown(self):
        #close the browser
        logging.debug("Function tearDown()")
       # self.driver.close()
        

    def test_login(self):
        for z in range(1,50):
            if self.browser == "ff":
                self.driver = webdriver.Firefox()
            else:
                self.driver = webdriver.Chrome()

            # classes used in this file
            self.loader = Page(self.driver)
            self.loginPage = LoginPage1(self.driver)
            self.logoutPage = LogoutPage(self.driver)
            logging.info("Test logging into Xray")
            logging.info("loading url %s" % self.xray_url)
            self.loader.open(self.xray_url) #or this
            self.loginPage.login_with_valid_user(self.user, self.password)
            time.sleep(1)
            self.driver.close()

if __name__ == "__main__": # allows unittest to start by running this class file
    #global loglevel 
    argv = sys.argv[1:]
    
    # command line parser
    parser = OptionParser(usage='%prog [options] ', version='0.1',)
    parser.add_option("-n", "--browser", dest="browser", default="ff", help='Defines the browser to test')
    
    # read the command line parameters now
    (options, args) = parser.parse_args(argv)    
    logging.info("Command Line: %s" % sys.argv)
    logging.info(options.browser)
    
    unittest.main() 
    