# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 13:08:58 2019

@author: libozhang
"""

TempStr=input("请输出带有符号的温度值:")
if TempStr[-1] in ['F','f']:
    C=(eval(TempStr[0:-1])-32)/1.8
    print('转换后的温度是{:.4f}C'.format(C))
elif TempStr[-1] in ['C','c']:
    F=1.8*eval(TempStr[0:-1])+32
    print('转换后的温度值是{:.4f}F'.format(F))
else:
    print('输入格式错误')
    
#%%
s=int(input("请输入一个整数"))
if s==0:
    print("Hello World")
elif s>0:
    print("He\nll\no \nWo\nrl\nd")
elif s<0:
    print("H\ne\nl\nl\n \nW\no\nr\nl\nd")
else:
    print("输入错误")