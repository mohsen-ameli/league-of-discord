# This script will show you the acttack range of your champion.
# Will need to have "show attack range" enabled in "interface" settings.
# Also "show advanced player stat" under "hotkeys > Menus" needs to be enabled and set to the 'c' key

import keyboard
from time import sleep

print('press p to pause')

paused = False

def on_key_event(e):
    global paused
    if e.name == 'p':
        paused = not paused
        print('paused' if paused else 'unpaused')

keyboard.on_press(on_key_event)

while True:
    if paused:
        sleep(1)
        continue
    keyboard.press('c')
    sleep(5)

