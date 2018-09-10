#!/usr/bin/env python
#author:MagiRui

import os, time

def counter(count):

    for i in range(count):

        time.sleep(1)
        print("[%s]=>%s" %(os.getpid(), i))


for i in range(5):
    pid = os.fork()
    if pid != 0:
        print("Processs %d spawned " %pid)
    else:

        counter(5)
        os._exit(0)

print("Main process exiting")