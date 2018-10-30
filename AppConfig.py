'''
Created on Oct 30, 2018

@author: vaibh
'''

import os;
from os.path import dirname;

"""
Error Codes
"""
BAD_CHOICE = -1;


"""
Logger Configuration
"""
LOG_LEVEL_CRITICAL = 0;
LOG_LEVEL_OPERATIONAL = 1;
LOG_LEVEL_DEBUG = 2;

APP_LOG_LEVEL = LOG_LEVEL_DEBUG;


"""
System States / Events
"""
SYS_STATE_HOME = 0;
SYS_STATE_MEMBER = 1;
SYS_STATE_RESULTS = 2;
SYS_STATE_SIMULATION = 3;
SYS_STATE_EXIT = 4;


"""
Saved Member List
"""
SAVED_MEMBER_FILE = (os.getcwd()) + "\\Resources\\memberList.txt";

"""
Language Config
"""
APP_LANGUAGE_FILE = (os.getcwd()) + "\\Resources\\EnglishMessages.txt";
MSG_GOOD_BYE = 1;
MSG_MANAGE_MEMBERS = 2;
MSG_SHOW_RESULTS = 3;
MSG_QUIT = 4;
MSG_ADD_MEMBER = 5;
MSG_REMOVE_MEMBER = 6;
MSG_SHOW_MEMBERS = 7;
MSG_GO_BACK = 8;
MSG_ENTER_MEMBER_NAME = 9;
MSG_ENTER_MEMBER_PARTNERS = 10;
MSG_MEMBER_NOT_FOUND = 11;
MSG_MEMBER_REMOVED = 12;
MSG_MEMBER_ADDED = 13;
MSG_PICKED_GIFT_FROM = 14;
MSG_WELLCOME_MESSAGE = 15;
MSG_GIFT_EXCHANGE_NOT_POSSIBLE = 16;
MSG_SIMULATE_TURNS = 17;
MSG_FALSE_PICK_START_AGAIN = 18;
MSG_MAKE_PICK = 19;