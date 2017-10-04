"""Raises and lowers beo's arms every few seconds"""
#!/usr/bin/python

import threading
import time
from Movements import Movements

MOVEMENTS = Movements()

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("Starting " + self.name)
        print_time(self.name, self.counter, 5)
        print("Exiting " + self.name)




def print_time(threadName, counter, delay):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        if threadName == "Thread-1":
            MOVEMENTS.set_raw_angle(0, 180)
        if threadName == "Thread-2":
            MOVEMENTS.set_raw_angle(0, 0)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

# Create new threads
thread1 = myThread(1, "Thread-1", 5)
thread2 = myThread(2, "Thread-2", 6)

# Start new Threads
thread1.start()
time.sleep(1)
thread2.start()

print("Exiting Main Thread")
