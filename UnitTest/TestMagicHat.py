'''
Created on Nov 1, 2018

@author: vaibh
'''
import unittest
from Model.Logger import Logger
from View.GiftExchangeCLI import GiftExchangeCLI
from Controller.MemberController import MemberController
from Controller.HatController import HatController
import os;
from os.path import dirname;
from Model.MagicHat import MagicHat
from Model.FamilyMember import FamilyMember
from Model.Gift import Gift

class TestMagicHat(unittest.TestCase):

    magicHatObj = None;
    namesInHat = None;
    memberObjs = None;
    
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
        self.memberController = MemberController(self.logger, self.viewObj, self.memberFilePath);
        self.magicHatObj = MagicHat(self.logger, self.viewObj, self.memberController.getRegisteredMembers());
        
    def testShuffleMemberNames(self):
        memberNames, memberObjs = self.magicHatObj.shuffleMemberNames();
        self.assertNotEqual(memberNames, None);
        self.assertNotEqual(memberObjs, None);
        self.assertEqual(len(memberNames), 2);
        self.assertEqual(len(memberObjs), 2);
        pass

    def testPickFromHat(self):
        idx = self.magicHatObj.pickFromHat(self.namesInHat);
        self.assertLessEqual(idx, len(self.namesInHat));
        return;
        
    def testPickAndValidate(self):
        res, name = self.magicHatObj.pickAndValidate(self.namesInHat[1], self.memberObjs[0]);
        self.assertEqual(res, True);
        self.assertEqual(name, 'a');
        return;
        
    def testDistributeGifts(self):
        resDistribution = self.magicHatObj.distributeGifts(self.namesInHat, self.memberObjs);
        self.assertEqual(len(resDistribution), 2);
        return;
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()