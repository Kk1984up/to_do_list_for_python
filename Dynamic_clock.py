from turtle import *
from datetime import *
 
def Skip(step):
    penup()
    forward(step)
    pendown()
 
def mkHand(name, length):
    #注册Turtle形状，建立表针Turtle
    reset()
    Skip(-length*0.1)
    begin_poly()
    forward(length*1.1)
    end_poly()
    handForm = get_poly()
    register_shape(name, handForm)
 
def Init():
    global secHand, minHand, hurHand, printer
    mode("logo")# 重置Turtle指向北
    #建立三个表针Turtle并初始化
    mkHand("secHand", 120)
    mkHand("minHand",  100)
    mkHand("hurHand", 60)
    secHand = Turtle()
    secHand.shape("secHand")
    secHand.color("blue")
    minHand = Turtle()
    minHand.shape("minHand")
    minHand.color("yellow")
    hurHand = Turtle()
    hurHand.shape("hurHand")
    hurHand.color("red")
    for hand in secHand, minHand, hurHand:
        hand.shapesize(1, 1, 3)
        hand.speed(0)
    #建立输出文字Turtle
    printer = Turtle()
    printer.hideturtle()
    printer.penup()
    
def SetupClock(radius):
    #建立表的外框
    reset()
    pensize(7)
    for i in range(60):
        Skip(radius)
        if i % 5 == 0:
            forward(20)
            Skip(-radius-20)
        else:
            dot(5)
            Skip(-radius)
        right(6)
    penup()
    goto(0,165)
    left(90)
    pendown()
    pensize(1)
    color("pink")
    circle(165)
    penup()
    goto(0,160)
    pendown()
    circle(160)
         
def Week(t):    
    week = ["星期一", "星期二", "星期三",
            "星期四", "星期五", "星期六", "星期日"]
    return week[t.weekday()]

def Date(t):
    y = t.year
    m = t.month
    d = t.day
    return "%s %d %d" % (y, m, d)
 
def Tick():
    #绘制表针的动态显示
    t = datetime.today()
    second = t.second + t.microsecond*0.000001
    minute = t.minute + second/60.0
    hour = t.hour + minute/60.0
    secHand.setheading(6*second)
    minHand.setheading(6*minute)
    hurHand.setheading(30*hour)
     
    tracer(False)  
    printer.forward(65)
    printer.write(Week(t), align="center",font=("Courier", 14, "bold"))
    printer.back(130)
    printer.write(Date(t), align="center",font=("Courier", 14, "bold"))
    printer.back(40)
    printer.write("自制表盘时钟", align="center",font=("Arial", 14, "normal"))
    printer.home()
    tracer(True)
    ontimer(Tick, 100)#100ms后继续调用tick

import turtle, time
def drawGap(): #绘制数码管间隔
    turtle.penup()
    turtle.fd(1)
def drawLine(draw):   #绘制单段数码管
    drawGap()
    speed(200)
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(5)
    drawGap()
    turtle.right(90)
def drawDigit(d): #根据数字绘制七段数码管
    drawLine(True) if d in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,2,6,7,8,9] else drawLine(False)
    turtle.left(90)
    drawLine(True) if d in [0,1,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,4,6,8] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(-20)
def drawDate(date):
    turtle.pencolor("red")
    for i in date: #根据设置的符号分隔年月日
        if i == '-':
            turtle.write('年',font=("Arial", 12, "normal"))
            turtle.pencolor("green")
            turtle.fd(-25)
        elif i == '=':
            turtle.write('月',font=("Arial", 12, "normal"))
            turtle.pencolor("blue")
            turtle.fd(-25)
        elif i == '+':
            turtle.write('日',font=("Arial", 12, "normal"))
        else:
            drawDigit(eval(i))

def Text():
    turtle.penup()
    goto(-100,200)
    speed(200)
    turtle.pensize(1) 
    t=time.gmtime() #获取系统当前时间
    drawDate(time.strftime('%Y-%m=%d+',t))
    turtle.hideturtle() 
    turtle.done()

def star(a,b):  
    begin_fill()
    color("yellow","yellow")
    speed(100)
    for i in range(5):
        forward(a)
        right(b)
    end_fill()

def fivestar():
    penup()
    goto(-100,-120)
    pendown()
    l=-50
    k=-70
    for m in range(5):
        star(40,144)
        penup()
        goto(l,k)
        pendown()
        l+=50
        k+=50
 
def main():
    tracer(False)
    Init()
    SetupClock(158)
    tracer(True)
    Tick()
    fivestar()
    Text()

main()