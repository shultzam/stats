#!/usr/bin/python3

# Standard Python3 imports.
import json
import sys

# Import the stats module from the adjacent src directory.
sys.path.append('../src/')
from stats import addAction, getStats

''' TODO: DESCRIPTION

TODO: DETAILS
'''
def tst_addAction():
    # Create some test data and call the addAction function.
    testData  = json.dumps({ 'action': 'jump', 'time': 100 })
    assert(addAction(testData) == True)
    
    # Repeat the above step with additional data.
    testData = json.dumps({ 'action': 'run', 'time': 75 })
    assert(addAction(testData) == True)
    
    # Repeat the above step with additional data.
    testData = json.dumps({ 'action': 'jump', 'time': 200 })
    assert(addAction(testData) == True)
    
    # Test addAction() against empty data and malformed data.
    assert(addAction({}) == False)
    assert(addAction(44) == False)
    assert(addAction(True) == False)
    
    return

''' TODO: DESCRIPTION
    
TODO: DETAILS
'''
def tst_getStats():
    print('TEMP | entered tst_getStats()')
    return

# Entry point.
if __name__ == "__main__":
    tst_addAction()
    tst_getStats()