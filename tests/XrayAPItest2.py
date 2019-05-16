'''
Created on Aug 31, 2018

@author: bmurray
'''

import logging, time, sys, os
import pytest, unittest
import requests

# setting the logging module to the console
logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(threadName)-2s) %(message)s', level=logging.INFO ,)

class XrayAPItest2(unittest.TestCase):
    
    def setUp(self):
        #set variables, load the browser
        logging.info("Function Setup()") 
        logging.info('Current Working Directory: %s' % os.getcwd())


    def tearDown(self):
        #close the browser
        logging.info("Function tearDown()")


    def test_login(self):


        testdata = {
            "testExecutionKey": "TOOL2-49",
            "info": {
                "summary": "Execution of automated tests for release v1.3",
                "user": "user31",
            },
            "tests": [
                {
                    "testKey": "TOOL2-47",
                    "comment": "Successful execution",
                    "status": "PASS"
                },
                {
                    "testKey": "TOOL1-5",
                    "comment": "Successful execution",
                    "status": "PASS"
                },
                {
                    "testKey": "TOOL1-7",
                    "comment": "Successful execution",
                    "status": "PASS"
                },
                {
                    "testKey": "TOOL1-2",
                    "comment": "Successful execution",
                    "status": "PASS"
                }
            ]
        }


        #ok, this works to set a bunch of tests to a results using the above json
        res = requests.post("https://sandbox.xpand-it.com/rest/raven/1.0/import/execution",
                           auth=('user31', 'rhtoolnext'),
                           headers={'content-type': 'application/json'},
                           json= testdata )

        print res.status_code
        print res.text


if __name__ == "__main__": # allows unittest to start by running this class file
    unittest.main()  
    
    
    