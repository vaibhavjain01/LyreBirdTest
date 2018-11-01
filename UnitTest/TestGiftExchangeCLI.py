'''
Created on Nov 1, 2018

@author: vaibh
'''
import unittest;
import os;
from os.path import dirname;
from Model.Logger import Logger;
from View.GiftExchangeCLI import GiftExchangeCLI;
from unittest.mock import patch;
from AppConfig import *;

class TestGiftExchangeCLI(unittest.TestCase):
    
    cliObj = None;
    langFilePath = None;
    
    def setUp(self):
        unittest.TestCase.setUp(self);
        loggerObj = Logger();
        self.langFilePath = dirname(os.getcwd()) + "\\Resources\\EnglishMessages.txt";
        self.cliObj = GiftExchangeCLI(loggerObj, self.langFilePath);
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)
    
    def testInitMessages(self):
        self.assertTrue(self.cliObj.initMessages(self.langFilePath));
        return;
    
    """
    @patch('GiftExchangeCLI.getInput', return_value=2)
    def testDispUserOpts(self):
        userOpts = [MSG_QUIT];
        self.assertNotEqual(self.cliObj.displayUserOptions(userOpts), None);
        return;
    """
    
    def testProcessMsgCode(self):
        self.assertEqual(self.cliObj.processMsgCode(MSG_QUIT), "Quit");
        return;


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()