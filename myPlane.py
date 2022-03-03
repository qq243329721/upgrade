"""
@title:我方飞机
@author:喵
"""

import pygame
import sys
from pygame.locals import *
import imgRect


# 继承Sprite（碰撞检测）
class MyPlane(pygame.sprite.Sprite):
    """
    我方飞机
    """
    # 初始化
    def __init__(self, gb_size):
        # 调用父类的初始化
        pygame.sprite.Sprite.__init__(self)
        # 飞机图片（突突突）
        self.flyImages = imgRect.getMyPlaneFlyImg()
        # 飞机爆炸图片
        self.blowupImages = imgRect.getMyPlaneBlowupImg()
        # 获取飞机矩形
        self.rect = self.flyImages[0].get_rect()
        # 最大屏幕
        self.width, self.height = gb_size[0], gb_size[1]
        # 生成位置
        self.rect.left, self.rect.top = (self.width - self.rect.width) // 2, self.height - self.rect.height - 60
        # 速度
        self.speed = 10
        # 存活标志
        self.active = True
        # mash 碰撞检测区域
        self.image = self.flyImages[0]
        self.mash = pygame.mask.from_surface(self.image)

    def moveUp(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        else:
            self.rect.top -= self.speed

    def moveDown(self):
        if self.rect.bottom >= self.height - 60:  # 因为飞机不能到最底部, 需要有60的高度
            self.rect.bottom = self.height - 60
        else:
            self.rect.bottom += self.speed

    def moveLeft(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed

    def moveRight(self):
        if self.rect.right >= self.width:
            self.rect.right = self.width
        else:
            self.rect.right += self.speed


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("抠图测试")
    screen = pygame.display.set_mode((400, 600))
    bk = pygame.image.load(r"spritesheets/gameArts-hd.png")
    clock = pygame.time.Clock()
    myPlaneRunning = 1
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(bk, (0, 0))
        if myPlaneRunning:
            screen.blit(imgRect.getMyPlaneFlyImg()[0], (0, 0))
            myPlaneRunning = 0
        else:
            screen.blit(imgRect.getMyPlaneFlyImg()[1], (0, 0))
            myPlaneRunning = 1
        pygame.display.flip()
        clock.tick(10)


