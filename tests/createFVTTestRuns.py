'''
Created on Jan 10, 2019

@author: bmurray
'''

import logging, time, sys, os
import pytest, unittest, datetime
from pylarion.work_item import TestCase
from pylarion.test_record import TestRecord
from pylarion.test_run import TestRun

# setting the logging module to the console
logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(threadName)-2s) %(message)s', level=logging.INFO, )


class createFVTTestRun(unittest.TestCase):

    def setUp(self):
        # set variables, load the browser
        logging.info("Function Setup()")
        logging.info('Current Working Directory: %s' % os.getcwd())
        self.polarion_project = 'Polarion'



    def tearDown(self):
        # close the browser
        logging.info("Function tearDown()")

    def test_createTR(self):
        this_id = "POLA-2019-01-10"
        this_title = "Stage, Pol 18.2, Imp2.0.23"
        trsATs = ['TestCaseE_Accept', 'TestCaseI_Accept', 'ResI_Accept', 'ReqI_Accept']
        trsFVTs = ['TestCaseI_Regress', 'ResI_Regress', 'ReqI_Regress']
        logging.info("Creating Test Runs")

        for x in trsFVTs:
            logging.info("Creating Test Run-> %s" % x)
            tr = TestRun.create(self.polarion_project, this_id, x, this_title)
            time.sleep(3)
            for record in tr.records:
                logging.info("setting %s result to passed" % record.test_case_id)
                tr.update_test_record_by_fields(record.test_case_id, test_result="passed", test_comment="OK", executed_by="bmurray",  executed=datetime.datetime.now(), duration=0.50)
            tr.update


            #tc = TestCase(project_id=self.polarion_project, work_item_id=self.testcase)
        #logging.info(tc.description)


if __name__ == "__main__":  # allows unittest to start by running this class file
    unittest.main()


