'''
Created on Nov 1, 2018

@author: vaibh
'''
import unittest
from Model.Logger import Logger
from View.GiftExchangeCLI import GiftExchangeCLI
from Controller.HomeScreenController import HomeScreen
from Controller.MemberController import MemberController
from Controller.HatController import HatController
import os;
from os.path import dirname;
from Model.FamilyMember import FamilyMember
from Model.Gift import Gift
from AppConfig import *;

class TestHatController(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self);
        self.langFilePath = dirname(os.getcwd()) + "\\Resources\\EnglishMessages.txt";
        self.memberFilePath = dirname(os.getcwd()) + "\\Resources\\testMemberList.txt";
        self.memberObjs = [FamilyMember("testMemOne", None, Gift("testMemOne")), 
                      FamilyMember("testMemTwo", None, Gift("testMemTwo"))]
        self.namesInHat = ["vj","a"];
        
        f = open(self.memberFilePath, "w");
        f.write("vj\na");
        f.close();
        
        self.logger = Logger();
        self.viewObj = GiftExchangeCLI(self.logger, self.langFilePath);
        self.homeScreenController = HomeScreen(self.logger, self.viewObj);
        self.memberController = MemberController(self.logger, self.viewObj, self.memberFilePath);
        self.hatController = HatController(self.logger, self.viewObj, self.memberController.getRegisteredMembers());

    def testHatDriver(self):
        self.assertEqual(self.hatController.hatDriver(), SYS_STATE_HOME);
        return;


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()