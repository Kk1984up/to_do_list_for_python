# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 21:48:31 2019

@author: libozhang
"""

import pygame,sys
pygame.init()
size=width,height=800,600
speed=[1,1]
yellow=0.5,0.6,0.7
screen=pygame.display.set_mode(size)
pygame.display.set_caption("PygameBIQIU")
ball=pygame.image.load("snake.png")
ballrect=ball.get_rect()
fps=300
fclock=pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                speed[0]=speed[0] if speed[0]==0 else (abs(speed[0]-1))
            elif event.key==pygame.K_RIGHT:
                speed[0]=speed[0]+1 if speed[0]>0 else speed[0]-1
            elif event.key==pygame.K_UP:
                speed[1]=speed[1]+1 if speed[1]>0 else speed[1]-1
            elif event.key==pygame.K_DOWN:
                speed[1]=speed[1] if speed[1]==0 else (abs(speed[1]-1))*int(speed[1]/abs(speed[1]))
                
    ballrect=ballrect.move(speed[0],speed[1])
    if ballrect.left<0 or ballrect.right>width:
        speed[0]=-speed[0]
    if ballrect.top<0 or ballrect.bottom>height:
        speed[1]=-speed[1]
    screen.fill(yellow)
    screen.blit(ball,ballrect)
    pygame.display.update()
    fclock.tick(fps)