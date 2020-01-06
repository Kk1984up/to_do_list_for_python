
#coding=gbk
from tkinter import *
from math import sqrt
import random

def cal(point):
    delta = point[0] - here
    if delta==0:
        return [-1, -1, 1, 0, 0]
    x = point[1]/delta  # x����
    y = point[2]/delta  # y����
    r = point[3]/delta  # ����뾶
    return [x, y, r]

def display_all(widget, star):

    # ���������λ�ü���С
    # Զ��������ڻ�����ײ�
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

    # ÿһ�θ������е�����λ�ü���С
    global here
    here += step
    for i in range(stars):
        while True:

            position = cal(star[i])
            #������Ļ, �ĳ�������, ���꼰�뾶������
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
    # ÿ0.1�����һ��
    process()
    root.after(100,threaded)

width = 1536            #��Ļ����
height = 800            #��Ļ�߶�

step = 1                # ǰ���ٶ�
min_r = 1               # ��С����뾶
max_r = 200             # �������뾶
stars = 1000            # ȫ����������
x_far = 100             # �ǿ������X�����
y_far = width/2*x_far   # �ǿ������Y�����
z_far = height/2*x_far  # �ǿ������Z������
here = 0                # Ŀǰ����ԱX��λ��Ϊ0, ��Ļ��X��1��λ��
x_center = int(width/2) # ��Ļ����X����
y_center = int(height/2)# ��Ļ����Y����
star = [[0,0,0,0,0] for i in range(stars)]  # ��������[x,y,z,r,����ID]

root = Tk()
canvas = Canvas(root, width=width, height=height, bg='black')
canvas.pack()

for i in range(stars):  # �������е����򲿼�

    position = cal(star[i])
    x0 = position[0] - position[2] + width/2
    y0 = position[1] - position[2] + height/2
    x1 = position[0] + position[2] + width/2
    y1 = position[1] + position[2] + height/2

    star[i][4] = canvas.create_oval(x0, y0, x1, y1, fill='white')

# root.bind('<KeyPress>', process)
root.resizable(0, 0)    # ���ô���Ϊ�̶���С, ���ɸı�
threaded()              # ��ʱ�𶯺���Աǰ��

root.mainloop()