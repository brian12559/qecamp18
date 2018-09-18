'''
Created on Aug 31, 2018

@author: bmurray
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# this Base class is serving basic attributes for every single page inherited from Page class

class Page(object):
    def __init__(self, driver, base_url='https://polarion.engineering.redhat.com/polarion/'):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30
        #self.start() 
 
    def find_element(self, *locator):
        #this line doesnt work.  gets attribute error on the wait
        #wait = WebDriverWait(self.driver, 10)
        #return wait.until(EC.element_to_be_clickable(*locator))
        #might want to throw this in a loop to wait for object until timeout
        return self.driver.find_element(*locator)
        
    #def find_element(self, *locator):
        #return self.driver.wait.until(EC.visibility_of(*locator))
    
    def open(self,url):
        #url = self.base_url + url
        self.driver.get(url)
        
    def get_title(self):
        return self.driver.title
        
    def get_url(self):
        return self.driver.current_url
    
    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()