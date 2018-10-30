'''
Created on Oct 30, 2018

@author: vaibh
'''
from AppConfig import *; #@UnusedWildImport 

class HomeScreen(object):
    '''
    This class implements home screen and related event handlers
    '''
    logger = None;
    viewObj = None;
    
    def __init__(self, logger, viewObj):
        '''
        Default Constructor
        logger: (Object) The common logger object
        viewObj: (Object) The common view object
        '''
        self.logger = logger;
        self.viewObj = viewObj;
        
    def homeScreenDriver(self):
        '''
        This function is responsible for generating the options that user needs to choose
        return: Returns the new state
        '''
        userOptions = self.generateAvailableOptions();
        choice = self.viewObj.displayUserOptions(userOptions);
        oprResult = self.handleChoice(choice);
        return oprResult;
        
    def generateAvailableOptions(self):
        '''
        Generates all possible user interaction options for view
        return: The generated list containing user options
        '''
        userOptions = [];
        userOptions.append(MSG_MANAGE_MEMBERS);
        userOptions.append(MSG_SHOW_RESULTS);
        userOptions.append(MSG_QUIT);
        return userOptions;
    
    def handleChoice(self, choice):
        '''
        This function handles the user choice
        choice: (int) User's choice
        return: (int) The new system state
        '''
        if(choice == 1): return self.handleManageMembers();
        elif(choice == 2): return self.handleShowResults();
        elif(choice == 3): return SYS_STATE_EXIT;
    
    def handleManageMembers(self):
        '''
        return: Returns the new state
        '''
        return SYS_STATE_MEMBER;
    
    def handleShowResults(self):
        '''
        return: Returns the new state
        '''
        return SYS_STATE_RESULTS;