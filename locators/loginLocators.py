'''
Created on August 31,2018

@filename loginLocators.py   
@author: bmurray
'''

from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    USERNAME      = (By.XPATH, '//input[contains(@id,\'username\')]') #an example using contains
    PASSWORD1      = (By.ID, 'com.polarion.password') #works on prod prev version
    PASSWORD2      =  (By.XPATH, "//*[contains(@id, '.password')]") #SR3
    PASSWORD3a      = (By.XPATH, "//*[contains(@id, 'j_password')]") #SR3
    PASSWORD3      = (By.ID, 'j_password') #SR3   an exact example
    SUBMIT        = (By.ID, 'submitButton')
    REMEMBERME    = (By.NAME, 'rememberme')
    ERROR_MESSAGE2 = (By.ID, 'message_error')
    #good example.  in latest version of Polarion it changed to this
    ERROR_MESSAGE = (By.ID, 'errorMessage')
    POLARION_LOGO = (By.XPATH,"//img[@class[contains(., 'polarion-Logo')]]")
    LOADING = (By.XPATH,"//img[@src[contains(., 'progress.gif')]]")
                     
  
class LogoutPageLocators(object):
    GEARICONrec    = (By.CSS_SELECTOR, 'img.gwt-Image')  #what IDE recorded
    GEARICON    = (By.XPATH, '//img[@src[contains(., \'settings_off\')]]') #what I got from firebug
    SETTINGSON  = (By.XPATH, '//img[@src[contains(., \'settings_on\')]]')
    LOGOUT      = (By.XPATH, '//img[@src[contains(., \'logout\')]]')  
    HIDE     = (By.XPATH, '//img[@src[contains(., \'hide\')]]')  
    
    # for maintainability we can seperate web objects by page name

#not used, this is from example
class MainPageLocators(object):
    LOGO          = (By.ID, 'nav-logo')
    NAVIGATORDOMS =  (By.XPATH, '//*[contains(@id,\'DOM_\')]')
    MENUEXPAND    =   (By.XPATH, "//div[@class='polarion-NavigatorContainer']//td[.='Expand']")
  
