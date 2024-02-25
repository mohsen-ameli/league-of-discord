# Made by me, NoobMoe
# This script will listen for a keyboard click of "r" and will click on a series
# of button using an invisible cursor, to play a sound on th soundboard of discord.

import win32.win32gui as win32gui
import win32.win32api as win32api
import win32.lib.win32con as win32con
import pygetwindow as gw
from time import sleep
from pynput import keyboard

# These are just the soundboards I have access to. If you want to specifically do this
# you will have to use the mouse_click_listener function to manually retrieve these values.
soundboard = {
    "hentai.exe": (400, 400),
    "trump wall": (550, 400),
    "cook":       (700, 400),
    "hit nexus":  (400, 450),
    "poosy":      (550, 450),
    "brazil":     (700, 450),
    "gulp":       (400, 450),
    "ack":        (550, 500),
}
discord_pos = (343, 837)
dismiss_soundboard_pos = (821, 806)
open_soundboard_pos = (282, 734)

# Find out the position of the cursor when left-clicked.
# note: this is not actually used for the core program.
def mouse_click_listener():
    while True:
        left_button_state = win32api.GetKeyState(win32con.VK_LBUTTON)
        
        if left_button_state < 0:
            x, y = win32api.GetCursorPos()
            # name = input("Give a name to this soundboard")
            # input("Save or try again?")
            print(f"Left-clicked at position: ({x}, {y})")

        sleep(0.1)

# Gets the full window name of discord
def get_active_window_title():
    for title in gw.getAllTitles():
        if "Discord" in title:
            return title

# Clicks on a given window in the background
def click(pos: tuple[int, int]):
    window_title = get_active_window_title()
    hWnd = win32gui.FindWindow(None, window_title)
    lParam = win32api.MAKELONG(pos[0], pos[1])

    hWnd1= win32gui.FindWindowEx(hWnd, None, None, None)
    win32gui.SendMessage(hWnd1, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
    win32gui.SendMessage(hWnd1, win32con.WM_LBUTTONUP, None, lParam)

# When a key is pressed, we run this function
def on_press(key):
    print(key)
    try:
        # if key.char == 'e':
        #     # sleep(0.5)
        #     click_discord("gaymer")
        # if key.char == 'q':
        #     sleep(0.5)
        #     click_discord("bonk")
        if key.char == 'r':
            click_discord("brazil")
            sleep(3)
    except AttributeError:
        pass

# When a key is released we run this function
def on_release(key):
    if key == keyboard.Key.esc:
        return False

# Plays a soundboard sound on discord, given its name
def click_discord(name: str):
    click(discord_pos)              # click on discord
    click(dismiss_soundboard_pos)   # click outside to dismiss soundboard
    click(open_soundboard_pos)      # open soundboard
    click(soundboard[name])         # click specific sound

if __name__ == "__main__":
    with keyboard.Listener(on_press=on_press, on_release=on_release) as keyboard_: keyboard_.join()

    # Uncomment the following to get the mouse position. Also comment the top two lines
    # mouse_click_listener()
