# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 22:57:47 2019

@author: libozhang
"""

from turtle import *
from random import *


def snow():
    hideturtle()
    pensize(3)
    speed(100)
    for i in range(100):
        r=random()
        g=random()
        b=random()
        pencolor(r,g,b)
        penup()
        setx(randint(-350,350))
        sety(randint(1,270))
        pendown()
        dens=randint(8,12)
        snowsize=randint(10,14)
        for j in range(dens):
            forward(snowsize)
            backward(snowsize)
            right(360/dens)
def ground():
    hideturtle()
    speed(100)
    for i in range(300):
        pensize(randint(5,10))
        x=randint(-350,350)
        y=randint(-300,-1)
        r=-y/300
        g=-y/300
        b=-y/300
        pencolor((r,g,b))
        penup()
        goto(x,y)
        pendown()
        forward(randint(20,200))
def main():
    setup(800,600,0,0)
    tracer(False)
    bgcolor(0.5,0.5,0.6)
    snow()
    ground()
    tracer(True)
    mainloop()

main()
