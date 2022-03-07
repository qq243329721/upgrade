"""
@title:抠图
@author：喵
"""

import pygame
from pygame.locals import *
import sys
import json

pygame.init()
# 获取大图片
bigImg = pygame.image.load(r"spritesheets/gameArts-hd.png")


def getMyPlaneFlyImg():
    """
    获取我方飞机图片
    :return:
    """
    myPlaneFlyImg0 = bigImg.subsurface(868, 1484, 132, 164)
    myPlaneFlyImg1 = bigImg.subsurface(573, 1643, 160, 132)
    myPlaneFlyImg1 = pygame.transform.rotate(myPlaneFlyImg1, 90)
    return [myPlaneFlyImg0.convert_alpha(), myPlaneFlyImg1.convert_alpha()]


def getSmallEnemyFlyImg():
    """
    获取敌方小型飞机图片
    :return:
    """
    # smallEnemyFlyImg0 = bigImg.subsurface(218, 1608, 68, 50)
    return [bigImg.subsurface(218, 1608, 68, 50).convert_alpha()]


def getMidEnemyFlyImg():
    """
    获取敌方中型飞机图片
    :return:
    """
    midEnemyFlyImg0 = bigImg.subsurface(733, 1695, 116, 92)
    midEnemyFlyImg0 = pygame.transform.rotate(midEnemyFlyImg0, 90)
    return [midEnemyFlyImg0.convert_alpha()]


def getBigEnemyFlyImg():
    """
    获取敌方中型飞机图片
    :return:
    """
    bigEnemyFlyImg0 = bigImg.subsurface(332, 1136, 219, 328)
    bigEnemyFlyImg1 = bigImg.subsurface(0, 1136, 332, 219)
    bigEnemyFlyImg1 = pygame.transform.rotate(bigEnemyFlyImg1, 90)
    return [bigEnemyFlyImg0.convert_alpha(), bigEnemyFlyImg1.convert_alpha()]


def getMyPlaneBlowupImg():
    """
    获取我方飞机爆炸图片
    :return:
    """
    myPlaneBlowupImg0 = bigImg.subsurface(317, 1464, 164, 132)
    myPlaneBlowupImg0 = pygame.transform.rotate(myPlaneBlowupImg0, 90)
    myPlaneBlowupImg1 = bigImg.subsurface(573, 1511, 164, 132)
    myPlaneBlowupImg1 = pygame.transform.rotate(myPlaneBlowupImg1, 90)
    myPlaneBlowupImg2 = bigImg.subsurface(868, 1320, 132, 164)
    myPlaneBlowupImg3 = bigImg.subsurface(0, 1546, 102, 88)
    myPlaneBlowupImg3 = pygame.transform.rotate(myPlaneBlowupImg3, 45)
    return [myPlaneBlowupImg0.convert_alpha(), myPlaneBlowupImg1.convert_alpha(), myPlaneBlowupImg2.convert_alpha(),
            myPlaneBlowupImg3.convert_alpha()]


def getSmallEnemyBlowupImg():
    """
    获取敌方小型飞机爆炸图片
    :return:
    """
    smallEnemyBlowupImg0 = bigImg.subsurface(102, 1622, 68, 50)
    smallEnemyBlowupImg1 = bigImg.subsurface(218, 1546, 68, 62)
    smallEnemyBlowupImg2 = bigImg.subsurface(951, 1809, 68, 76)
    smallEnemyBlowupImg2 = pygame.transform.rotate(smallEnemyBlowupImg2, 90)
    smallEnemyBlowupImg3 = bigImg.subsurface(286, 1596, 64, 60)
    smallEnemyBlowupImg3 = pygame.transform.rotate(smallEnemyBlowupImg3, 315)
    return [smallEnemyBlowupImg0.convert_alpha(), smallEnemyBlowupImg1.convert_alpha(),
            smallEnemyBlowupImg2.convert_alpha(), smallEnemyBlowupImg3.convert_alpha()]


def getMidEnemyBlowupImg():
    """
    获取敌方中型飞机爆炸图片
    :return:
    """
    midEnemyBlowupImg0 = bigImg.subsurface(481, 1464, 92, 124)
    midEnemyBlowupImg1 = bigImg.subsurface(737, 1603, 120, 92)
    midEnemyBlowupImg1 = pygame.transform.rotate(midEnemyBlowupImg1, 90)
    midEnemyBlowupImg2 = bigImg.subsurface(737, 1511, 120, 92)
    midEnemyBlowupImg2 = pygame.transform.rotate(midEnemyBlowupImg2, 90)
    midEnemyBlowupImg3 = bigImg.subsurface(481, 1588, 92, 122)
    return [midEnemyBlowupImg0.convert_alpha(), midEnemyBlowupImg1.convert_alpha(), midEnemyBlowupImg2.convert_alpha(),
            midEnemyBlowupImg3.convert_alpha()]


