'''
Created on 19/set/2011

@author: giuppe
'''

import threading
from joystick import Joystick
import time

class JoystickUpdate(threading.Thread):
    '''
    classdocs
    '''
    
    def setDevice(self, devicePath):
        self.devicePath = devicePath

    def getJoystick(self):
        return self.joy

    def run(self):
        self.joy = Joystick()
        self.joy.init(self.devicePath)
        while(1):
            #time.sleep(1)
            print "Updating Joystick"
            self.joy.update()