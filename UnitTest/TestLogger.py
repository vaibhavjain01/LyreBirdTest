'''
Created on Oct 30, 2018

@author: vaibh
'''
import unittest
from Model.Logger import Logger
from AppConfig import LOG_LEVEL_CRITICAL


class TestLogger(unittest.TestCase):

    testLoggerObj = None;
    
    def setUp(self):
        self.testLoggerObj = Logger();
        pass

    def testTrace(self):
        self.assertEqual(self.testLoggerObj.TRACE(LOG_LEVEL_CRITICAL, "Test Case Passed"), True);
        return;


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()