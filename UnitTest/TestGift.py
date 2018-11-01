'''
Created on Nov 1, 2018

@author: vaibh
'''
import unittest
from Model.Gift import Gift


class TestGift(unittest.TestCase):

    giftObj = None;
    
    def setUp(self):
        unittest.TestCase.setUp(self);
        self.giftObj = Gift("testmember");
    
    def testGetBroughtBy(self):
        self.assertEqual(self.giftObj.getBroughtBy(), "testmember");
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()