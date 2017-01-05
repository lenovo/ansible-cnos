#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Lenovo, Inc.

# This module is distributed WITHOUT ANY WARRANTY; without even the implied 
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
#
# See the GNU General Public License for more details <http://www.gnu.org/licenses/>.
#
#Contains utility methods
# Lenovo Networking

import time
import ftplib
import re


#Entry method to parse the dictionary for commanf formation 
def parseCommand(commandid, valuelist, dictionaryFile) :
    commandStr = getCommandTextFromDictionary(commandid, dictionaryFile)
    variables = re.findall(r"\<([A-Za-z0-9_]+)\>", commandStr)
    index = 0
    cmdVal = {}
    for variable in variables:
        print variable
        cmdVal[variable] = valuelist[index]
        index = index +1
    retSanity = checkSanityofVariables(cmdVal, dictionaryFile)
    if(retSanity == "ok"):
        retCmd = replaceCommandStrWithValues(commandStr, valuelist)
        print retCmd
    else:
        print retSanity
        retCmd = ""
    return retCmd 

#From the command 
def getCommandTextFromDictionary(commandid, dictionaryFile):
    f = open(dictionaryFile, 'r')
    lines = f.readlines()
    f.close()
    retCmd = ""
    for i, line in enumerate(lines):
        data = line.split(':')
        if(data[0] == commandid):
            retCmd = data[1]  
    return retCmd

# A dictionary object is passed and validation happens against type range and values
def checkSanityofVariables(cmdVal, dictionaryFile) :
    #Fill in logic here
    return "ok"
#EOM

def replaceCommandStrWithValues(commandStr, valuelist) :
    #Need to be tested.
    retCmd = commandStr
    for key, value in valuelist.iteritems():
        retCmd = retCmd.replace(key,value,1)
    return retCmd

#EOM
