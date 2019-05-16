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

class testrailAPIaddtc(unittest.TestCase):
    
    def setUp(self):
        #set variables, load the browser
        logging.info("Function Setup()") 
        logging.info('Current Working Directory: %s' % os.getcwd())


    def tearDown(self):
        #close the browser
        logging.info("Function tearDown()")

    def test_login(self):
        #this works, have to send enum number for autoamation type instead of 'manual'
        client = APIClient('https://toolnext.testrail.io/')
        client.user = 'bmurray@redhat.com'
        client.password = 'polarion'
        case = client.send_post(
	'add_case/1/1', { 'title': 'this 2nd test case was added via rest API using python', 'custom_automation_type': 0 })
        #pprint(case)
        #logging.info(case.get('title'))
        

if __name__ == "__main__": # allows unittest to start by running this class file
    unittest.main()  
    
    
    