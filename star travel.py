
#coding=gbk
from tkinter import *
from math import sqrt
import random

def cal(point):
    delta = point[0] - here
    if delta==0:
        return [-1, -1, 1, 0, 0]
    x = point[1]/delta  # x坐标
    y = point[2]/delta  # y坐标
    r = point[3]/delta  # 星球半径
    return [x, y, r]

def display_all(widget, star):

    # 更新星球的位置及大小
    # 远的星球放在画布最底层
    star = sorted(star, reverse=False, key=lambda k:k[0]**2+k[1]**2+k[2]**2)
    for i in range(stars):
        star[i][4]=i+1

    for i in range(stars):
        position = cal(star[i])
        x0 = position[0] - position[2] + width/2
        y0 = position[1] - position[2] + height/2
        x1 = position[0] + position[2] + width/2
        y1 = position[1] + position[2] + height/2
        widget.coords(star[i][4], x0, y0, x1, y1)

def process():

    # 每一次更新所有的星球位置及大小
    global here
    here += step
    for i in range(stars):
        while True:

            position = cal(star[i])
            #超出屏幕, 改成新星球, 坐标及半径都更新
            if (0 <= position[0]+width/2  < width and
                0 <= position[1]+height/2 < height and star[i][0]>here):
                break
            else:
                star[i][0] = random.randint(x_far, 2*x_far)+here
                star[i][1] = random.randint(-y_far, y_far)
                star[i][2] = random.randint(-z_far, z_far)
                star[i][3] = random.randint(min_r, max_r)

    display_all(canvas, star)

def threaded():
    # 每0.1秒更新一次
    process()
    root.after(100,threaded)

width = 1536            #屏幕寛度
height = 800            #屏幕高度

step = 1                # 前进速度
min_r = 1               # 最小星球半径
max_r = 200             # 最大星球半径
stars = 1000            # 全部星球数量
x_far = 100             # 星空中最大X轴距离
y_far = width/2*x_far   # 星空中最大Y轴距离
z_far = height/2*x_far  # 星空中最大Z轴离离
here = 0                # 目前航天员X轴位置为0, 屏幕在X轴1的位置
x_center = int(width/2) # 屏幕中心X坐标
y_center = int(height/2)# 屏幕中心Y坐标
star = [[0,0,0,0,0] for i in range(stars)]  # 星球资料[x,y,z,r,部件ID]

root = Tk()
canvas = Canvas(root, width=width, height=height, bg='black')
canvas.pack()

for i in range(stars):  # 建立所有的星球部件

    position = cal(star[i])
    x0 = position[0] - position[2] + width/2
    y0 = position[1] - position[2] + height/2
    x1 = position[0] + position[2] + width/2
    y1 = position[1] + position[2] + height/2

    star[i][4] = canvas.create_oval(x0, y0, x1, y1, fill='white')

# root.bind('<KeyPress>', process)
root.resizable(0, 0)    # 设置窗口为固定大小, 不可改变
threaded()              # 定时起动航天员前进

root.mainloop()