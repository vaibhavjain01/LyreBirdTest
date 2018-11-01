'''
Created on Nov 1, 2018

@author: vaibh
'''
import unittest
from Model.Logger import Logger
from View.GiftExchangeCLI import GiftExchangeCLI
from Controller.HomeScreenController import HomeScreen
from Controller.MemberController import MemberController
import os;
from os.path import dirname;
from Model.FamilyMember import FamilyMember
from Model.Gift import Gift
from AppConfig import *;

class TestMemberController(unittest.TestCase):

    memberController = None;

    def setUp(self):
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
        return;


    def tearDown(self):
        pass


    def testHandleChoice(self):
        self.assertEqual(self.memberController.handleChoice(5), SYS_STATE_RESULTS);
        return;
        
    def testGenerateAvailableOptions(self):
        self.assertEqual(len(self.memberController.generateAvailableOptions()), 4);
        return;

    def testShowMembers(self):
        self.assertEqual(self.memberController.handleShowMembers(), SYS_STATE_MEMBER);
        return;
    
    def testCheckPreviousSaves(self):
        self.assertEqual(self.memberController.checkPreviousSaves(self.memberFilePath), len(self.memberObjs));
        return;
    
    def testGetRegisteredMembers(self):
        self.assertNotEqual(self.memberController.getRegisteredMembers(), None);

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()