'''
Created on Aug 31, 2018

@author: bmurray
'''

import logging, time, sys, os
import pytest, unittest
import requests

# setting the logging module to the console
logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(threadName)-2s) %(message)s', level=logging.INFO ,)

class ptAPItest(unittest.TestCase):
    
    def setUp(self):
        #set variables, load the browser
        logging.info("Function Setup()") 
        logging.info('Current Working Directory: %s' % os.getcwd())


    def tearDown(self):
        #close the browser
        logging.info("Function tearDown()")

    def test_login(self):
        # curl -H "Content-Type: application/json" \
        #     -u user@pt.com:dd2d9ddee2e9cd4861b1f0353375de1b4444d49  \
        #    https://api.practitest.com/api/v2/projects.json

        import httplib
        import requests
        from requests.auth import AuthBase
        #works
        res = requests.get('https://api.practitest.com/api/v2/projects.json',
                           auth=('bmurray@redhat.com', '563aff227865af92545a7ffbe8a4b7a8c606702b'))
        print res.status_code
        print res.text

        #hmmm this doesnt work
        #res = requests.get('https://api.practitest.com/api/v2/projects/New48570/tests.json',
                           #auth=('bmurray@redhat.com', '563aff227865af92545a7ffbe8a4b7a8c606702b'))
        #works
        res = requests.get('https://api.practitest.com/api/v2/users.json',
                           auth=('bmurray@redhat.com', '563aff227865af92545a7ffbe8a4b7a8c606702b'))

        print res.status_code
        print res.text

        #res = requests.get('https://api.practitest.com/api/v2/projects/11836/tests.json',
                           #auth=('bmurray@redhat.com', '563aff227865af92545a7ffbe8a4b7a8c606702b'))
       # print res.status_code
        #print res.text

        res = requests.get('https://api.practitest.com/api/v2/projects/11836/runs.json',
                           auth=('bmurray@redhat.com', '563aff227865af92545a7ffbe8a4b7a8c606702b'))

        print res.status_code
        print res.text

        res = requests.get('https://api.practitest.com/api/v2/projects/11836/tests/1894737.json',
            auth=('bmurray@redhat.com', '563aff227865af92545a7ffbe8a4b7a8c606702b'))
        print res.status_code
        print res.text



if __name__ == "__main__": # allows unittest to start by running this class file
    unittest.main()  
    
    
    