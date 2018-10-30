'''
Created on Oct 30, 2018

@author: vaibh
'''

class FamilyMember(object):
    '''
    This class represents a family member of Raccoons
    '''

    memberName = None;
    memberPartners = None;
    giftBroughtByMember = None;

    def __init__(self, memberName, memberPartners, giftBroughtByMember):
        '''
        Default Constructor
        memberName: (String) The new member's name
        memberPartners: (List of String) The list of member's partners 
        giftBroughtByMember: (Object of class Gift) The gift brought by member
        '''
        self.memberName = memberName;
        self.memberPartners = memberPartners;
        self.giftBroughtByMember = giftBroughtByMember;
        
    def modifyMemberName(self, newName):
        if(self.validateNewName == True):
            self.memberName = newName;
        else:
            return False;
        return True;
            
    def validateNewName(self, newName):
        if(len(newName > 1)):
            return True;
        else:
            return False;
        
    def getMemberName(self):
        return self.memberName;
    
    def getPartners(self):
        return self.memberPartners;