'''
Created on Oct 30, 2018

@author: vaibh
'''
import unittest
from View.GiftExchangeCLI import GiftExchangeCLI
from Model.Logger import Logger
import os;

class TestGiftExchangeCLI(unittest.TestCase):

    testViewObj = None;

    def setUp(self):
        self.logger = Logger();
        
        self.f = open("tmp.txt", 'w')
        fileContent = "1=Good Bye!\n2=Manage Members";
        self.f.write(fileContent);
        self.f.close();
        
        self.testViewObj = GiftExchangeCLI(self.logger, "tmp.txt");
        return;

    def tearDown(self):
        os.remove("tmp.txt");
        unittest.TestCase.tearDown(self)

    def testInitMessages(self):
        self.assertEqual(self.testViewObj.getLinesFromFile(self.f), True);
        return;


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()