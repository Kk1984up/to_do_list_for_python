# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 00:19:24 2019

@author: libozhang
"""

import turtle


def star(a):
    turtle.pensize(1)
    turtle.begin_fill()
    turtle.color("yellow","yellow")
    turtle.speed(0)
    for i in range(5):
        turtle.forward(a)
        turtle.right(144)
    turtle.end_fill()

def star_bg():
    turtle.bgcolor("red")
    turtle.setup(960,640,0,0)
    turtle.pencolor("black")
    turtle.speed(0)
    x=-480
    y=-320
    for i in range(20):
        turtle.up()
        turtle.goto(x,y)
        turtle.down()
        turtle.fd(960)
        y+=32
    turtle.seth(270)
    for i in range(30):
        turtle.up()
        turtle.goto(x,y)
        turtle.down()
        turtle.fd(640)
        x+=32
    turtle.up()
    turtle.home()
        

def main():
    star_bg()
    turtle.up()
    turtle.goto(-320,160)
    turtle.left(162)
    turtle.fd(96)
    turtle.down()
    turtle.right(162)
    star(182)
    turtle.up()
    turtle.goto(-160,32)
    turtle.fd(32)
    turtle.down()
    turtle.right(162)
    star(60.8)
    turtle.up()
    turtle.goto(-96,96)
    turtle.seth(162)
    turtle.fd(32)
    turtle.right(162)
    star(60.8)
    turtle.goto(-96,192)
    turtle.seth(188.6)
    turtle.fd(32)
    turtle.right(162)
    star(60.8)
    turtle.goto(-160,258)
    turtle.seth(211)
    turtle.fd(32)
    turtle.right(162)
    star(60.8)
    turtle.hideturtle()
    turtle.done()
        
if __name__ == "__main__":
    main()
    mainloop()    
    