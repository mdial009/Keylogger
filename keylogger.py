import pynput
from pynput.keyboard import Key, Listener


def on_pressed(key):
    print("{0} pressed".format(key))


def on_released(key):
    if key == Key.esc:
        return False


# functions called when a button is pressed and released.
with Listener(on_pressed=on_pressed, on_released=on_released) as thelistener:
    thelistener.join()
