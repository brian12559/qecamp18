'''
Created on Aug 31, 2018

@author: bmurray
'''

import logging, time, sys, os
import pytest, unittest
import requests

# setting the logging module to the console
logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(threadName)-2s) %(message)s', level=logging.INFO ,)

class testlabAPItest(unittest.TestCase):
    
    def setUp(self):
        #set variables, load the browser
        logging.info("Function Setup()") 
        logging.info('Current Working Directory: %s' % os.getcwd())


    def tearDown(self):
        #close the browser
        logging.info("Function tearDown()")

    def test_login(self):
        #this works
        company = 'ToolNext'
        apiKey = '550e8400-e29b-41d4-a716-44665544'
        restAdd= "https://rhtoolnext.melioratestlab.com/api/defect/ToolNext"
        requests.get(restAdd, auth=('user', '550e8400-e29b-41d4-a716-44665544'))
        #works to get all test cases in project=TLABTMPL
        res = requests.get('https://rhtoolnext.melioratestlab.com/api/testcase/TLABTMPL',
                           auth=('user', '550e8400-e29b-41d4-a716-44665544'))
        print res.status_code
        print res.text

       #works to get the single test case data
        res = requests.get('https://rhtoolnext.melioratestlab.com/api/testcase/TLABTMPL/227091',
                           auth=('user', '550e8400-e29b-41d4-a716-44665544'))
        print res.status_code
        print res.text

        

if __name__ == "__main__": # allows unittest to start by running this class file
    unittest.main()  
    
    
    