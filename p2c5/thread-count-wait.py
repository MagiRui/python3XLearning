#!/usr/bin/python
#author:MagiRui

import _thread as thread

stdoutMutex = thread.allocate_lock()

exitMutex = [thread.allocate_lock() for i in range(10)]

def counter(myId, count):

    for i in range(count):

        stdoutMutex.acquire()
        print("[%s] => %s" %(myId, i))
        stdoutMutex.release()
    exitMutex[myId].acquire()


for i in range(10):

    thread.start_new_thread(counter, (i, 100))

for mutex in exitMutex:

    while not mutex.locked():
        pass

print("Main thread exiting")