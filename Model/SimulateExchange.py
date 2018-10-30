'''
Created on Oct 30, 2018

@author: vaibh
'''

import random;
from random import shuffle;
#from random import seed;
from Model.MagicHat import MagicHat
from AppConfig import *;

class SimulateExchange(object):
    '''
    classdocs
    '''
    
    logger = None;
    registeredMembers = None; ''' Key: Registered Member, Value : Object of Family Member '''
    viewObj = None;
    magicHat = None;
    distribution = None;

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
        self.distribution = [];
        self.magicHat = MagicHat(self.logger, self.viewObj, self.registeredMembers);
    
    def shuffleMemberNames(self):
        '''
        Shuffles the member names and member objects
        return: The shuffeled member names, and member objects
        '''
        # Hat
        memberNames = list(self.registeredMembers.keys());
        memberNames = (memberNames.copy());
        random.shuffle(memberNames);
        
        # Picker
        memberObjs = list(self.registeredMembers.values());
        memberObjs = memberObjs.copy();
        random.shuffle(memberObjs);
        
        return memberNames, memberObjs;
    
    def startSim(self):
        #seed(1);
        namesInHat, randomPickers = self.shuffleMemberNames();
        for picker in randomPickers:
            self.viewObj.displayText(picker.getMemberName());
            self.viewObj.displayGeneralMessage(MSG_MAKE_PICK);
            _ = self.viewObj.getInput();
            
            pickResult, receiver = self.magicHat.pickAndValidate(namesInHat, picker);
            self.viewObj.displayText("Result: " + receiver);
            if(pickResult == False):
                self.viewObj.displayGeneralMessage(MSG_FALSE_PICK_START_AGAIN);
                self.distribution = [];
                return False;
            self.distribution.append([receiver, picker.getMemberName()]);
            namesInHat.remove(receiver);
        return True;
    
    def distributeGifts(self):
        '''
        The recursive function to distribute the gifts among members following the rules.
        return: Returns the list containing gift distribution information
        '''
        while(self.startSim() != True):
            continue;
        return self.distribution;