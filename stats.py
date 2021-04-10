#!/usr/bin/python3
# Created using Python 3.7.5

# Standard Python3 import(s).
import json


''' Stats class '''
class Stats:
    def __init__(self):
        ''' actionDict, a standard Python3 dictionary.
            
            Used to maintain incoming data through concurrent calls. The data is stored as a list
            containing [action count, total duration]. Total count represents the total count of 
            that specific action given.
        '''
        self.actionDict = {}
        
    
    ''' TODO: DESCRIPTION

    TODO: DETAILS
    '''
    def addAction(self, action: str) -> bool:
        # Load the JSON into a string. In this case, loads() is really only used to verify JSON format.
        try:
            actionJson = json.loads(action)
            actionName = actionJson['action']
            actionTime = actionJson['time']
            #print('TEMP | in action getAction(), received action: {}'.format(actionJson))
        except TypeError:
            print('ERROR in addAction(): action ({}) cannot be processed.'.format(action))
            return False
        
        # Save off the action's info for easier handling.
        
        # This check prevents a KeyError in the event this is the first of this action type received.
        if actionName not in self.actionDict:
            self.actionDict[actionName] = [0, 0]
            
        # Add the given action data to the actionDict.
        self.actionDict[actionName][0] += 1             # Increment action count.
        self.actionDict[actionName][1] += actionTime    # Increment action duration.
        
        return True

    
    ''' TODO: DESCRIPTION

    TODO: DETAILS
    '''
    def getStats(self) -> str:
        print('TEMP | entered tst_getStats()')
        return 'Not yet implemented'