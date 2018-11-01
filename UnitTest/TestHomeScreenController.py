'''
Created on Nov 1, 2018

@author: vaibh
'''
import unittest
from Model.Gift import Gift
from Model.Logger import Logger
from Controller.EngineeringTestV2 import GiftExchange
from View.GiftExchangeCLI import GiftExchangeCLI
from Controller.HomeScreenController import HomeScreen
import os;
from os.path import dirname;
from AppConfig import *;

class TesHomeScreenController(unittest.TestCase):

    homeScreenController = None;
    
    def setUp(self):
        unittest.TestCase.setUp(self);
        
        self.logger = Logger();
        self.langFilePath = dirname(os.getcwd()) + "\\Resources\\EnglishMessages.txt";
        self.viewObj = GiftExchangeCLI(self.logger, self.langFilePath);
        self.homeScreenController = HomeScreen(self.logger, self.viewObj);
    
    def testHandleSimulation(self):
        self.assertEqual(self.homeScreenController.handleSimulation(), SYS_STATE_SIMULATION);
        return;
    
    def testHandleManageMembers(self):
        self.assertEqual(self.homeScreenController.handleManageMembers(), SYS_STATE_MEMBER);
        return;

    def testHandleShowResults(self):
        self.assertEqual(self.homeScreenController.handleShowResults(), SYS_STATE_RESULTS);
        return;
        
    def testHandleChoice(self):
        self.assertEqual(self.homeScreenController.handleChoice(SYS_STATE_EXIT), SYS_STATE_EXIT);
        return;
        
    def testGenerateAvailableOptions(self):
        self.assertEqual(len(self.homeScreenController.generateAvailableOptions()), 4);
        return;

    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()