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
            "testExecutionKey": "TOOL2-533",
            "info": {
                "summary": "Execution of automated tests for release v1.3",
                "user": "user31",
            }}

        mylist = []
        for x in range(25, 533):
            if (x in (48,49)):
                continue
            y = x/3.0
            z=int(x/3.0)
            if (y-z==0):
                mylist.append({'comment': 'Failed execution', 'status': 'FAIL', 'testKey': 'TOOL2-%s' %x})
            else:
                mylist.append({'comment': 'Successful execution', 'status': 'PASS', 'testKey': 'TOOL2-%s' % x})

        testdata.update({'tests': mylist})
        time.sleep(2)

        res = requests.post("https://sandbox.xpand-it.com/rest/raven/1.0/import/execution",
                           auth=('user31', 'rhtoolnext'),
                           headers={'content-type': 'application/json'},
                           json= testdata )

        print res.status_code
        print res.text


if __name__ == "__main__": # allows unittest to start by running this class file
    unittest.main()  
    
    
    