# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 18:28:01 2019

@author: libozhang
"""

#BMI计算公式

height,weight=eval(input("请输入身高m和体重kg，用逗号隔开,"))

bmi=weight/pow(height,2)
h1=""
h2=""
if bmi<18:
    h1,h2="偏瘦","偏瘦"
elif 18<=bmi<24:
    h1,h2="正常","正常"
elif 24<=bmi<25:
    h1,h2="偏胖","正常"
elif 25<=bmi<28:
    h1,h2="偏胖","偏胖"
elif 28<=bmi<29:
    h1,h2="肥胖","偏胖"
elif  29<=bmi<34:
    h1,h2="肥胖","肥胖"
else:
    h1,h2="重度肥胖","重度肥胖"
print("身体指数BMI:{:.4f}".format(bmi))
print("国内标准:{}，国际标准:{}".format(h1,h2))
    
    
    
#%%蒙特卡罗方法计算圆周率
from random import random
from time import perf_counter

D=10000*10000
hits=0.0
start=perf_counter()
for i in range(1,D+1):
    x,y=random(),random()
    dist=pow(x**2+y**2,0.5)
    if dist<=1.0:
        hits+=1
pi=4*(hits/D)
print("圆周率为:{:.8f}".format(pi))
print("运行时间是:{:.6f}s".format(perf_counter()-start))




#%%基本数据统计方法
def getNum():
    nums=[]
    iNumStr=input("请输入数字（回车退出）:")
    while iNumStr!="":
        nums.append(eval(iNumStr))
        iNumStr=input("请输入数字（回车退出）:")
    return nums
def mean(numbers):
    s=0.0
    for num in numbers:
        s=s+num
    return s/len(numbers)
def dev(numbers,mean):
    sdev=0.0
    for num in numbers:
        sdev=sdev+(num-mean)**2
    return pow(sdev/(len(numbers)-1),0.5)
def median(numbers):
    sorted(numbers)
    size=len(numbers)
    if size%2==0:
        med=(numbers[size//2-1]+numbers[size//2])/2
    else:
        med=numbers[size//2]
    return med

n=getNum()
m=mean(n)
print("平均数：{},方差：{:.2},中位数：{}".format(m,dev(n,m),median(n)))

    
        
        
        



















