#! /usr/bin/env python
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
from datetime import datetime

package='com.nintendo.zaba'
activity='org.cocos2dx.cpp.AppActivity'
component=package + "/" + activity
device, serialno = ViewClient.connectToDeviceOrExit()
cwd = os.path.dirname(os.path.abspath(__file__))

def openRow(device, start, end, row, y=344):
    iter = 70
    x = 65
    for i in range(start, end):
        print 'Getting image ' + str(i) + ' of row ' + str(row)
        device.dragDip((x + (iter*i), y), (x + (iter*i), y+1), 2000, -1)
        ViewClient(device, serialno).writeImageToFile(cwd + '/images/' + str(row) + '-' + str(i) +'.png', 'PNG', None, False, False)
        device.press('KEYCODE_BACK')

HEROES_PER_ROW = 5
HERO_COUNT = 198
FIRST_ROW = 4
FINAL_ROW = (HERO_COUNT - 4) % HEROES_PER_ROW
ROWS_COUNT = (HERO_COUNT - FIRST_ROW - FINAL_ROW) / HEROES_PER_ROW

if True:
    startTime = datetime.now()

    # print "Read First Row"
    # openRow(device, 1, HEROES_PER_ROW, 0)

    # row = 1
    # for _ in range(ROWS_COUNT - 3):
    #     device.drag((15, 1000), (15, 827.45), 1000, 20, 0)
    #     openRow(device, 0, HEROES_PER_ROW, row)
    #     row += 1

    print "Read Final Rows"
    openRow(device, 0, HEROES_PER_ROW, ROWS_COUNT - 2, 405)
    openRow(device, 0, HEROES_PER_ROW, ROWS_COUNT - 1, 480)
    openRow(device, 0, HEROES_PER_ROW, ROWS_COUNT, 555)
    openRow(device, 0, FINAL_ROW, ROWS_COUNT + 1, 630)





    print('Script Complete: ' + str(datetime.now() - startTime))
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


    # for _ in range(34):
    #     print("Dragging")
    #     device.drag((15, 1000), (15, 827.45), 1000, 20, 0)