'''
Created on Oct 30, 2018

@author: vaibh
'''

import random;
from random import randint, seed;

class MagicHat(object):
    '''
    This class represents the magic hat with member names
    '''
    
    logger = None;
    registeredMembers = None; ''' Key: Registered Member, Value : Object of Family Member '''
    viewObj = None;
    
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
        seed(1);
    
    def shuffleMemberNames(self):
        '''
        Shuffles the member names and member objects
        return: The shuffeled member names, and member objects
        '''
        memberNames = list(self.registeredMembers.keys());
        memberNames = (memberNames.copy());
        random.shuffle(memberNames);
        memberObjs = list(self.registeredMembers.values());
        memberObjs = memberObjs.copy();
        random.shuffle(memberObjs);
        return memberNames, memberObjs;
        
    def pickFromHat(self, namesInHat):
        if(len(namesInHat) == 0):
            return None;
        pickedNameIndex = randint(0, len(namesInHat) - 1);
        return pickedNameIndex;
        
    def validatePick(self, picker, pickedName):
        if(picker.getMemberName() == pickedName):
            return False;
        if(picker.getPartners() == None):
            return True;
        if(pickedName in picker.getPartners()):
            return False;
        return True;
        
    def pickAndValidate(self, namesInHat, randomPicker):
        pickedNameIndex = self.pickFromHat(namesInHat);
        if(pickedNameIndex == None):
            return None;
        
        result = self.validatePick(randomPicker, namesInHat[pickedNameIndex]);
        return result, namesInHat[pickedNameIndex];
        
        
    def distributeGifts(self, shuffeledMemberNames, shuffeledMembers):
        '''
        The recursive function to distribute the gifts among members following the rules.
        shuffeledMemberNames: (List) The names of all members shuffled
        shuffeledMembers: (List) The familyMember objects of all members shuffeled
        return: Returns the list containing gift distribution information
        '''
        if(len(shuffeledMembers) <= 0):
            return self.distribution;
        memberRepick = [];
        
        ctrOne = 0;
        ctrTwo = 0;
        
        while(ctrOne < len(shuffeledMemberNames)) and (ctrTwo < len(shuffeledMembers)):
        #for ctrOne, ctrTwo in zip(range(len(shuffeledMemberNames)), range(len(shuffeledMembers))):
            receiver = shuffeledMemberNames[ctrOne];
            picker = shuffeledMembers[ctrTwo].getMemberName();
            
            res = self.validatePick(shuffeledMembers[ctrTwo], receiver);
            if(res == False):
                memberRepick.append(shuffeledMembers[ctrTwo]);
                ctrTwo += 1;
            else:
                self.distribution.append([picker, receiver]);
                ctrOne += 1;
                ctrTwo += 1;
        
        if(len(memberRepick) == len(shuffeledMembers)):
            return None;
        
        if(self.distributeGifts(shuffeledMemberNames[ctrOne:], memberRepick) == None):
            return None;
        
        return self.distribution;