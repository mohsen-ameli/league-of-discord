# Half-ass attempt i know :0

from pynput.keyboard import Key, Listener
from playsound import playsound

# def on_press(key):
#     print(f'{key} pressed')

def on_release(key):
    print(f'{key} released')

    if key == "q":
        print("Q pressed")

    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
