'''
Created on Oct 30, 2018

@author: vaibh
'''
from AppConfig import *; #@UnusedWildImport 
from pathlib import Path;

class GiftExchangeCLI(object):
    '''
    This class implements user interactions for gift exchange application
    '''
    
    logger = None;
    messageDict = None;

    def __init__(self, logger):
        '''
        Default Constructor
        '''
        self.logger = logger;
        self.initMessages();
    
    def initMessages(self):
        self.messageDict = {};
        
        fileContent = None;
        # TBD: File Validation
        if(Path(APP_LANGUAGE_FILE).exists()):
            with open(APP_LANGUAGE_FILE) as f:
                fileContent = f.readlines();
        
        for line in fileContent:
            tokens = line.split("=");
            self.messageDict[int(tokens[0])] = tokens[1];
    
    def displayUserOptions(self, userOptions):
        '''
        This function displays the available options to the user
        userOptions: (list of str) available user options
        returns: (int) the user's choice
        '''
        print("*********************************************");
        for ctr in range(len(userOptions)):
            print(str(ctr + 1) + ")", self.processMsgCode(userOptions[ctr]));
            
        return self.getUserChoice(len(userOptions));
    
    def processMsgCode(self, msgCode):
        return self.messageDict[msgCode].replace("\n","");
    
    def displayGeneralMessage(self, message):
        '''
        This function displays the general message intended for user
        message: (str) the message
        '''
        print(self.processMsgCode(message));
        return;
    
    def displayText(self, text):
        print(text);
        return;
    
    def getUserChoice(self, maxChoice):
        '''
        This function gets the user choice, and sends it back to controller for processing
        maxChoice: (int) the maximum possible user choice
        return: (int) the user choice
        '''    
        choice = self.getInput();
        if((choice.isdigit() == False) or 
           (int(choice) > maxChoice) or 
           ((int(choice) < 1))):
            self.logger.TRACE(LOG_LEVEL_CRITICAL, "Please enter a numerical value ranging between available options.", self);
            return BAD_CHOICE;
        else:
            return int(choice);
    
    def getMessagedInput(self, message):
        self.displayGeneralMessage(message);
        return self.getInput();
    
    def getInput(self):
        userInput = input('> ');
        return userInput;
        
    def log(self, logData):
        '''
        This function called by logger to push log to view
        logData: (str) The log data.
        '''
        print(self.processMsgCode(logData));