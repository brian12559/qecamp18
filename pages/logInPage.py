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
        self.driver.find_element(*LoginPageLocators.USERNAME).send_keys(username)

    def clear_username(self):
        self.driver.find_element(*LoginPageLocators.USERNAME).clear()
        
    def enter_password1(self, pw):
        self.driver.find_element(*LoginPageLocators.PASSWORD1).send_keys(pw)
        
    def enter_password2(self, pw):
        self.driver.find_element(*LoginPageLocators.PASSWORD2).send_keys(pw)        
    
    def enter_password3(self, pw):
        self.driver.find_element(*LoginPageLocators.PASSWORD3).send_keys(pw)
        
    def clear_password(self):
        self.driver.find_element(*LoginPageLocators.PASSWORD).clear()
    
    def click_login_button(self):
        self.driver.find_element(*LoginPageLocators.SUBMIT).click()

    def click_rememeberme_box(self):
        self.driver.find_element(*LoginPageLocators.REMEMBERME).click()
        
    def loginuser(self, username, pw, rememberme=False): #for devel and sr2
        logging.info("Entering username: %s using %s" %(username, LoginPageLocators.USERNAME))
        #might need clear
        self.enter_username(username)
        logging.info("Entering password: %s using %s" %(pw, LoginPageLocators.PASSWORD3))
        self.enter_password3(pw)
        if rememberme:
            logging.info("clicking 'stay logged in' using {0}".format(LoginPageLocators.REMEMBERME))
            self.click_rememeberme_box()
        logging.info("clicking 'LOG IN' button using {0}".format(LoginPageLocators.SUBMIT))
        self.click_login_button()        

    def login_with_valid_user(self, username, pw, rememberme=False):
        self.loginuser(username, pw, rememberme)
        return HomePage(self.driver)

    def login_with_invalid_user(self, username, pw, rememberme=False):
        self.loginuser(username, pw, rememberme)
        return self.find_element(*LoginPageLocators.ERROR_MESSAGE).text  
    
    def polarion_ready(self):
        try:
            return self.driver.find_element(*LoginPageLocators.POLARION_LOGO)
        except Exception as e:
            return False
    
    def is_polarion_ready(self):
        iX=0
        while (not self.polarion_ready()) and iX<30:
            iX=iX+1
            time.sleep(1)
            
    def waitForPolarion(self, maxwaittime):
        startloading = time.time()
        try:  
            self.driver.implicitly_wait(3)
            elapsedtime = time.time() - startloading         
            while (self.driver.find_element(*LoginPageLocators.LOADING) and elapsedtime < maxwaittime): 
                elapsedtime = time.time() - startloading
                logging.info("still waiting...%s" % str(elapsedtime))
                time.sleep(3)
            logging.info("Polarion did not finish loading in %s seconds" % str(maxwaittime))
            return False
        except Exception as e:
            #do nothing...report has finished loading because we got an error looking for loading  
            #setting default imlicit wait time back to 10
            self.driver.implicitly_wait(10)   
            logging.info("finished loading loading polarion")
            logging.info("time to load Polarion -> %s" % str(time.time() - startloading))
            return True

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


        
        
        