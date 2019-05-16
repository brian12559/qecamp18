'''
Created on Aug 31, 2018

@author: bmurray
'''

import logging, time, sys, os
import pytest, unittest
import requests

# setting the logging module to the console
logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(threadName)-2s) %(message)s', level=logging.INFO ,)

class spiraTestAPItest(unittest.TestCase):
    
    def setUp(self):
        #set variables, load the browser
        logging.info("Function Setup()") 
        logging.info('Current Working Directory: %s' % os.getcwd())


    def tearDown(self):
        #close the browser
        logging.info("Function tearDown()")

    def test_login(self):
        #token for spira {5F663F9F-0F74-40C5-8A00-3AAED22D3A36}
        #this works
        #our url is https://demo.spiraservice.net/rhtoolnext/5/MyProfile.aspx
        res = requests.get('https://demo.spiraservice.net/rhtoolnext/Services/v5_0/RestService.svc/projects?administrator&{5F663F9F-0F74-40C5-8A00-3AAED22D3A36}')
        print res.status_code
        print res.text



if __name__ == "__main__": # allows unittest to start by running this class file
    unittest.main()  
    
    
    