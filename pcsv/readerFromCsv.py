#!/usr/bin/env python
#coding:utf8
#author:MagiRui

import csv

csvRows = []
csvFileObj = open("example1.csv")
readerObj = csv.reader(csvFileObj)
for row in readerObj:

    if readerObj.line_num == 1:

        continue
    csvRows.append(row)
csvFileObj.close()

print(csvRows)