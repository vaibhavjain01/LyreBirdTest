'''
Created on Oct 30, 2018

@author: vaibh
'''
import random;
from AppConfig import *; #@UnusedWildImport 
from Model.MagicHat import MagicHat

class HatController(object):
    '''
    This class implements the magic hat's driver and functionality
    '''

    logger = None;
    registeredMembers = None; ''' Key: Registered Member, Value : Object of Family Member '''
    viewObj = None;
    
    shuffeledMemberNames = [];
    
    def __init__(self, logger, viewObj, registeredMembers):
        '''
        Default Constructor
        '''
        self.logger = logger;
        self.registeredMembers = registeredMembers;
        self.viewObj = viewObj;
    
    def hatDriver(self):
        print("*********************************************");
        magicHat = MagicHat(self.logger, self.viewObj, self.registeredMembers);
        shuffeledMemberNames, shuffeledMembers = magicHat.shuffleMemberNames();
        results = magicHat.distributeGifts(shuffeledMemberNames, shuffeledMembers);
        if(results == None):
            self.viewObj.displayGeneralMessage(MSG_GIFT_EXCHANGE_NOT_POSSIBLE);
        else:
            for res in results:
                self.viewObj.displayText(res[0] + " < " + res[1]);
        return SYS_STATE_HOME;
    
    