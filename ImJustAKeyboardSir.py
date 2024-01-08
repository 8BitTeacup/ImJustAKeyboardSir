#!/usr/bin/python3 

import Cocoa, Foundation, time, Quartz, objc
from PyObjCTools import AppHelper
from ctypes import CDLL, c_int, c_float, c_uint32, byref

def howManyMonitors():
    
    (err, active_displays, number_of_active_displays) = Quartz.CGGetOnlineDisplayList(2, None, None)
    return number_of_active_displays

DisplayServices = CDLL("/System/Library/PrivateFrameworks/DisplayServices.framework/DisplayServices")
DisplayServices.DisplayServicesSetBrightness.argtypes = [c_int, c_float]

class MyClass(Cocoa.NSObject):
    def setBrightnessToZero(self):
        if howManyMonitors() > 1:
            DisplayServices.DisplayServicesSetBrightness(1, 0.0)

nc = Foundation.NSDistributedNotificationCenter.defaultCenter()
MyClass = MyClass.new()
nc.addObserver_selector_name_object_(MyClass, 'setBrightnessToZero', 'com.apple.screenIsUnlocked',None)

AppHelper.runConsoleEventLoop()