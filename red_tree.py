# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 20:55:54 2019

@author: libozhang
"""

import turtle as tl
import random


def koch(size,n):
    if n==0:
        tl.fd(size)
    else:
        for angle in [0,60,-120,60]:
            tl.left(angle)
            koch(size/3,n-1)
def tree(length,angel,k):
    if length>10:
        if length<40:
            tl.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        else:
            tl.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        if 0<length<=30:
            tl.pensize(2)
        elif 30<length<=90:
            tl.pensize(4)
        elif 90<length<=160:
            tl.pensize(8)
        else:
            tl.pensize(16)
        tl.fd(length)
        tl.right(angel)
        tree(length*k,angel,k)
        tl.left(angel*2)
        tree(length*k,angel,k)
        if length<40:
            tl.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        else:
            tl.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        tl.right(angel)
        tl.backward(length)     


def snowflake():
    tl.begin_fill()
    tl.colormode(255)
    tl.color((210,230,255),(220,240,255))
    for i in range(3):
        koch(20,4)
        tl.right(120)
    tl.end_fill()
    tl.up()
    
def main():
    tl.setup(960,480,0,0)
    tl.pensize(1)
    tl.speed(100)
    for i in range(20):
        tl.up()
        tl.goto(random.randint(-200,200),random.randint(20,220))
        tl.down()
        snowflake()
        tl.up()
    tl.goto(0,-240)
    tl.left(90)
    tl.down()
    tl.pensize(5)
    length=200
    angel=36
    k=0.60
    tree(length,angel,k)
    tl.done()
if __name__ == '__main__':
    main()










