#__author__ = 'user'
#coding: utf-8
import sys,os
import linecache
import re
print sys.path[0]
filepath=sys.path[0]+"\\Report\\bv.html"
file=open(filepath)
content=file.readlines()

i=0
for line in content:
    i=i+1
    if line.__contains__("<tr id='total_row'>"):
        break

#获取FAIL的TESTCase数量
FailCasePostion=linecache.getline(filepath,i+4)
FailCaseNumb=int(filter(str.isdigit, FailCasePostion))

#获取ERROR的TESTCase数量
ErrorCasePostion=linecache.getline(filepath,i+5)
ErrorCaseNumb=int(filter(str.isdigit, ErrorCasePostion))

if FailCaseNumb==0 and ErrorCaseNumb==0:
    assert True
else:
    assert False