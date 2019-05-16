'''
Created on Aug 31, 2018

@author: bmurray
'''

import logging, time, sys, os
import pytest, unittest
import requests

# setting the logging module to the console
logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(threadName)-2s) %(message)s', level=logging.INFO ,)

class codeBeamerAPItest(unittest.TestCase):
    
    def setUp(self):
        #set variables, load the browser
        logging.info("Function Setup()") 
        logging.info('Current Working Directory: %s' % os.getcwd())


    def tearDown(self):
        #close the browser
        logging.info("Function tearDown()")

    def test_login(self):

        #ok, it looks like I can auth
        res = requests.get("https://saas.codebeamer.com/api/v2/project/6628",
             auth = ('bmurray125', 'rhtoolnext'))
             #headers = ('accept: application/json'))

        print res.status_code
        print res.text


        # ok, it looks like I can get test run info
        res = requests.get("https://saas.codebeamer.com/api/v2/item/1816459",
                           auth=('bmurray125', 'rhtoolnext'))
        # headers = ('accept: application/json'))

        print res.status_code
        print res.text

        # # ok, it looks like I can get user info
        # res = requests.get("https://saas.codebeamer.com/api/v2/user/findByName?name=bmurray125",
        #                    auth=('bmurray125', 'rhtoolnext'))
        # # headers = ('accept: application/json'))
        #
        # print res.status_code
        # print res.text

        # ok, it looks like I can get test run info
        res = requests.get("https://saas.codebeamer.com/api/v2/item/1816460",
                           auth=('bmurray125', 'rhtoolnext'))
        # headers = ('accept: application/json'))

        print res.status_code
        print res.text



if __name__ == "__main__": # allows unittest to start by running this class file
    unittest.main()  
    
    
    