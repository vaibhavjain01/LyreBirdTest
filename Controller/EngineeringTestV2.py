'''
Created on Oct 30, 2018

@author: vaibh
'''
from Model.Logger import Logger;
from AppConfig import *; #@UnusedWildImport 
from Controller.HomeScreenController import HomeScreen;
from Controller.MemberController import MemberController;
from Controller.HatController import HatController;
from View.GiftExchangeCLI import GiftExchangeCLI;
from Controller.SimController import SimController

class GiftExchange(object):
    '''
    Automation of gift exchange process for Mr. Raccoon
    '''
    
    ''' Controller and Other Class Objects '''
    homeScreenController = None;
    memberController = None;
    hatController = None;
    viewObj = None;
    logger = None;
    
    ''' Internal Processing Variables '''
    state = None;
    
    def __init__(self):
        '''
        Default Constructor
        '''
        self.state = SYS_STATE_HOME;
        self.appDriver();
        
    def appDriver(self):
        '''
        The driver that runs the application
        '''
        self.initApp();
        while(True):
            if(self.state == SYS_STATE_HOME):
                self.state = self.processStateHome();
            if(self.state == SYS_STATE_MEMBER):
                self.state = self.processStateMember();
            if(self.state == SYS_STATE_RESULTS):
                self.state = self.procesStateResults();
            if(self.state == SYS_STATE_SIMULATION):
                self.state = self.processStateSimulation();
            
    def welcomeMessage(self):
        '''
        A welcome message whenever application starts
        '''
        print("*********************************************");
        self.viewObj.displayGeneralMessage(MSG_WELLCOME_MESSAGE);
        return;
    
    def processStateHome(self):
        '''
        Initiate controller for home screen
        return: The new state of system
        '''
        oprResult = self.homeScreenController.homeScreenDriver();
        if(oprResult == SYS_STATE_EXIT):
            self.viewObj.displayGeneralMessage(MSG_GOOD_BYE);
            exit();
            
        return oprResult;
    
    def processStateMember(self):
        '''
        Initiate controller for member screen
        return: The new state of system
        '''
        oprResult = self.memberController.memberDriver();
        return oprResult;
        
    def procesStateResults(self):
        '''
        Initiate controller for results calculation
        return: The new state of system
        '''
        oprResult = self.hatController.hatDriver();
        return oprResult;
    
    def processStateSimulation(self):
        oprResult = self.simController.simDriver();
        return oprResult;
    
    def initApp(self):
        '''
        This function initializes the home controller and view
        '''
        self.logger = Logger();
        self.viewObj = GiftExchangeCLI(self.logger);
        self.homeScreenController = HomeScreen(self.logger, self.viewObj);
        self.memberController = MemberController(self.logger, self.viewObj);
        self.hatController = HatController(self.logger, self.viewObj, self.memberController.getRegisteredMembers());
        self.simController = SimController(self.logger, self.viewObj, self.memberController.getRegisteredMembers());
        self.welcomeMessage();
        return;
