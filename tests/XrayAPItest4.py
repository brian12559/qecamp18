'''
Created on May 13, 2019

@author: bmurray
'''

import logging, time, sys, os
import pytest, unittest
import requests, random

# setting the logging module to the console
logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(threadName)-2s) %(message)s', level=logging.INFO ,)

class XrayAPItest4(unittest.TestCase):
    
    def setUp(self):
        #set variables, load the browser
        logging.info("Function Setup()") 
        logging.info('Current Working Directory: %s' % os.getcwd())


    def tearDown(self):
        #close the browser
        logging.info("Function tearDown()")

    def test_login(self):

        #to use this import 3500 RHEL tests into Jira
        project_name = "TOOL1"
        test_start_id = 1
        test_end_id = 3499
        test_run_id_start = 21
        test_run_id_end = 22
        tester_id = "user27"
        tester_pw = "rhtoolnext"


        for z in range(test_run_id_start,test_run_id_end):
            myRan = round(random.random() * 10) + 1
            logging.info(myRan)

            testdata = {
                "info": {
                    "summary": "Execution of automated tests for release v1.%sx" %z,
                    "description": "This execution is automatically created when importing execution results from an external source",
                    "user": tester_id,
                }}

            mylist = []
            for x in range(1, 3500):
                y = x/myRan
                q=int(x/myRan)
                if (y-q==0):
                    mylist.append({'comment': 'Failed execution', 'status': 'FAIL', 'testKey': '%s-%s' %(project_name, x)})
                else:
                    mylist.append({'comment': 'Successful execution', 'status': 'PASS', 'testKey': '%s-%s' %(project_name, x)})

            testdata.update({'tests': mylist})
            time.sleep(2)

            res = requests.post("https://sandbox.xpand-it.com/rest/raven/1.0/import/execution",
                               auth=(tester_id, tester_pw),
                               headers={'content-type': 'application/json'},
                               json= testdata )
            #auth=('user27', 'rhtoolnext'),

            print res.status_code
            print res.text


if __name__ == "__main__": # allows unittest to start by running this class file
    unittest.main()  
    
    
    