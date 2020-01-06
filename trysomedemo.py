# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 08:24:46 2019

@author: libozhang
"""

for i in range(0,2):
    print(i)
    
k=10000
while k>1:
    print(k)
    k=k/2
    
for i in range(1000,9999):
    s=str(i)
    a0=eval(s[0])
    a1=eval(s[1])
    a2=eval(s[2])
    a3=eval(s[3])
    if (pow(a0,4)+pow(a1,4)+pow(a2,4)+pow(a3,4))==i:
        print(i)   
        
sum=0       
for i in range(2,101):
    for a in range(2,i):
        if i%a==0:
            break
    else:
        sum=sum+i
print(sum)

    
for s in "PYTHON":
   if s=="T":
      continue
   print(s,end="")
#%%
a=int(input("请输入一个整数:"))
print("{:+>30.3f}".format(pow(a,0.5)))

s=input("输入一个字符串:")
s1=s.split("-")
print("{}+{}".format(s1[0],s1[-1]))







#%%产生随机密码
import random

def genpwd(length):
    a=pow(10,(length-1))
    b=pow(10,length)-1
    s=random.randint(a,b)
    return s

length =eval(input("请输入密码位数N:"))
random.seed(17)
for i in range(3):
    print(genpwd(length))
#%%产生连续质数的计算

def prime(m):
    for i in range(2,m):
        if m % i == 0:
            return False
    return True

n = eval(input())
n_ = int(n)
n_ = n_+1 if n_ < n else n_
count = 5

while count > 0:
    if prime(n_):
        if count > 1:
            print(n_, end=",")
        else:
            print(n_, end="")
        count -= 1 
    n_ += 1



















