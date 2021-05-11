'''
@tiele:打飞机
@author:喵
'''

import pygame
from pygame.locals import *
import traceback
import myPlane
import enemy
# 初始化pygame
pygame.init()
# 初始化音乐模块
pygame.mixer.init()
# 初始画布大小
bg_size = width, height = 550, 800
screen = pygame.display.set_mode(bg_size)
# 标题
pygame.display.set_caption("Demo -- 飞机大战")
# 背景图片
background = pygame.image.load(r"spritesheets/gameArts-hd.png")
# 背景音乐和音效
pygame.mixer.music.load(r'music/game_music.mp3')
pygame.mixer.music.play()
# 子弹
# bullets = pygame.mixer.Sound(r'music/bullet.mp3')


def add_small_enemies(groups, sort_group, num):
    '''
    生成小型飞机，并加入到组中
    :param groups:大组（碰撞检测）
    :param sort_group:种类组（同类型飞机处理）
    :param num:初始飞机数量
    :return:
    '''
    for i in range(num):
        small_enemy = enemy.SmallEnemy(bg_size)
        groups.add(small_enemy)
        sort_group.add(small_enemy)


def add_mid_enemies(groups, sort_group, num):
    '''
    生成中型飞机，并加入到组中
    :param groups:大组（碰撞检测）
    :param sort_group:种类组（同类型飞机处理）
    :param num:初始飞机数量
    :return:
    '''
    for i in range(num):
        mid_enemy = enemy.MidEnemy(bg_size)
        groups.add(mid_enemy)
        sort_group.add(mid_enemy)


def add_big_enemies(groups, sort_group, num):
    '''
    生成小型飞机，并加入到组中
    :param groups:大组（碰撞检测）
    :param sort_group:种类组（同类型飞机处理）
    :param num:初始飞机数量
    :return:
    '''
    for i in range(num):
        big_enemy = enemy.BigEnemy(bg_size)
        groups.add(big_enemy)
        sort_group.add(big_enemy)


def main():
    # 实例化我方飞机
    hero = myPlane.MyPlane(bg_size)
    # 存放敌方所有飞机
    enemies = pygame.sprite.Group()
    # 存放敌方小型飞机
    small_enemies = pygame.sprite.Group()
    add_small_enemies(enemies, small_enemies, 10)
    # 存放敌方中型飞机
    mid_enemies = pygame.sprite.Group()
    add_mid_enemies(enemies, mid_enemies, 4)
    # 存放敌方大型飞机
    big_enemies = pygame.sprite.Group()
    add_big_enemies(enemies, big_enemies, 1)

    # 爆炸飞机图片索引
    big_enemy_blowup_img_index = 0
    mid_enemy_blowup_img_index = 0
    small_enemy_blowup_img_index = 0
    hero_blowup_img_index = 0
    # 运行标识
    running = True
    # 初始化时钟（用于画面帧数）
    clock = pygame.time.Clock()
    # 切换图片标识
    switch_image = True
    # 手动增加延迟
    delay = 100
    while running:
        # 获取事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # 监控空格键（全屏爆炸）
            if event.type == pygame.K_SPACE:
                pass
        # 监控键盘
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_w] or key_pressed[K_UP]:
            hero.moveUp()
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            hero.moveDown()
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            hero.moveLeft()
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            hero.moveRight()

        # 背景
        screen.blit(background, (0, 0), (0, 0, width, height))

        

        # 生成敌方飞机(大 > 中 > 小)
        for each in big_enemies:
            if each.active:
                # 存活
                each.move()
                # print(each.rect)
                if switch_image:
                    screen.blit(each.flyImages[0], each.rect)
                else:
                    screen.blit(each.flyImages[1], each.rect)
                if each.rect.bottom == -50:
                    # -50距离,播放出场音乐
                    pass
            else:
                #毁灭
                if not (delay % 3):
                    if not big_enemy_blowup_img_index:
                        # 播放毁灭音乐
                        pass
                    screen.blit(each.blowupImages[big_enemy_blowup_img_index],each.rect)
                    big_enemy_blowup_img_index = (big_enemy_blowup_img_index + 1) % 8
                    # 处理毁灭图片索引切换
                    if not big_enemy_blowup_img_index:
                        # 停止出场音乐
                        
                        each.reset()
                        each.active = True

        for each in mid_enemies:
            if each.active:
                # 存活
                each.move()
                screen.blit(each.flyImages[0], each.rect)
            else:
                # 毁灭
                if not (delay % 3):
                    screen.blit(each.blowupImages[mid_enemy_blowup_img_index],each.rect)
                    mid_enemy_blowup_img_index = (mid_enemy_blowup_img_index + 1) % 4
                    # 处理毁灭图片索引切换
                    if not mid_enemy_blowup_img_index:
                        each.reset()
                        each.active = True

        for each in small_enemies:
            if each.active:
                # 存活
                each.move()
                screen.blit(each.flyImages[0], each.rect)
            else:
                # 毁灭
                if not (delay % 3):
                    screen.blit(each.blowupImages[small_enemy_blowup_img_index],each.rect)
                    small_enemy_blowup_img_index = (small_enemy_blowup_img_index + 1) % 4
                    # 处理毁灭图片索引切换
                    if not small_enemy_blowup_img_index:
                        each.reset()
                        each.active = True
                

        #碰撞检测
        enemies_blowup = pygame.sprite.spritecollide(hero, enemies, False, pygame.sprite.collide_mask)
        if enemies_blowup:
            #hero.active = False
            for e in enemies_blowup:
                e.active = False
        
        # 生成我方飞机
        if hero.active:
            #我方飞机存活
            if switch_image:
                screen.blit(hero.flyImages[0], hero.rect)
            else:
                screen.blit(hero.flyImages[1], hero.rect)
            # 切换图片
            if not (delay % 5):
                switch_image = not switch_image
            
        else:
            # 我方飞机毁灭
            if not (delay % 3):
                screen.blit(hero.blowupImages[hero_blowup_img_index], hero.rect)
                hero_blowup_img_index = (hero_blowup_img_index + 1) % 4
                # 处理毁灭图片索引切换
                if not hero_blowup_img_index:
                    print("Game Over !!")
                    running = False
        # 手动延迟
        delay -= 1
        if not delay:
            delay = 100
        # 画面刷新
        pygame.display.flip()
        # 60帧
        clock.tick(60)

    # 根据运行标识，判断是否退出
    if not running:
        pygame.quit()


if __name__ == "__main__":
    try:
        main()
    except SystemError:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()







