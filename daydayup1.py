# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 22:58:59 2019

@author: libozhang
"""

#daydayupQ3
dayfactor=0.01
dayup=1.0
for i in range(365):
    if i%7 in [6,0]:
        dayup=dayup*(1-dayfactor)
    else:
        dayup=dayup*(1+dayfactor)
print("工作日的力量:{:4f}".format(dayup))
#%%daydayupq1
dayfactor=0.005
dayup=pow(1+dayfactor,365)
daydown=pow(1-dayfactor,365)
print("向上的力量:{:.4f},向下:{:.4f}".format(dayup,daydown))

#%%daydayupq4工作日的努力

def dayUP(df):
    dayup=1
    for i in range(365):
        if i%7 in [0,6]:
            dayup=dayup*(1-0.01)
        else:
            dayup=dayup*(1+df)
    return dayup
dayfactor=0.01
while dayUP(dayfactor)<37.78:
    dayfactor+=0.01
print("工作日的努力参数是:{:3f}".format(dayfactor))

#%%获取星期字符串
#Weekstring

weekstr="一二三四五六日"
weekid=eval(input("请输入星期数字:"))
print("星期"+weekstr[weekid-1])

#%%输出星座符号

for i in range(12):
    print(chr(9800+i),end="")

import time
for i in range(101):
    print('\r{:3}%'.format(i),end="")
    time.sleep(0.5)
#%%时间进度条
import time
scale=50
print("执行开始".center(scale//2,"-"))
start=time.perf_counter()
for i in range(scale+1):
    a='*'*i
    b='.'*(scale-i)
    c=(i/scale)*100
    dur=time.perf_counter()-start
    print('\r{:^3.0f}%[{}->{}]{:.2f}s'.format(c,a,b,dur),end="")
    time.sleep(0.1)
print("\n"+"执行结束".center(scale//2,'-'))

















