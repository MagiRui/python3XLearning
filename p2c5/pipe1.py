#!/usr/bin/env python
#coding:utf8
#author:MagiRui

import os, time

def child(pipeout):

    zzz = 0
    while True:

        time.sleep(zzz)
        msg = ("Spam %03d" % zzz).encode() #管道是二进制字节
        os.write(pipeout, msg)
        zzz = (zzz + 1 ) % 5


def parent():

    pipein, pipeout = os.pipe()  #创建带有两个末端的管道
    if os.fork() == 0:
        child(pipeout)
    else:

        while True:
            line = os.read(pipein, 32)
            print("Parent %d got [%s] at %s " %(os.getpid(), line, time.time()))



parent()