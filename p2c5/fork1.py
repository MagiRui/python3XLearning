#!/usr/bin/env python
#author:MagiRui

import os


def child():
    print("Hello from child", os.getpid(), os.getppid())
    os._exit(0)


def parent():

    while True:

        newpid = os.fork()
        if newpid == 0 :
            child()
        else:
            print("Hello from parent", os.getpid(), newpid, os.getppid())

        if input() == "q":
            break


if __name__ == "__main__":

    parent()