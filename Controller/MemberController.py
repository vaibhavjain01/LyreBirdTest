'''
Created on Oct 30, 2018

@author: vaibh
'''

from AppConfig import *; #@UnusedWildImport 
from Model.FamilyMember import FamilyMember
from Model.Common import Common
from Model.Gift import Gift
from pathlib import Path
import os;

class MemberController(object):
    '''
    This class implements member controller functions
    '''

    logger = None;
    registeredMembers = None; ''' Key: Registered Member, Value : Object of Family Member '''
    viewObj = None;
    commonObj = None;
    
    def __init__(self, logger, viewObj):
        '''
        Default Constructor
        '''
        self.logger = logger;
        self.registeredMembers = {};
        self.viewObj = viewObj;
        self.commonObj = Common;
        self.checkPreviousSaves();
    
    def memberDriver(self):
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
        userOptions.append(MSG_SHOW_MEMBERS);
        userOptions.append(MSG_ADD_MEMBER);
        userOptions.append(MSG_REMOVE_MEMBER);
        userOptions.append(MSG_GO_BACK);
        return userOptions;
    
    def handleChoice(self, choice):
        '''
        This function handles the user choice
        choice: (int) User's choice
        return: (int) The new system state
        '''
        if(choice == 1): return self.handleShowMembers();
        elif(choice == 2): return self.handleAddMember();
        elif(choice == 3): return self.handleRemoveMember();
        elif(choice == 4): return SYS_STATE_HOME;
        elif(choice == 5): return SYS_STATE_RESULTS;
    
    def handleShowMembers(self):
        print("*********************************************");
        for _, member in self.registeredMembers.items():
            mName = member.getMemberName(); 
            mName = mName.replace("\n","");
            mPartners = member.getPartners();
            if(mPartners != None):
                mName += " :: "
                ctr = 0;
                for partner in mPartners:
                    if(ctr != (len(mPartners) - 1)):
                        mName += partner + ", ";
                    else:
                        partner = partner.replace("\n","");
                        mName += partner; 
                    ctr += 1;
            self.viewObj.displayText(mName);
            
        return SYS_STATE_MEMBER;
    
    def handleAddMember(self):
        newMemberName, newMemberPartnersStr = self.getNewMemberDetails();
        self.addMemberToDict(newMemberName, newMemberPartnersStr);
        self.addMemberToFile(newMemberName, newMemberPartnersStr);
        self.viewObj.displayGeneralMessage(MSG_MEMBER_ADDED);
        return SYS_STATE_MEMBER;
    
    def getNewMemberDetails(self):
        newMemberName = self.viewObj.getMessagedInput(MSG_ENTER_MEMBER_NAME);
        newMemberPartnersStr = self.viewObj.getMessagedInput(MSG_ENTER_MEMBER_PARTNERS);
        return newMemberName, newMemberPartnersStr;
    
    def addMemberToDict(self, newMemberName, newMemberPartnersStr = None):
        newMemberName = newMemberName.replace("\n","");
        if(newMemberPartnersStr != None):
            newMemberPartnersStr = newMemberPartnersStr.replace("\n","");
            newMemberPartners = newMemberPartnersStr.split(","); #self.commonObj.commaSepStrToList(newMemberPartnersStr);
        else:
            newMemberPartners = None;
            
        newMemberGift = Gift(newMemberName);
        newMember = FamilyMember(newMemberName, newMemberPartners, newMemberGift);
        self.registeredMembers[newMemberName] = newMember;
        
    def addMemberToFile(self, newMemberName, newMemberPartnersStr = None):
        f= open(SAVED_MEMBER_FILE,"a+");
        if(os.path.getsize(SAVED_MEMBER_FILE) > 2):
            f.write("\n");
        f.write(newMemberName + "=" + newMemberPartnersStr);
        f.close();
        
    def handleRemoveMember(self):
        memberToRemove = self.viewObj.getMessagedInput(MSG_ENTER_MEMBER_NAME);
        if(memberToRemove in self.registeredMembers):
            self.registeredMembers.pop(memberToRemove);
            self.viewObj.displayGeneralMessage(MSG_MEMBER_REMOVED);
            self.updateFileAfterDelete();
        else:
            self.logger.TRACE(LOG_LEVEL_CRITICAL, MSG_MEMBER_NOT_FOUND, self.viewObj);
        return SYS_STATE_MEMBER;
    
    def updateFileAfterDelete(self):
        os.remove(SAVED_MEMBER_FILE);
        for _, member in self.registeredMembers.items():
            partners = "";
            ctr = 0;
            if(member.getPartners() != None):
                for partner in member.getPartners():
                    partners += partner;
                    if(ctr != (len(member.getPartners()) - 1)):
                        partners += ",";
            
            self.addMemberToFile(member.getMemberName(), partners);
    
    def getRegisteredMembers(self):
        return self.registeredMembers;
    
    def checkPreviousSaves(self):
        fileContent = None;
        # TBD: File Validation
        if(Path(SAVED_MEMBER_FILE).exists()):
            with open(SAVED_MEMBER_FILE) as f:
                fileContent = f.readlines();
        if(fileContent == None): return;
        for line in fileContent:
            tokens = line.split("=");
            if(len(tokens) > 1):
                self.addMemberToDict(tokens[0], tokens[1]);
            else:
                self.addMemberToDict(tokens[0]);