import mouse
from time import sleep

duration = 0.5 # 0.01

def click(pos: tuple[int, int]):
    mouse.move(pos[0], pos[1], absolute=True, duration=duration)
    mouse.click('left')

# get position of mouse
def get_mouse_pos():
    # events = mouse.record()
    # mouse.play(events[:-1])

    mouse.on_click(lambda: print(mouse.get_position()))
    sleep(100)

discord_icon = (369, 842)
dismiss_soundboard = (1014, 47)
open_soundboard = (278, 745)
first_sound = (382, 410)


click(discord_icon)
click(dismiss_soundboard)
click(open_soundboard)
click(first_sound)

# get_mouse_pos()
