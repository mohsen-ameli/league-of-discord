# The first version of this script
# Main problem to solve is that the actual mouse has to move for this to work.
# We want an invisible mouse to do the work.

import mouse
from time import sleep

duration = 0.5
discord_pos = (350, 843)
dismiss_soundboard_pos = (1014, 47)
open_soundboard_pos = (278, 745)
sound_pos = (382, 410)

# click on a given position
# pos: x,y position to click on
def click(pos: tuple[int, int]):
    mouse.move(pos[0], pos[1], absolute=True, duration=duration)
    mouse.click('left')

# gets the position of the mouse when left clicked.
def get_mouse_pos():
    # events = mouse.record()
    # mouse.play(events[:-1])

    mouse.on_click(lambda: print(mouse.get_position()))
    sleep(100)


# first click on discord, then dismiss the soundboard, then open soundboard and click on the desired sound
if __name__ == "__main__":
    click(discord_pos)
    click(dismiss_soundboard_pos)
    click(open_soundboard_pos)
    click(sound_pos)
    # get_mouse_pos()
