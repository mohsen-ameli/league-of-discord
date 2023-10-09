# Made by me, NoobMoe

import win32.win32gui as win32gui
import win32.win32api as win32api
import win32.lib.win32con as win32con
import pygetwindow as gw
from time import sleep
from pynput import keyboard

soundboard = {
    "hentai.exe": (400, 410),
    "trump wall": (550, 410),
    "cook": (700, 410),
    "hit the nexus": (400, 460),
    "gaymer": (550, 460),
    "poosy": (700, 460),
    "brazil": (400, 510),
    "bonk": (550, 510),
    "quack": (383, 588),
    "airporn": (539, 587),
    "cricket": (702, 588),
    "golf clap": (383, 639),
    "sad porn": (539, 635),
    "da dum tss": (699, 634),
}

# Find out the position of the cursor when left-clicked.
# NOT actually used for the core program.
def click_listener():
    while True:
        left_button_state = win32api.GetKeyState(win32con.VK_LBUTTON)
        
        if left_button_state < 0:
            x, y = win32api.GetCursorPos()
            print(f"Left-clicked at position: ({x}, {y})")

        sleep(0.1)

# Gets the full window name of discord
def get_active_window_title():
    for title in gw.getAllTitles():
        if "Discord" in title:
            return title

# Clicks on a given window in the background
def click(x, y):
    window_title = get_active_window_title()
    hWnd = win32gui.FindWindow(None, window_title)
    lParam = win32api.MAKELONG(x, y)

    hWnd1= win32gui.FindWindowEx(hWnd, None, None, None)
    win32gui.SendMessage(hWnd1, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
    win32gui.SendMessage(hWnd1, win32con.WM_LBUTTONUP, None, lParam)

def on_press(key):
    try:
        if key.char == 'q':
            sleep(0.5)
            click_discord("bonk")
        if key.char == 'r':
            click_discord("brazil")
    except AttributeError:
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        return False

# PLAY DISCORD SOUND
def click_discord(name: str):
    click(812, 809) # click outside to dismiss soundboard
    click(280, 747) # open soundboard
    click(soundboard[name][0], soundboard[name][1]) # specific sound

# def mouse_listener(x, y, button, pressed):
#     if pressed and button == mouse.Button.right:
#         click_discord("quack") # QUACK

if __name__ == "__main__":
    # Collect events until released
    # mouse.Listener(on_click=mouse_listener) as mouse_l # for mouse
    with keyboard.Listener(on_press=on_press, on_release=on_release) as keyboard_l:
        keyboard_l.join()

    # click_listener()
