# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 20:55:05 2019

@author: libozhang
"""

print("hello world")
# %%数字相加
num1=input('输入第一个数字:')
num2=input('输出第二个数字:')
sum=float(num1)+float(num2)
print('数字{0}和数字{1}相加结果为:{2}'.format(num1,num2,sum))

#%%平方根的计算
k=float(input('请输入一个数字：'))
k_sqrt=k**0.5
print('%0.3f的平方根为%0.3f'%(k,k_sqrt))

#%%负数的平方根的计算
import cmath
k=float(input('请输入一个数字:'))
K=cmath.sqrt(k)
print('{0:0.3f}的平方根为{1:0.5f}+{2:0.5f}j'.format(k,K.real,K.imag))

#%%求解一元二次方程ax**2+bx+c=0

import cmath
a=float(input('输入一个系数a:'))
b=float(input('输入一个系数b:'))
c=float(input('输入一个系数c:'))

d=cmath.sqrt(b**2)-(4*a*c)

s1=(-b+d)/(2*a)
s2=(-b-d)/(2*a)
print('结果为{0:0.4f}+{1:0.4f}j和{2:0.4f}+{3:0.4f}j'.format(s1.real,s1.imag,s2.real,s2.imag))

#%%计算三角形的面积

a=float(input('三角形的边长a:'))
b=float(input('三角形的边长b:'))
c=float(input('三角形的表长c:'))
s=(a+b+c)/2
if((a+b)<c):
    print('无法构成三角形')
elif((b+c)<a):
    print("不构成三角形")
elif((a+c)<b):
    print("三角形边长输入有误")
else:
    print('三角形的面积为{0:0.5f}'.format((s*(s-a)*(s-b)*(s-c))**0.5))

#%%计算圆的面积

import sys
import math

def findA(r):
    area=math.pi*r**2
    return area
r=float(input('请输入圆的半径:'))
print('半径为{0:0.2f}的圆面积为{1:0.4f}'.format(r,findA(r)))

#%%产生随机数字并且与你输入的数字比较

import random

i=1
a=random.randint(1,100)
b=int(input('请输入1-10之间的一个数字:'))
while a!=b:
    if a>b:
        print('你第%d个输入的数字小于随机数字'%i)
        b=int(input('请再次输入数字:'))
    else:
        print('你第%d个输入的数字大于随机数字'%i)
        b=int(input('请再次输入数字:'))
    i+=1
else:
    print('恭喜你，你第%d个输入的数字和电脑产生的随机数字%d一样'%(i,b))

#%%华氏度和摄氏度的互相转换
    
a=input('请输入带有符号的温度值:')
if a[-1] in ['f','F']:
    C=(eval(a[0:-1])-32)/1.8
    print('转换后的温度为:{:.3f}C'.format(C))
elif a[-1] in ['c','C']:
    F=1.8*eval(a[0:-1])+32
    print('转换后的温度为:{:.4f}F'.format(F))
else:
    print('你输入的格式有误')
    
#%%互相交换两个数字
x=float(input('输入一个数字x:'))
y=float(input('输入一个数字y:'))
x,y=y,x
print('交换后的x:{0:0.3f}和交换后的数字y:{1:0.4f}'.format(x,y))

#%%判断是不是闰年

year=int(input('请输入一个年份:'))

if (year%4==0):
    if(year%100==0):
        if(year%400==0):
            print('{0}是一个闰年'.format(year))
        else:
            print('{0}不是一个闰年'.format(year))
    else:
        print('{0}是一个闰年'.format(year))
else:
    print('{0}不是一个闰年'.format(year))

#%%判断一个数是不是质数
    
a=int(input('请输入一个自然数：'))
if a>1:
    for i in range(2,a):
        if (a%i==0):
            print(a,'不是质数')
            print(i,'乘以',a//i,'等于',a)
            break
    else:
        print(a,'是一个质数')
else:
    print(a,'不是一个质数')

#%%输出选定范围内的素数
    
a=int(input('输出一个较小的数:'))
b=int(input('输出一个较大的数:'))

for c in range(a,b+1):
    if c>1:
        for i in range(2,c):
            if (c%i==0):
                break
        else:
            print('素数：',c)
    else:
        print('输出错误')
#%%阶乘的算法

a=int(input('请输出一个数字：'))
b=1
if a<0:
    print('负数没有阶乘')
elif a==0:
    print('0的阶乘为1')
else:
    for i in range(1,a+1):
        b=b*i
    print('%d的阶乘为%d'%(a,b))
#%%九九乘法表
for i in range(1, 21):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='')
    print()
#%%输出斐波那契额数列

a=0
b=1

count=int(input('你需要输出前几项？'))

if count<=0:
    print('请输入一个正整数')
else:
    print(0,end=',')
    for i in range(1,count):
      print(b,end=',')
      a,b=b,a+b

#%%显示日历
import calendar

y=int(input('请输入年份：'))
m=int(input('请输入月份：'))

print(calendar.month(y,m))

#%%文件的写入和读取

with open("test.txt", "wt") as out_file:
    out_file.write("把日历写入")
 
# Read a file
with open("test.txt", "rt") as in_file:
    text = in_file.read()
 
print(text)

    
    
    
    
    
    
    