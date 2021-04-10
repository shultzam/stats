#!/usr/bin/python3
# Created using Python 3.7.5

# Standard Python3 import(s).
import json

# Import the stats module from the adjacent src directory.
from stats import Stats

''' tst_addAction

Tests Stats::addAction. Tests included:
  - Valid JSON data of multiple action types
  - Empty data
  - Invalid data types
  - Invalid JSON data
  - Missing fields from valid JSON data
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
    
    # Add an action that is not part of the sample inputs.
    testData = json.dumps({ 'action': 'spin', 'time': 12 })
    assert(statsObj.addAction(testData) == True)
    testData = json.dumps({ 'action': 'spin', 'time': 190 })
    assert(statsObj.addAction(testData) == True)
    
    # Test addAction() against empty and malformed data.
    assert(statsObj.addAction({}) == False)
    assert(statsObj.addAction(44) == False)
    assert(statsObj.addAction(True) == False)
    testData = json.dumps({ 'action': 'spin' })
    assert(statsObj.addAction(testData) == False)
    testData = json.dumps({ 'time': 12 })
    assert(statsObj.addAction(testData) == False)
    
    print('tst_addAction() completed successfully.')
    return


''' tst_getStats
    
Tests Stats::getStats by mostly just verifying the result getStats matches expectations.
'''
def tst_getStats():
    # Create class instance.
    statsObj = Stats()
    
    # Define some common keys for easier verification later.
    jumpKey = 'jump'
    runKey = 'run'
    spinKey = 'spin'
    
    # Create some test data and call the addAction function.
    testData  = json.dumps({ 'action': jumpKey, 'time': 100 })
    statsObj.addAction(testData)
    
    # Repeat the above step with additional data.
    testData = json.dumps({ 'action': runKey, 'time': 75 })
    statsObj.addAction(testData)
    
    # Repeat the above step with additional data.
    testData = json.dumps({ 'action': jumpKey, 'time': 200 })
    statsObj.addAction(testData)
    
    # Add an action that is not part of the sample inputs.
    testData = json.dumps({ 'action': spinKey, 'time': 12 })
    assert(statsObj.addAction(testData) == True)
    testData = json.dumps({ 'action': spinKey, 'time': 190 })
    assert(statsObj.addAction(testData) == True)
    
    # Get the current data and verify it against expectations.
    statsResults = json.loads(statsObj.getStats())
    
    # The expected results are hard-coded for now. If this test becomes more robust or more values
    # are tested we may want to determine this value dynamically. Pop is used to remove the lone item 
    # from the returned list.
    testVal = [item for item in statsResults if item['action'] == jumpKey].pop()
    assert(testVal['time'] == 150.0)
    testVal = [item for item in statsResults if item['action'] == runKey].pop()
    assert(testVal['time'] == 75.0)
    testVal = [item for item in statsResults if item['action'] == spinKey].pop()
    assert(testVal['time'] == 101.0)
    
    print('tst_getStats() completed successfully.')
    return


# Entry point.
if __name__ == "__main__":
    tst_addAction()
    tst_getStats()
    