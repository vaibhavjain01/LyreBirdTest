'''
Created on Oct 30, 2018

@author: vaibh
'''

from AppConfig import *; #@UnusedWildImport 

class Logger(object):
    '''
    Implementation of application logger
    '''

    def __init__(self):
        '''
        Default Constructor
        '''

    def TRACE(self, logLevel, logData, logTarget=None):
        '''
        logLevel: (int) The log level of current log
        logData: (str) The log data to be printed
        logTarget: (Object) The log target. None means console
        '''
        if(logTarget == None):
            self.logConsole(logLevel, logData);
        else:
            self.logView(logLevel, logData, logTarget);
            
    def logConsole(self, logLevel, logData):
        '''
        logLevel: (int) The log level of current log
        logData: (str) The log data to be printed
        '''
        if(logLevel <= APP_LOG_LEVEL):
            print(logData);
            
    def logView(self, logLevel, logData, logTarget):
        '''
        logLevel: (int) The log level of current log
        logData: (str) The log data to be printed
        logTarget: (Object) The log target. None means console
        '''
        if(logLevel <= APP_LOG_LEVEL):
            logTarget.log(logData);