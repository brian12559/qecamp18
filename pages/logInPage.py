'''
Created on August 31, 2018

@filename logInPage.py
@author: bmurray
'''

from pages.base import Page
from locators.loginLocators import *
import logging, time
from selenium.webdriver.support import expected_conditions as EC

# Page objects are written in this module.
# Depends on the page functionality we can have more functions for new classes

class MainPage(Page):
    def check_page_loaded(self):
        return True if self.find_element(*MainPageLocators.LOGO) else False

     
class LoginPage1(Page):
    def check_page_loaded(self):
        return True if self.find_element(*LoginPageLocators.USERNAME) else False
    
    def enter_username(self, username):
        self.driver.find_element(*LoginPageLocators.USERNAMEXRAY).send_keys(username)

    def clear_username(self):
        self.driver.find_element(*LoginPageLocators.USERNAMEXRAY).clear()
        
    def enter_password(self, pw):
        self.driver.find_element(*LoginPageLocators.PASSWORDXRAY).send_keys(pw)

    def clear_password(self):
        self.driver.find_element(*LoginPageLocators.PASSWORDXRAY).clear()
    
    def click_login_button(self):
        self.driver.find_element(*LoginPageLocators.SUBMITXRAY).click()

    def click_rememeberme_box(self):
        self.driver.find_element(*LoginPageLocators.REMEMBERME).click()
        
    def loginuserxrayOLD(self, username, pw): #for devel and sr2
        logging.info("Entering username: %s using %s" %(username, LoginPageLocators.USERNAMEXRAY))
        #might need clear
        self.enter_username(username)
        logging.info("Entering password: %s using %s" %(pw, LoginPageLocators.PASSWORDXRAY))
        self.enter_password(pw)
        logging.info("clicking 'LOG IN' button using {0}".format(LoginPageLocators.SUBMITXRAY))
        self.click_login_button()
        time.sleep(5)

    def loginuserxray(self, username, pw):  # for devel and sr2
        logging.info("Entering username: %s using %s" % (username, LoginPageLocators.USERNAMEXRAY))
        # might need clear
        self.enter_username(username)
        logging.info("Entering password: %s using %s" % (pw, LoginPageLocators.PASSWORDXRAY))
        self.enter_password(pw)
        logging.info("clicking 'LOG IN' button using {0}".format(LoginPageLocators.SUBMITXRAY))
        startloading = time.time()
        self.click_login_button()
        elapsedtime = time.time() - startloading
        while not (self.driver.find_element(*LoginPageLocators.ISSUEKEYXRAY)):
            elapsedtime = time.time() - startloading
            logging.info("still waiting...%s" % str(elapsedtime))
            time.sleep(3)
        ltime = str((time.time() - startloading))
        logging.info("time to load XRAY -> %s" % ltime)
        with open("/home/bmurray//LoginTime.csv", "a") as myfile:
            myfile.write(time.ctime() + "," + ltime +  "\n")


    def login_with_valid_user(self, username, pw):
        self.loginuserxray(username, pw)
        return HomePage(self.driver)

    def login_with_invalid_user(self, username, pw, rememberme=False):
        self.loginuser(username, pw, rememberme)
        return self.find_element(*LoginPageLocators.ERROR_MESSAGE).text  
    

class LogoutPage(Page):
    def check_page_loaded(self):
        return True if self.find_element(*LogoutPageLocators.GEARICON) else False
    
    def click_gearicon (self):
        self.driver.find_element(*LogoutPageLocators.GEARICON).click()
    
    def wait_for_settings (self):
        self.driver.find_element(*LogoutPageLocators.SETTINGS)
        
    def click_logout (self):
        self.driver.find_element(*LogoutPageLocators.LOGOUT).click()
        
    def click_hide (self):
        self.driver.find_element(*LogoutPageLocators.HIDE).click()        
        
    def logout(self):
        logging.info("clicking gear icon using {0}".format(LogoutPageLocators.GEARICON))
        self.click_gearicon()
        #self.wait_for_settings()
        logging.info("clicking Logout using {0}".format(LogoutPageLocators.LOGOUT))
        self.click_logout()
        
        

class HomePage(Page):
    pass
    
class SignUpPage(Page):
    pass


        
        
        