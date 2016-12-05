#!/usr/bin/env python

import threading
import time
import sys

exitFlag = 0
key = 'n'

class timerThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print "Starting " + self.name
        start_timer(self.name, self.counter)
        print "Exiting " + self.name

def start_timer(threadName, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(1)
        counter -= 1
        
class keystrokeThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        print "Starting " + self.name
        keystroke_handler(self.name)
        print "Exiting " + self.name
        
def keystroke_handler(threadName):
    global key
	
    while True:
        """if exitFlag:
            threadName.exit()"""
        key = sys.stdin.read( 1 )

# Create new threads
timer_5sn = timerThread(1, "timer 5 sn", 5)

# Start new Threads
timer_5sn.start()

print "hello world"
print "how are you"
