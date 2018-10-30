'''
Created on Oct 30, 2018

@author: vaibh
'''
from Model.SimulateExchange import SimulateExchange
from AppConfig import *; #@UnusedWildImport 

class SimController(object):
    '''
    classdocs
    '''
    
    logger = None;
    registeredMembers = None; ''' Key: Registered Member, Value : Object of Family Member '''
    viewObj = None;
    
    def __init__(self, logger, viewObj, registeredMembers):
        '''
        Default Constructor
        logger: (Object) The common logger object
        viewObj: (Object) The common view object
        registeredMembers: (Dictionary) The key,value pair of registered members
        '''
        self.logger = logger;
        self.registeredMembers = registeredMembers;
        self.viewObj = viewObj;
    
    def simDriver(self):
        '''
        This function is responsible for using Hat Model to calculate results.
        return: Returns the new state
        '''
        print("*********************************************");
        simulateExchange = SimulateExchange(self.logger, self.viewObj, self.registeredMembers);
        
        #magicHat = MagicHat(self.logger, self.viewObj, self.registeredMembers);
        #shuffeledMemberNames, shuffeledMembers = magicHat.shuffleMemberNames();
        results = simulateExchange.distributeGifts();
        for res in results:
            self.viewObj.displayText(res[0] + " < " + res[1]);
        return SYS_STATE_HOME;