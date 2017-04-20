#! /usr/bin/env python
'''
Copyright (C) 2012  Diego Torres Milano
Created on Feb 1, 2012

@author: diego
'''


import re
import sys
import os

# This must be imported before MonkeyRunner and MonkeyDevice,
# otherwise the import fails.
# PyDev sets PYTHONPATH, use it
try:
    for p in os.environ['PYTHONPATH'].split(':'):
        if not p in sys.path:
            sys.path.append(p)
except:
    pass

try:
    sys.path.append(os.path.join(os.environ['ANDROID_VIEW_CLIENT_HOME'], 'src'))
except:
    pass

from com.dtmilano.android.viewclient import ViewClient

package='com.nintendo.zaba'
activity='org.cocos2dx.cpp.AppActivity'
component=package + "/" + activity
device, serialno = ViewClient.connectToDeviceOrExit()
cwd = os.path.dirname(os.path.abspath(__file__))
def openRow(device, start, end, row):
    iter = 70
    x = 65
    for i in range(start, end):
        print('Getting image ' + str(i) + ' of row ' + str(row))
        device.dragDip((x + (iter*i), 344), (x + (iter*i), 345), 2000, -1)
        ViewClient.sleep(2)
        ViewClient(device, serialno).writeImageToFile(cwd + '/' + str(i) +'.png', 'PNG', None, False, False)
        device.press('KEYCODE_BACK')



if True:
    # device.press('KEYCODE_BACK')
    openRow(device, 1, 5, 0)
    print('done')
    # device.startActivity(component=component)
    # ViewClient.sleep(10)
    # #Touch somewhere to progress from splash screen
    # device.touch(45,980)
    # ViewClient.sleep(5) # Sleep while we load the castle
    # device.getDisplayInfo
    # # Open the Allies Tab
    # device.touchDip(170, 700, 0)

    # # Open Equip Edit Teams Screen
    # device.touchDip(200, 150, 0)

    # #Simulate Longpress
    # device.dragDip((55,344),(55,345), 2000, -1)


    # for _ in range(20):
    #     device.drag((15, 1000), (15, 827.45), 1000, 20, 0)