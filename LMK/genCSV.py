#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import csv
import re

pyDir = os.getcwd()
devices = []
def readConf():
    confFile = pyDir+"/running.conf"
    cf = open(confFile,'r')
    lines = cf.readlines()
    cf.close()
    for _device in lines:
        devices.append(_device.strip())

def count(device):
    nfile = pyDir + "/logs/kmsg/" + "output/final_" + device + ".log"
    nf = open(nfile,'r')
    wfile = pyDir + "/logs/kmsg/" + "output/finally_" + device
    lines = nf.readlines()
    target1 = 0
    oline = ""
    for line in lines[target1:]:
        line = line.strip("\t\n\r")
        fw = file(wfile,'a')
        if (re.search(r'[ofree]',line)):
            count = 0
           # print "origin line is: %s" %line
            for _line in lines[target1+1:]:
                if len(lines[target1+1]):
          #          print "the line after origin line is: %s" %_line
                    if (re.search(r'[sigkill]',_line)) or (re.search(r'[Killing]',_line)):
                        count += 1
                        continue
                    else:
 #                       print "****************: %s" %len(line)
                        oline = line + "\t" + str(count)
                        #取出oline中的第一个字段、第五个字段和第六个字段
                        fw.writelines(oline.strip().split('\t',6)[0] + '\t' \
                                    + oline.strip().split('\t',6)[4] + '\t' \
                                    + oline.strip().split('\t',6)[5] + '\n')
                   # print "%s" % oline
                        target1 += 1
                        break
                else:
                    fw.writelines(oline.strip().split('\t',6)[0] + '\t' \
                                + oline.strip().split('\t',6)[4] + '\t' \
                                + oline.strip().split('\t',6)[5] + '\n')
        else:
           target1 += 1
           continue
        fw.close()

# 生成csv文件
def writeM1csv(device):
    mcsvFile = pyDir+"/csv/" + device + "_lowMemKill.csv"
    inputFile = pyDir + "/logs/kmsg/output/finally_" + device
    data = []
    writer = csv.writer(open(mcsvFile,'wb'))
    writer.writerow(['TimeStamp','ma','killcount'])

    inLog = open(inputFile,'r')
    lines = inLog.readlines()
    inLog.close()

    for line in lines:
        if (line.strip().split('\t',3)[2] != "0"):
            data.append(line.strip().split('\t'))
        #   print line


    for item in data:
        writer.writerow(item)

        writer.writerow(item)

def writeM2csv(device):
    Mcsvfile = pyDir+"/csv/" + device + "_MemInfo.csv"
    Memfile = pyDir+"/logs/meminfo/"+device+"/finally"
    data = []
    writer = csv.writer(open(Mcsvfile,'wb'))
    writer.writerow(['TimeStamp','MemeryLeft(KB)','SwapUsed(KB)'])

    fMem = open(Memfile,'r')
    alllines = fMem.readlines()
    fMem.close()
    for eachLine in alllines:
        data.append(eachLine.strip().split("\t"))


    for item in data:
        writer.writerow(item)
#    print data

def writeLcsv(device):
    Lcsvfile = pyDir+"/csv/" + device + "_lostFrame.csv"
    Logfile = pyDir+"/logs/log/new_"+device+".log"
    data = []
    writer = csv.writer(open(Lcsvfile,'wb'))
    writer.writerow(['TimeStamp','Number'])

    fLog = open(Logfile,'r')
    alllines = fLog.readlines()
    fLog.close()

    for line in alllines:
        data.append(line.strip().split("\t"))

    for item in data:
        writer.writerow(item)



# main logic
def main():
    readConf()
    for rdevice in devices:
        try:
            count(rdevice)
            writeM1csv(rdevice)
        except IOError:
            print "Kmsg File does not exists"
        try:
            writeM2csv(rdevice)
        except IOError:
            print "MemInfo File does not exists"
        try:
            writeLcsv(rdevice)
        except IOError:
            print "LogInfo File does not exists"
if __name__=='__main__':
    main()
             
