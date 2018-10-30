'''
Created on Oct 30, 2018

@author: vaibh
'''
import random;
from AppConfig import *; #@UnusedWildImport 

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
        shuffeledMemberNames, shuffeledMembers = self.shuffleMemberNames();
        self.distributeGifts(shuffeledMemberNames, shuffeledMembers);
        
        return SYS_STATE_HOME;
    
    def shuffleMemberNames(self):
        memberNames = list(self.registeredMembers.keys());
        memberNames = (memberNames.copy());
        random.shuffle(memberNames);
        memberObjs = list(self.registeredMembers.values());
        memberObjs = memberObjs.copy();
        random.shuffle(memberObjs);
        return memberNames, memberObjs;
            
    def distributeGifts(self, shuffeledMemberNames, shuffeledMembers):
        if(len(shuffeledMembers) <= 0):
            return;
        memberRepick = [];
        
        ctrOne = 0;
        ctrTwo = 0;
        
        while(ctrOne < len(shuffeledMemberNames)) and (ctrTwo < len(shuffeledMembers)):
        #for ctrOne, ctrTwo in zip(range(len(shuffeledMemberNames)), range(len(shuffeledMembers))):
            giver = shuffeledMemberNames[ctrOne];
            picker = shuffeledMembers[ctrTwo].getMemberName();
            pickerPartners = shuffeledMembers[ctrTwo].getPartners();
            
            if((picker == giver) or 
               ((pickerPartners != None) and (giver in pickerPartners))):
                memberRepick.append(shuffeledMembers[ctrTwo]);
                ctrTwo += 1;
            else:
                self.viewObj.displayText(picker + " << " + giver);
                ctrOne += 1;
                ctrTwo += 1;
        
        self.distributeGifts(shuffeledMemberNames[ctrOne:], memberRepick);
        return;