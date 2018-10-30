'''
Created on Oct 30, 2018

@author: vaibh
'''

class Gift(object):
    '''
    classdocs
    '''
    
    broughtBy = None;

    def __init__(self, broughtBy):
        '''
        Constructor
        '''
        self.broughtBy = broughtBy;
        
    def getBroughtBy(self):
        return self.broughtBy;
    
    def setBroughtBy(self, broughtBy):
        self.broughtBy = broughtBy;