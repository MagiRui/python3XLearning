#!/usr/bin/env python
#coding:utf8
#author:MagiRui


import csv

outputFile = open("output.csv", "w", newline="")
outputWriter = csv.writer(outputFile)
outputWriter.writerow(["spam", "eggs", "bacon", "ham"])
outputWriter.writerow(["Hello, world!", "eggs", "bacon", "ham"])
outputWriter.writerow([1, 2, 3.1415926, 4])
outputFile.close()


#使用制表符来分隔单元格,并希望两倍行距
csvFile = open("example1.csv", "w", newline="")
csvWriter = csv.writer(csvFile)
csvWriter.writerow(["apples", "oranges", "grapes"])
csvWriter.writerow(["spam", "spam", "spam", "spam", "spam"])
csvWriter.writerow(["eggs", "bacon", "ham"])
csvFile.close()