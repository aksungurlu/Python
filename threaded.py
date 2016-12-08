#!/usr/bin/env python

import threading
import time
import tty
import sys
import termios

exitFlag = 0
key = 'n'
orig_settings = termios.tcgetattr(sys.stdin)



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
    global termios
    
    
	
    while key != 'q':
        if exitFlag:
            threadName.exit()
        tty.setraw(sys.stdin)
        ch = sys.stdin.read( 1 )[0]
        if ch != key:
			key = ch
	
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings) 
			
# Create new threads
timer_5sn = timerThread(1, "timer 5 sn", 5)
keystroke_h1 = keystrokeThread(2, "keystroke handler")

# Start new Threads
timer_5sn.start()
keystroke_h1.start()

print "press q to quit"
