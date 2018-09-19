#!/usr/bin/env python
#coding:utf8
#author:MagiRui

numconsumers = 2
numproducers = 4
nummessages = 4

import threading, queue, time

dataqQueue = queue.Queue()

def producer(idnum, dataqueue):

    for msgnum in range(nummessages):

        time.sleep(idnum)
        dataqueue.put("[producer id = %d, count=%d]" %(idnum, msgnum))


def consumer(idnum, dataqueue):

    while True:
        print(">>>><<<<<")
        time.sleep(0.1)
        try:
            data = dataqueue.get(block=False)
        except queue.Empty:

            pass
        else:

            print("consumer", idnum, "got =>", data)


if __name__ == "__main__":

    for i in range(numconsumers):

       thread =  threading.Thread(target=consumer, args=(i, dataqQueue))
       #thread.daemon = True
       thread.start()

    waitfor = []
    for i in range(numproducers):

        thread = threading.Thread(target=producer, args = (i, dataqQueue))
        waitfor.append(thread)
        thread.start()


    #for thread in waitfor: thread.join()
    print("Main thread exit.")
