'''
Created on Nov 1, 2018

@author: vaibh
'''
import unittest
from Model.FamilyMember import FamilyMember
from Model.Gift import Gift


class TestFamilyMember(unittest.TestCase):

    familyMemberObj = None;
    
    def setUp(self):
        unittest.TestCase.setUp(self);
        testGift = Gift("memberOne");
        self.familyMemberObj = FamilyMember("memberOne", ["partner1","partner2"], testGift);
        
    def testGetMemberName(self):
        memberName = self.familyMemberObj.getMemberName();
        self.assertEqual(memberName, "memberOne");
        return;
    
    def testGetMemberPartners(self):
        partners = self.familyMemberObj.getPartners();
        self.assertIn("partner1", partners);


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()