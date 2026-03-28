# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 13:03:14 2024

Controlling the Keyboard and Mouse with GUI Automation

@author: 9387758
"""

import pyautogui, time
width, height = pyautogui.size()

'''for i in range(2):
    pyautogui.moveTo(100, 100, duration=1)
    pyautogui.moveTo(200, 100, duration=1)
    pyautogui.moveTo(200, 200, duration=1)
    pyautogui.moveTo(100, 200, duration=1)
    pyautogui.moveRel(100, 0, duration=1)
    pyautogui.moveRel(0, 100, duration=1)
    pyautogui.moveRel(-100, 0, duration=1)
    pyautogui.moveRel(0, -100, duration=1)'''

pyautogui.position()
    
# click
pyautogui.click(410, 130, button='left')

pyautogui.click(470, 1030, button='right')

# drag - draw spiral
time.sleep(5)
pyautogui.click()    # click to put drawing program in focus
distance = 100
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.2)   # move right
    distance = distance - 5
    pyautogui.dragRel(0, distance, duration=0.2)   # move down
    pyautogui.dragRel(-distance, 0, duration=0.2)  # move left
    distance = distance - 5
    pyautogui.dragRel(0, -distance, duration=0.2)  # move up

# Scrolling the Mouse
pyautogui.scroll(100)

# Getting a Screenshot
im = pyautogui.screenshot()
im.getpixel((50, 200))
pyautogui.pixelMatchesColor(50, 200, (130, 135, 144))
pyautogui.pixelMatchesColor(50, 200, (255, 135, 144))


def position_and_color():
    print('Press Ctrl-C to quit.')
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            pixelColor = pyautogui.screenshot().getpixel((x, y))
            positionStr += ' RGB: (' + str(pixelColor[0]).rjust(3)
            positionStr += ', ' + str(pixelColor[1]).rjust(3)
            positionStr += ', ' + str(pixelColor[2]).rjust(3) + ')'
            print(positionStr, end='')
            time.sleep(1)
    except KeyboardInterrupt:
        print('\nDone.')
        
position_and_color()

# open outlook, new mail
pyautogui.click(871, 1022, button='right')
time.sleep(1)
pyautogui.click(778, 774, button='left')
time.sleep(1)
# maximize window
pyautogui.keyDown('winleft'); 
pyautogui.press('up');
pyautogui.keyUp('winleft');

def fillin_e360_submission():
    # Step 1: Figure Out the Steps
    # 1. open browser, page. open excel that contains data.
    # Step 2: Set Up Coordinates
    # Step 3: Start Typing Data
    # Step 4: Handle Select Lists and Radio Buttons
    # Step 5: Submit the Form and Wait

def open_dbeaver():
    pyautogui.hotkey('winleft','r')
    pyautogui.write(r'C:\Users\9387758\AppData\Local\DBeaver\dbeaver.exe')
    pyautogui.press('enter')

def close_dbeaver():
    pyautogui.click(1645,12,button='left')    
    
def run_morning_sqlqueries():
    open_dbeaver()
    close_dbeaver()    
    

