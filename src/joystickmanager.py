'''
Created on 17/set/2011

@author: giuppe
'''
import pygtk
pygtk.require('2.0')
import gtk
import time
from observer import JoystickEventListener
from joystickupdate import JoystickUpdate
import gobject

gobject.threads_init()

class JoystickManager(JoystickEventListener):

    joystickDescriptions = []
    buttons = []
    
    def main(self):
        
        gui = gtk.Builder()
        gui.add_from_file('../ui/joystick-manager.glade')
        win_youtubedl = gui.get_object('jsmanager')
        win_youtubedl.show_all()
        self.joystickList = gui.get_object('liststore1')
        self.joystickList.append(["pippo"])
        
        jsUpdate = JoystickUpdate()
        jsUpdate.setDevice("/dev/input/js1")
        jsUpdate.start()
        time.sleep(1)
        jsUpdate.getJoystick().registerListener(self)
        btnNum = jsUpdate.getJoystick().get_buttons()
        for i in range(btnNum):
            objectName = "btn%d" % (i+1) 
            self.buttons.append(gui.get_object(objectName))
        gtk.main()
        
    def onButtonSignal(self, btnNumber, btnValue):
        if(btnValue==1):
            self.buttons[btnNumber].set_active(True)
        else:
            self.buttons[btnNumber].set_active(False)
       
    def onAxisSignal(self, axisNumber, axisValue):
        pass
    
    
if __name__ == '__main__':
    jsm = JoystickManager()
    gtk.gdk.threads_enter()
    jsm.main()
    gtk.gdk.threads_leave()