def getBigEnemyBlowupImg():
    """
    获取敌方打飞机爆炸图片
    :return:
    """
    bigEnemyBlowupImg0 = bigImg.subsurface(640, 1101, 340, 219)
    bigEnemyBlowupImg0 = pygame.transform.rotate(bigEnemyBlowupImg0, 90)
    bigEnemyBlowupImg1 = bigImg.subsurface(640, 221, 341, 220)
    bigEnemyBlowupImg1 = pygame.transform.rotate(bigEnemyBlowupImg1, 90)
    bigEnemyBlowupImg2 = bigImg.subsurface(640, 881, 341, 220)
    bigEnemyBlowupImg2 = pygame.transform.rotate(bigEnemyBlowupImg2, 90)
    bigEnemyBlowupImg3 = bigImg.subsurface(640, 661, 341, 220)
    bigEnemyBlowupImg3 = pygame.transform.rotate(bigEnemyBlowupImg3, 90)
    bigEnemyBlowupImg4 = bigImg.subsurface(640, 441, 341, 220)
    bigEnemyBlowupImg4 = pygame.transform.rotate(bigEnemyBlowupImg4, 90)
    bigEnemyBlowupImg5 = bigImg.subsurface(640, 0, 341, 221)
    bigEnemyBlowupImg5 = pygame.transform.rotate(bigEnemyBlowupImg5, 90)
    bigEnemyBlowupImg6 = bigImg.subsurface(0, 1355, 269, 191)
    bigEnemyBlowupImg6 = pygame.transform.rotate(bigEnemyBlowupImg6, 90)
    bigEnemyBlowupImg7 = bigImg.subsurface(599, 1320, 269, 191)
    bigEnemyBlowupImg7 = pygame.transform.rotate(bigEnemyBlowupImg7, 90)
    return [bigEnemyBlowupImg0.convert_alpha(), bigEnemyBlowupImg1.convert_alpha(), \
            bigEnemyBlowupImg2.convert_alpha(), bigEnemyBlowupImg3.convert_alpha(), \
            bigEnemyBlowupImg4.convert_alpha(), bigEnemyBlowupImg5.convert_alpha(), \
            bigEnemyBlowupImg6.convert_alpha(), bigEnemyBlowupImg7.convert_alpha()]


def getBombImg():
    """
    获得炸弹补给图片
    :return:
    """
    return [bigImg.subsurface(857, 1648, 137, 79).convert_alpha()]


def getBulletImg():
    """
    获得子弹补给图片
    :return:
    """
    return [bigImg.subsurface(102, 1546, 116, 76).convert_alpha()]


def get_bullet1_img():
    """
    获取1号子弹图片
    :return:
    """
    position = '{{1009, 0}, {12, 28}}'
    t = position.replace('{', '[').replace('}', ']')
    rect = json.loads(t)
    return [bigImg.subsurface(rect[0][0], rect[0][1], rect[1][0], rect[1][1]).convert_alpha()]


def get_enemy2_hit_img():
    """
    大型飞机击中图片
    :return:
    """
    position = '{{640, 1101}, {340, 219}}'
    t = position.replace('{', '[').replace('}', ']')
    rect = json.loads(t)
    return [pygame.transform.rotate(bigImg.subsurface(rect[0][0], rect[0][1], rect[1][0], rect[1][1]), 90).convert_alpha()]


def get_enemy3_hit_img():
    """
    中型飞机击中图片
    :return:
    """
    position = '{{481, 1464}, {92, 124}}'
    t = position.replace('{', '[').replace('}', ']')
    rect = json.loads(t)
    return [bigImg.subsurface(rect[0][0], rect[0][1], rect[1][0], rect[1][1]).convert_alpha()]


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("抠图测试")
    screen = pygame.display.set_mode((600, 600))
    bk = pygame.image.load(r"spritesheets/gameArts-hd.png")
    clock = pygame.time.Clock()
    myPlaneRunning = 1
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(bk, (0, 0))

        '''
        if myPlaneRunning == 1:
            screen.blit(getSmallEnemyBlowupImg()[0], (0, 0))
            myPlaneRunning = 2
        elif myPlaneRunning == 2:
            screen.blit(getSmallEnemyBlowupImg()[1], (0, 0))
            myPlaneRunning = 3
        elif myPlaneRunning == 3:
            screen.blit(getSmallEnemyBlowupImg()[2], (0, 0))
            myPlaneRunning = 4
        elif myPlaneRunning == 4:
            screen.blit(getSmallEnemyBlowupImg()[3], (0, 0))
            myPlaneRunning = 1
        '''
        r = '{{350, 1596}, {58, 56}}'
        # rect = '{{981, 0}, {28, 96}}'
        r = r.replace('{', '[').replace('}', ']')
        r = json.loads(r)

        img = bigImg.subsurface(r[0][0], r[0][1], r[1][0], r[1][1])

        screen.blit(img, (0, 0))
        # screen.blit(getMyPlaneBlowupImg()[3], (200, 200))

        pygame.display.flip()
        clock.tick(1)
