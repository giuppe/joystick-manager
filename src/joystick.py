'''
Created on 16/set/2011

@author: giuppe
'''


from ioctl.IOCTL import _IOC, _IOR, _IOW, _IOC_READ
from ioctl.sizes import INT
from observer import JoystickEventGenerator



import fcntl, struct

class Joystick(JoystickEventGenerator):
    JS_EVENT_BUTTON  =       0x01    #/* button pressed/released */
    JS_EVENT_AXIS   =        0x02    #/* joystick moved */
    JS_EVENT_INIT   =        0x80    #/* initial state of device */

    #struct js_event {
    #        __u32 time;     /* event timestamp in milliseconds */
    #        __s16 value;    /* value */
    #        __u8 type;      /* event type */
    #        __u8 number;    /* axis/button number */
    #};


    KEY_MAX = 0x2ff
    KEY_CNT = (KEY_MAX + 1)
    
    ABS_MAX = 0x3f
    ABS_CNT = (ABS_MAX + 1)
    
    BTN_MISC = 0x100
    
    JSIOCGVERSION = _IOR(ord('j'), 0x01, INT)                          # get driver version */
    
    JSIOCGAXES = _IOR(ord('j'), 0x11, "b")                        # get number of axes */
    JSIOCGBUTTONS = _IOR(ord('j'), 0x12, "b")                          # get number of buttons */
    JSIOCGNAME = _IOC(_IOC_READ, ord('j'), 0x13, 1024)                 # get identifier string */
    
     
    
    #define JSIOCSCORR              _IOW(ord('j'), 0x21, struct js_corr)                 /* set correction values */
    #define JSIOCGCORR              _IOR(ord('j'), 0x22, struct js_corr)                 /* get correction values */
    
    JSIOCSAXMAP = _IOW(ord('j'), 0x31, ABS_CNT.__str__() + "b")                  #/* set axis mapping */
    JSIOCGAXMAP = _IOR(ord('j'), 0x32, ABS_CNT.__str__() + "b")                  #/* get axis mapping */
    JSIOCSBTNMAP = _IOW(ord('j'), 0x33, (KEY_MAX - BTN_MISC + 1).__str__() + "h")  #/* set button mapping */
    JSIOCGBTNMAP = _IOR(ord('j'), 0x34, (KEY_MAX - BTN_MISC + 1).__str__() + "h")  #/* get button mapping */


    file_name = None
    isInit = False
    fd = None
    
    def __init__(self):
        pass
    
    def init(self, fileName):
        self.fd = open(fileName)
        self.isInit = True

    def get_name(self):
        name = fcntl.ioctl(self.fd, self.JSIOCGNAME, chr(0)*1024)
        return name.replace(chr(0), '')

    def get_axis(self):
        name = fcntl.ioctl(self.fd, self.JSIOCGAXES, chr(0))
        return struct.unpack("b", name.replace(chr(0), ''))[0]
    
    def get_buttons(self):
        name = fcntl.ioctl(self.fd, self.JSIOCGBUTTONS, chr(0))
        

        return struct.unpack("b", name.replace(chr(0), ''))[0]
        
        #return 0
    
    def update(self):
        event = self.fd.read(4+2+1+1)
        (etime, evalue, etype, enumber) = struct.unpack("Ihbb", event)
        if(etype & self.JS_EVENT_AXIS):
            print "%s: Axis %d, value %d" % (etime, enumber, evalue)
            self.sendAxisSignal(enumber, evalue)
        elif(etype & self.JS_EVENT_BUTTON):
            print "%s: Button %d, value %d" % (etime, enumber, evalue)
            self.sendButtonSignal(enumber, evalue)
        else:     
            print etime
            print evalue
            print etype
            print enumber
    
if __name__ == '__main__':
    import time
    joy = Joystick()
    joy.init("/dev/input/js0")
    print joy.get_name()
    print joy.get_axis()
    print joy.get_buttons()
    while(1):
        #time.sleep(1)
        joy.update()
        