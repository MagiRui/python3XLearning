#!/usr/bin/env python
#author:MagiRui


"""
以上代码的要点在于os.execlp调用。简而言之,该调用可以用一个全新的程序代替(即执行覆盖)当前进程
中正运行的程序。由于这个原因，os.fork和os.execlp的组合意味着开始一个新的进程,并在其中运行一个
新的程序。换言之，启动与原有程序并行运行的新程序。
"""

import os

parm = 0
while True:
    parm += 1
    pid = os.fork()
    if pid == 0:

        os.execl("/Users/magirui/anaconda/bin/python", "python", "child.py", str(parm))
        assert False, "error starting program"
    else:

        print("Child is", pid)
        if input() == "q":
            break;
