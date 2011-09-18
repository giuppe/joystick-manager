'''
Created on 18/set/2011

@author: giuppe
'''

class EventSubject(object):
    '''
    classdocs
    '''
    observers = []

    def __init__(self):
        '''
        Constructor
        '''
    def registerObserver(self, obs):
        self.observers.append(obs)
        
    def sendSignal(self, evtype, evnumber, evvalue):
        for obs in self.observers:
            obs.onSignal(evtype, evnumber, evvalue)
            
class EventObserver(object):
    
    def onSignal(self, evtype, evnumber, evvalue):
        pass