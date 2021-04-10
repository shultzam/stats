#!/usr/bin/python3
# Created using Python 3.7.5

# Standard Python3 import(s).
import json


''' Stats class '''
class Stats:
    def __init__(self):
        ''' actionDict, a standard Python3 dictionary.
            
            Used to maintain incoming data through concurrent calls. The data is stored as a list
            containing [action count, total duration] with key of action_name. Total count represents 
            the total count of that specific action.
        '''
        self.actionDict = {}
        
    
    ''' TODO: DESCRIPTION

    TODO: DETAILS
    '''
    def addAction(self, action: str) -> bool:
        # Deserialize the JSON into a string. In this case, loads() is mostly used to verify JSON format.
        try:
            actionJson = json.loads(action)
            actionName = actionJson['action']
            actionTime = actionJson['time']
        except TypeError:
            print('ERROR in addAction(): action ({}) cannot be processed.'.format(action))
            return False
        
        # This check prevents a KeyError if this is the first of this action type received.
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
        # Formulate the response.
        responseList = []
        for key in self.actionDict:
            # Add this key's data to the response.
            actionAverage = float(self.actionDict[key][1] / self.actionDict[key][0])
            responseList.append({ 'action': key, 'time': actionAverage })
        
        # JSON serialize the response and return it.
        return json.dumps(responseList)
