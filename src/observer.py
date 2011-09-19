'''
Created on 18/set/2011

@author: giuppe
'''

class JoystickEventGenerator(object):
    '''
    classdocs
    '''
    observers = []

    def __init__(self):
        '''
        Constructor
        '''
    def registerListener(self, obs):
        self.observers.append(obs)
        
    def sendAxisSignal(self, evnumber, evvalue):
        for obs in self.observers:
            obs.onAxisSignal(evnumber, evvalue)
            
    def sendButtonSignal(self, evnumber, evvalue):
        for obs in self.observers:
            obs.onButtonSignal(evnumber, evvalue)
            
class JoystickEventListener(object):
    
    def OnAxisSignal(self, axisNumber, axisValue):
        pass
    
    def OnButtonSignal(self, btnNumber, btnValue):
        pass
    
