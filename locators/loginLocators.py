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

    #for xray
    USERNAMEXRAY = (By.ID, 'login-form-username')
    PASSWORDXRAY = (By.ID, 'login-form-password')
    SUBMITXRAY = (By.ID, 'login-form-submit')
    ISSUEKEYXRAY = (By.ID, 'raven-test-filter-contains-text')

    #for CodeBeamer
    USERNAMECB = (By.ID, 'user')
    PASSWORDCB = (By.ID, 'password')
    SUBMITCB = (By.ID, 'login-button')
    ISSUEKEYCB = (By.ID, 'raven-test-filter-contains-text') #not done as can't login yet

    # for TestLab..hmmm this might be tricky...looks like its embedded java so inspect element does not work
    USERNAMETL = (By.ID, 'user')
    PASSWORDTL = (By.ID, 'password')
    SUBMITTL = (By.ID, 'login-button')
    ISSUEKEYTL = (By.ID, 'raven-test-filter-contains-text')  # not done as can't login yet

    # for PT
    USERNAMEPT = (By.NAME, 'email')
    PASSWORDPT = (By.NAME, 'password')
    SUBMITPT = (By.NAME, 'submit') #submit type id Sign in
    ISSUEKEYPT = (By.ID, 'raven-test-filter-contains-text')  # not done as can't login yet


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
  
