"""
@title:敌方飞机
@author：喵
"""

import pygame
import imgRect
from random import *


# 继承Sprite（碰撞检测）
class SmallEnemy(pygame.sprite.Sprite):
    """
    小型飞机
    """
    # 初始化
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.flyImages = imgRect.getSmallEnemyFlyImg()
        self.blowupImages = imgRect.getSmallEnemyBlowupImg()
        self.rect = self.flyImages[0].get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.top, self.rect.left = randint(-5 * self.height, 0), randint(0, self.width - self.rect.width)
        self.speed = 3
        self.active = True
        self.bomb_flag = False
        # mash 碰撞检测区域
        self.image = self.flyImages[0]
        self.mash = pygame.mask.from_surface(self.image)

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.rect.top, self.rect.left = randint(-5 * self.height, 0), randint(0, self.width - self.rect.width)


# 继承Sprite（碰撞检测）
class MidEnemy(pygame.sprite.Sprite):
    """
    中型飞机
    """
    # 初始化血量
    hp = 9

    # 初始化
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        
        self.flyImages = imgRect.getMidEnemyFlyImg()
        self.blowupImages = imgRect.getMidEnemyBlowupImg()
        self.hitImages = imgRect.get_enemy3_hit_img()
        self.rect = self.flyImages[0].get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.top, self.rect.left = randint(-10 * self.height, -2 * self.height), randint(0, self.width - self.rect.width)
        # 速度
        self.speed = 2
        # 存活标志
        self.active = True
        self.bomb_flag = False
        # mash 碰撞检测区域
        self.image = self.flyImages[0]
        self.mash = pygame.mask.from_surface(self.image)
        # 血量
        self.hp = MidEnemy.hp
        # 击中标志
        self.hit = False

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.hp = MidEnemy.hp
        self.rect.top, self.rect.left = randint(-10 * self.height, -2 * self.height), randint(0, self.width - self.rect.width)


# 继承Sprite（碰撞检测）
class BigEnemy(pygame.sprite.Sprite):
    """
    大型飞机
    """
    hp = 20

    # 初始化
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.flyImages = imgRect.getBigEnemyFlyImg()
        self.blowupImages = imgRect.getBigEnemyBlowupImg()
        self.hitImages = imgRect.get_enemy2_hit_img()
        self.rect = self.flyImages[0].get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.top, self.rect.left = randint(-20 * self.rect.height, -4 * self.height), \
                                        randint(0, self.width - self.rect.width)
        self.speed = 1
        self.active = True
        self.bomb_flag = False
        # mash 碰撞检测区域
        self.image = self.flyImages[0]
        self.mash = pygame.mask.from_surface(self.image)
        # 血量
        self.hp = BigEnemy.hp
        # 击中标志
        self.hit = False

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.hp = BigEnemy.hp
        self.rect.top, self.rect.left = randint(-15 * self.rect.height, -5 * self.height), randint(0, self.width - self.rect.width)
