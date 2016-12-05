#!/usr/bin/env python

import threading
import time

exitFlag = 0

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
        time.sleep(1000)
        counter -= 1

# Create new threads
timer_5sn = timerThread(1, "timer 5 sn", 5)

# Start new Threads
timer_5sn.start()

print "hello world"
