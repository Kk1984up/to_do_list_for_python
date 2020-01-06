# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 20:48:13 2019

@author: libozhang
"""

#CalHamletV1

def getText():
    txt=open("hamlet.txt","r").read()
    txt=txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_'{|}~':
        txt=txt.replace(ch,"")
    return txt
hamletTxt=getText()
words=hamletTxt.split()
counts={}
for word in words:
    counts[word]=counts.get(word,0)+1
    
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count=item[i]
    print("{0:,10}{1:>5}".format(word,count))
    
#%%三国演义人物出场次数的统计
import jieba
txt=open("threekingdoms.txt","r",encoding="utf-8").read
excludes={"将军","却说","荆州","商议","如何","军士","二人","不可","不能"}
words=jieba.lcut(txt)
counts={}
for word in words:
    if len(word)==1:
        continue
    elif word=="诸葛亮" or word=="孔明曰":
        rword="孔明"
    elif word=="关公" or word=="云长":
        rword="关羽"
    elif word=="玄德" or word=="玄德曰":
        rword="刘备"
    elif word=="孟德" or word=="丞相"：:
        rword="曹操"
    else:
        rword=word
    counts[word]=counts.get(rword,0)+1
for word in excludes:
    del counts[word]
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count=items[i]
    print("{0:,10}{1:>5}".format(word,count))
    
#%%绘制七段数码管
    
import turtle
import time

def drawgap():
    turtle.penup()
    turtle.fd(5)
    
def darwLine(draw):
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    turtle.right(90)
def drawDigit(digit):
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
    
    
    
    
def drawDate(date):
    for i in date:
        drawDigit(eval(i))
def main():
    turtle.setup(800,600,0,0)
    turtle.penup()
    turtle()
    
    
    
    
#%%可可雪花

import turtle

def koch(size,n):
    if n==0:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            koch(size/3,n-1)
            
def main():
    turtle.setup(800,600,0,0)
    turtle.up()
    turtle.goto(-300,100)
    turtle.down()
    turtle.delay(0)
    level=5
    koch(600,level)
    turtle.right(120)
    koch(600,level)
    turtle.right(120)
    koch(600,level)
    turtle.hideturtle()
main()
    
    
#%%
import turtle


def draw_brach(brach_length):


    if brach_length > 5:
        if brach_length < 40:
            turtle.color('green')

        else:
            turtle.color('red')

        # 绘制右侧的树枝
        turtle.forward(brach_length)
        print('向前',brach_length)
        turtle.right(25)
        print('右转20')
        draw_brach(brach_length-15)
        # 绘制左侧的树枝
        turtle.left(50)
        print('左转40')
        draw_brach(brach_length-15)

        if brach_length < 40:
            turtle.color('green')

        else:
            turtle.color('red')


        # 返回之前的树枝上
        turtle.right(25)
        print('右转20')
        turtle.backward(brach_length)
        print('返回',brach_length)

def main():
    turtle.left(90)
    turtle.penup()
    turtle.backward(150)
    turtle.pendown()
    turtle.color('red')
    turtle.speed(2)

    draw_brach(100)

    turtle.exitonclick()

if __name__ == '__main__':
    main()




















    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
