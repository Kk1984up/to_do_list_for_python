# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 14:46:38 2019

@author: libozhang
"""
import turtle
turtle.setup(960,480,0,0)
turtle.penup()
turtle.fd(-450)
turtle.pendown()
turtle.pensize(30)
turtle.pencolor("purple")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done()