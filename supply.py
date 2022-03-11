# -*- coding: UTF-8 -*-
"""
@File       : supply.py
@Author     : MQ
@Time       : 2022/3/10 19:24
@Software   : PyCharm
@fun        : main, 防传播,  
"""

from datetime import datetime

import time

import imgRect
import pygame
from random import *


class BulletSupply(pygame.sprite.Sprite):

    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = imgRect.get_bullet_supply_img()[0]
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        # 可以不用定义, 因为每次reset的时候都会初始化
        # self.rect.left, self.rect.bottom = randint(0, self.width - self.rect.winth), -100
        self.speed = 5
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.active = False

    def reset(self):
        self.active = True
        self.rect.left, self.rect.bottom = randint(0, self.width - self.rect.width), -100


class BombSupply(pygame.sprite.Sprite):

    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = imgRect.get_bomb_supply_img()[0]
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        # 可以不用定义, 因为每次reset的时候都会初始化
        # self.rect.left, self.rect.bottom = randint(0, self.width - self.rect.winth), -100
        self.speed = 5
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.active = False

    def reset(self):
        self.active = True
        self.rect.left, self.rect.bottom = randint(0, self.width - self.rect.width), -100



