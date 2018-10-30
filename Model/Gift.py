'''
Created on Oct 30, 2018

@author: vaibh
'''

class Gift(object):
    '''
    The class represents gift
    '''
    
    broughtBy = None;

    def __init__(self, broughtBy):
        '''
        Default Constructor
        broughtBy: (str) The bringer's name
        '''
        self.broughtBy = broughtBy;
        
    def getBroughtBy(self):
        '''
        Returns the name of person, who brought the gift to dinner
        return: (str) The bringer's name
        '''
        return self.broughtBy;
    
    def setBroughtBy(self, broughtBy):
        '''
        Function to change the bringer's name. Never used in current scope.
        '''
        self.broughtBy = broughtBy;