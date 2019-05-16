'''
Created on Aug 31, 2018

@author: bmurray
'''

import logging, time, sys, os
import pytest, unittest
import requests, json

# setting the logging module to the console
logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(threadName)-2s) %(message)s', level=logging.INFO ,)

class XrayAPItest5(unittest.TestCase):
    
    def setUp(self):
        #set variables, load the browser
        logging.info("Function Setup()") 
        logging.info('Current Working Directory: %s' % os.getcwd())


    def tearDown(self):
        #close the browser
        logging.info("Function tearDown()")

    def test_login(self):

        #ok, this works...note different url for xray stuff
        #this gets the list of tests in the Test Execution
        res = requests.get("https://sandbox.xpand-it.com/rest/raven/1.0/api/testexec/TOOL3-3518/test",
                           auth=('user31', 'rhtoolnext'))
        print res.status_code
        print res.text

        #returns list of tests in the test execution
        todos = json.loads(res.text)
        #print todos [1]

        testdata = {
            "testExecutionKey": "TOOL3-3518",
            "info": {
                "summary": "Execution of automated tests for release v23.x",
                "user": "user31",
            }}

        mylist = []

        for x in todos:
            print x["key"]
            mylist.append({'comment': 'Successful execution', 'status': 'PASS', 'testKey': '%s' % x["key"]})

        testdata.update({'tests': mylist})
        time.sleep(2)

        res = requests.post("https://sandbox.xpand-it.com/rest/raven/1.0/import/execution",
                            auth=('user31', 'rhtoolnext'),
                            headers={'content-type': 'application/json'},
                            json=testdata)

        print res.status_code
        print res.text

    def qtest_login(self):

        #ok, it looks like I can auth
        #this works
        res = requests.get("https://sandbox.xpand-it.com/rest/api/2/issue/TOOL2-47",
             auth = ('user31', 'rhtoolnext'))

        print res.status_code
        print res.text

        #ok, this works...note different url for xray stuff
        #this gets the list of tests in the Test Execution
        res = requests.get("https://sandbox.xpand-it.com/rest/raven/1.0/api/testexec/TOOL2-49/test",
                           auth=('user31', 'rhtoolnext'))

        print res.status_code
        print res.text

        #this gets the test result for the test case in the test exec
        res = requests.get("https://sandbox.xpand-it.com/rest/raven/1.0/api/testrun?testExecIssueKey=TOOL2-49&testIssueKey=TOOL2-47",
                           auth=('user31', 'rhtoolnext'))

        print res.status_code
        print res.text

        #this does the same as above but using the test run ID
        res = requests.get("https://sandbox.xpand-it.com/rest/raven/1.0/api/testrun/4200",
                           auth=('user31', 'rhtoolnext'))

        print res.status_code
        print res.text

        testdata = {
            "status": "FAIL",
        }

        #ok, this works to set a test result to PASS
        #this does the same as above but using the test run ID
        res = requests.put("https://sandbox.xpand-it.com/rest/raven/1.0/api/testrun/4200",
                           auth=('user31', 'rhtoolnext'),
                           headers={'content-type': 'application/json'},
                           json= testdata )

        print res.status_code
        print res.text


if __name__ == "__main__": # allows unittest to start by running this class file
    unittest.main()  
    
    
    