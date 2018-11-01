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
        
    def getMemberName(self):
        '''
        Getter function to get the member name
        return: (str) The member name
        '''
        return self.memberName;
    
    def getPartners(self):
        '''
        Getter function to retrieve the list of partners
        return: (List) List of all partners of this member
        '''
        return self.memberPartners;