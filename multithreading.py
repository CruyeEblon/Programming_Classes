"""Raises and lowers beo's arms every few seconds"""
#!/usr/bin/python

import threading
import time
from Movements import Movements

MOVEMENTS = Movements()

EXITFLAG = 0

class MyThread(threading.Thread):
    """My thread class using threading library"""
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter
    def run(self):
        print("Starting " + self.name)
        print_time(self.name, self.counter, 5)
        print("Exiting " + self.name)




def print_time(thread_name, counter, delay):
    """Prints the time and moves beo's arm"""
    while counter:
        if EXITFLAG:
            thread_name.exit()
        time.sleep(delay)
        if thread_name == "Thread-1":
            MOVEMENTS.set_raw_angle(0, 180)
        if thread_name == "Thread-2":
            MOVEMENTS.set_raw_angle(0, 0)
        print("%s: %s" % (thread_name, time.ctime(time.time())))
        counter -= 1

# Create new threads
THREAD1 = MyThread(1, "Thread-1", 5)
THREAD2 = MyThread(2, "Thread-2", 6)

# Start new Threads
THREAD1.start()
time.sleep(1)
THREAD2.start()

print("Exiting Main Thread")
