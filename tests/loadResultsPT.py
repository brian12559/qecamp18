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
        import json

        #OK, this works...so loop on from 966-3597, doing twenty at a time
        #limited to 30 minute

        #for x in range(1,3597,20):
        for x in range(1, 600, 20):

            data_json = json.dumps(
                {'data': [{'type': 'instances', 'attributes': {'instance-id': 15210963 + x,
                             'exit-code': 1, 'automated-execution-output': 'my output'}},
                           {'type': 'instances', 'attributes': {'instance-id': 15210963 + x + 1,
                            'exit-code': 0, 'automated-execution-output': 'my output'}},
                           {'type': 'instances', 'attributes': {'instance-id': 15210963 + x + 2,
                            'exit-code': 0, 'automated-execution-output': 'my output'}},
                           {'type': 'instances', 'attributes': {'instance-id': 15210963 + x + 3,
                            'exit-code': 1, 'automated-execution-output': 'my output'}},
                           {'type': 'instances', 'attributes': {'instance-id': 15210963 + x + 4,
                             'exit-code': 0, 'automated-execution-output': 'my output'}},
                           {'type': 'instances', 'attributes': {'instance-id': 15210963 + x + 5,
                            'exit-code': 0, 'automated-execution-output': 'my output'}},
                           {'type': 'instances', 'attributes': {'instance-id': 15210963 + x + 6,
                            'exit-code': 0, 'automated-execution-output': 'my output'}},
                           {'type': 'instances', 'attributes': {'instance-id': 15210963 + x + 7,
                            'exit-code': 0, 'automated-execution-output': 'my output'}},
                           {'type': 'instances', 'attributes': {'instance-id': 15210963 + x + 8,
                            'exit-code': 0, 'automated-execution-output': 'my output'}},
                           {'type': 'instances', 'attributes': {'instance-id': 15210963 + x + 9,
                             'exit-code': 0, 'automated-execution-output': 'my output'}},
                           {'type': 'instances', 'attributes': {'instance-id': 15210963 + x + 10,
                             'exit-code': 1,'automated-execution-output': 'my output'}},
                           {'type': 'instances', 'attributes': {'instance-id': 15210963 + x + 11,
                             'exit-code': 0, 'automated-execution-output': 'my output'}},
                           {'type': 'instances', 'attributes': {'instance-id': 15210963 + x + 12,
                             'exit-code': 0, 'automated-execution-output': 'my output'}},
                           {'type': 'instances', 'attributes': {'instance-id': 15210963 + x + 13,
                             'exit-code': 0, 'automated-execution-output': 'my output'}},
                           {'type': 'instances', 'attributes': {'instance-id': 15210963 + x + 14,
                             'exit-code': 1, 'automated-execution-output': 'my output'}},
                           {'type': 'instances', 'attributes': {'instance-id': 15210963 + x + 15,
                             'exit-code': 0, 'automated-execution-output': 'my output'}},
                           {'type': 'instances', 'attributes': {'instance-id': 15210963 + x + 16,
                             'exit-code': 0, 'automated-execution-output': 'my output'}},
                           {'type': 'instances', 'attributes': {'instance-id': 15210963 + x + 17,
                              'exit-code': 0, 'automated-execution-output': 'my output'}},
                           {'type': 'instances', 'attributes': {'instance-id': 15210963 + x + 18,
                               'exit-code': 1, 'automated-execution-output': 'my output'}},
                           {'type': 'instances', 'attributes': {'instance-id': 15210963 + x + 19,
                              'exit-code': 0,'automated-execution-output': 'my output'}}
                          ]
                 })

            r = requests.post("https://api.practitest.com/api/v2/projects/11836/runs.json",
                              data=data_json,
                              auth=('bmurray@redhat.com', '563aff227865af92545a7ffbe8a4b7a8c606702b'),
                              headers={'Content-type': 'application/json'})

            print r.status_code
            print r.text

            #time.sleep(1)



if __name__ == "__main__": # allows unittest to start by running this class file
    unittest.main()  
    
    
    