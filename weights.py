# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 15:49:25 2019

@author: libozhang
"""

import sys,pygame
from pygame.locals import *
from random import randrange

class Weight(pygame.sprite.Sprite):
    def __init__(self,speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed=speed
        self.image=snake_image#使用到的图像
        self.rect=self.image.get_rect()
        self.reset()
        
    def reset(self):
        """
        将铅锤移到屏幕顶端的随机位置
        """
        self.rect.top=-self.rect.height
        self.rect.centerx=randrange(screen_size[0])
    def update(self):
        self.rect.top+=self.speed
        if self.rect.top>screen_size[1]:
            self.reset()
#初始化
pygame.init()
screen_size=800,600
pygame.display.set_mode(screen_size,FULLSCREEN)
pygame.mouse.set_visible(0)

#加载铅锤图像
snake_image=pygame.image.load('snake.png')
snake_image=snake_image.convert()#just match screen

#set speed
speed=100

#创建一个对象编组，并在其中添加一个weight实例

sprites=pygame.sprite.RenderUpdates()
sprites.add(Weight(speed))

#获取并填充屏幕表面

screen=pygame.display.get_surface()
bg=(100,255,200)#随便设置了一种颜色
screen.fill(bg)
pygame.display.flip()

#用于清除Sprites对象

def clear_callback(surf,rect):
    surf.fill(bg,rect)

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            sys.exit()
        if event.type==KEYDOWN and event.key==K_ESCAPE:
            sys.exit()
    sprites.clear(screen,clear_callback)
    sprites.update()
    updates=sprites.draw(screen)
    pygame.display.update(updates)
    
        
        
