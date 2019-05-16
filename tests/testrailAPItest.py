'''
Created on Aug 31, 2018

@author: bmurray
'''

import logging, time, sys, os
import pytest, unittest
from pylarion.work_item import TestCase
from testrail import *

# setting the logging module to the console
logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(threadName)-2s) %(message)s', level=logging.INFO ,)

class testrailAPItest(unittest.TestCase):
    
    def setUp(self):
        #set variables, load the browser
        logging.info("Function Setup()") 
        logging.info('Current Working Directory: %s' % os.getcwd())


    def tearDown(self):
        #close the browser
        logging.info("Function tearDown()")

    def test_login(self):
        #this works
        client = APIClient('https://toolnext.testrail.io/')
        client.user = 'bmurray@redhat.com'
        client.password = 'polarion'
        case = client.send_get('get_case/1')
        #pprint(case)
        logging.info(case.get('title'))
        

if __name__ == "__main__": # allows unittest to start by running this class file
    unittest.main()  
    
    
    