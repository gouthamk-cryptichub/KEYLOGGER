#!/usr/bin/env python
import pynput.keyboard

def use_keys(key):
    print(key)


key_rec = pynput.keyboard.Listener(on_press=use_keys)
with key_rec:
    key_rec.join()