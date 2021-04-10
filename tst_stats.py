#!/usr/bin/python3
# Created using Python 3.7.5

# Standard Python3 imports.
import json
import sys

# Import the stats module from the adjacent src directory.
sys.path.append('../src/')
from stats import Stats

''' TODO: DESCRIPTION

TODO: DETAILS
'''
def tst_addAction():
    # Create class instance.
    statsObj = Stats()
    
    # Create some test data and call the addAction function.
    testData  = json.dumps({ 'action': 'jump', 'time': 100 })
    assert(statsObj.addAction(testData) == True)
    
    # Repeat the above step with additional data.
    testData = json.dumps({ 'action': 'run', 'time': 75 })
    assert(statsObj.addAction(testData) == True)
    
    # Repeat the above step with additional data.
    testData = json.dumps({ 'action': 'jump', 'time': 200 })
    assert(statsObj.addAction(testData) == True)
    
    # Test addAction() against empty and malformed data.
    assert(statsObj.addAction({}) == False)
    assert(statsObj.addAction(44) == False)
    assert(statsObj.addAction(True) == False)
    
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