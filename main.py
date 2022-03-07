"""
@tiele:打飞机
@author:喵
"""
import sys
import time

import pygame
from pygame.locals import *
import traceback
import myPlane
import enemy
import bullet
import math


def add_small_enemies(groups, sort_group, num, _bg_size):
    """
    生成小型飞机，并加入到组中
    :param groups:大组（碰撞检测）
    :param sort_group:种类组（同类型飞机处理）
    :param num:初始飞机数量
    :param _bg_size:背景
    :return:
    """
    for i in range(num):
        small_enemy = enemy.SmallEnemy(_bg_size)
        groups.add(small_enemy)
        sort_group.add(small_enemy)


def add_mid_enemies(groups, sort_group, num, _bg_size):
    """
    生成中型飞机，并加入到组中
    :param groups:大组（碰撞检测）
    :param sort_group:种类组（同类型飞机处理）
    :param num:初始飞机数量
    :param _bg_size:背景
    :return:
    """
    for i in range(num):
        mid_enemy = enemy.MidEnemy(_bg_size)
        groups.add(mid_enemy)
        sort_group.add(mid_enemy)


def add_big_enemies(groups, sort_group, num, _bg_size):
    """
    生成小型飞机，并加入到组中
    :param groups:大组（碰撞检测）
    :param sort_group:种类组（同类型飞机处理）
    :param num:初始飞机数量
    :param _bg_size:背景
    :return:
    """
    for i in range(num):
        big_enemy = enemy.BigEnemy(_bg_size)
        groups.add(big_enemy)
        sort_group.add(big_enemy)


def main():
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
    pygame.mixer.music.play(-1)
    # 子弹
    bullet_out = pygame.mixer.Sound(r'music/bullet.wav')
    bullet_out.set_volume(0.5)
    # 其余声效
    enemy1_down = pygame.mixer.Sound(r'music/enemy1_down.wav')
    enemy1_down.set_volume(0.5)
    enemy2_down = pygame.mixer.Sound(r'music/enemy2_down.wav')
    enemy2_down.set_volume(0.5)
    enemy2_out = pygame.mixer.Sound(r'music/enemy2_out.wav')
    enemy2_out.set_volume(0.5)
    enemy3_down = pygame.mixer.Sound(r'music/enemy3_down.wav')
    enemy3_down.set_volume(0.5)
    enemy4_down = pygame.mixer.Sound(r'music/enemy4_down.wav')
    enemy4_down.set_volume(0.5)
    enemy4_out = pygame.mixer.Sound(r'music/enemy4_out.wav')
    enemy4_out.set_volume(0.5)
    enemy5_down = pygame.mixer.Sound(r'music/enemy5_down.wav')
    enemy5_down.set_volume(0.5)
    game_achievement = pygame.mixer.Sound(r'music/game_achievement.wav')
    game_achievement.set_volume(0.5)
    game_over = pygame.mixer.Sound(r'music/game_over.wav')
    game_over.set_volume(0.5)

    # 实例化我方飞机
    hero = myPlane.MyPlane(bg_size)
    # 记录飞机初始化位置
    hero_init_rect = hero.rect
    print(hero_init_rect)
    # 存放敌方所有飞机
    enemies = pygame.sprite.Group()
    # 存放敌方小型飞机
    small_enemies = pygame.sprite.Group()
    add_small_enemies(enemies, small_enemies, 10, bg_size)
    # 存放敌方中型飞机
    mid_enemies = pygame.sprite.Group()
    add_mid_enemies(enemies, mid_enemies, 4, bg_size)
    # 存放敌方大型飞机
    big_enemies = pygame.sprite.Group()
    add_big_enemies(enemies, big_enemies, 1, bg_size)

    # 实例化子弹
    bullet1s = []
    # TODO 注意子弹数量, 太少容易打穿屏幕
    # 向上取整
    b = bullet.Bullet1([0, 0])
    bullet_delay = 20
    BULLET_NUM = math.ceil((height - hero.rect.height - 60) / (bullet_delay * b.speed))
    print(BULLET_NUM)
    for i in range(BULLET_NUM):
        # midtop稍微偏了一点, 手动调整
        bullet1s.append(bullet.Bullet1([hero.rect.midtop[0] - 5, hero.rect.midtop[1]]))

    # 初始化图片索引
    big_enemy_blowup_img_index = 0
    mid_enemy_blowup_img_index = 0
    small_enemy_blowup_img_index = 0
    hero_blowup_img_index = 0
    bullet1s_img_index = 0
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
                # running = False
                pygame.quit()
                sys.exit()
            # 监控空格键（全屏爆炸）
            if event.type == pygame.K_SPACE:
                running = False
                pass
            if event.type == pygame.K_ESCAPE:
                running = False
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

        # 绘制子弹(10帧一次)
        if not (delay % bullet_delay):
            # midtop稍微偏了一点, 手动调整
            bullet1s[bullet1s_img_index].reset([hero.rect.midtop[0] - 5, hero.rect.midtop[1]])
            bullet1s_img_index = (bullet1s_img_index + 1) % BULLET_NUM

        # 碰撞检测(子弹-敌机)
        for each in bullet1s:
            if each.active:
                each.move()
                # time.sleep(1)
                screen.blit(each.image[0], each.rect)
                bullet1_hit = pygame.sprite.spritecollide(each, enemies, False, pygame.sprite.collide_mask)
                if bullet1_hit:
                    each.active = False
                    for i in bullet1_hit:
                        i.active = False

            else:
                if not (delay % bullet_delay):
                    # midtop稍微偏了一点, 手动调整
                    each.reset([hero.rect.midtop[0] - 5, hero.rect.midtop[1]])

        # 绘制敌方飞机(大 > 中 > 小)
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
                    enemy2_out.play(-5)
            else:
                # 毁灭
                if not (delay % 3):
                    if not big_enemy_blowup_img_index:
                        # 播放毁灭音乐
                        enemy2_down.play()
                    screen.blit(each.blowupImages[big_enemy_blowup_img_index], each.rect)
                    big_enemy_blowup_img_index = (big_enemy_blowup_img_index + 1) % 8
                    # 处理毁灭图片索引切换
                    if not big_enemy_blowup_img_index:
                        # 停止出场音乐
                        enemy2_out.stop()
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
                    if not mid_enemy_blowup_img_index:
                        enemy3_down.play()
                    screen.blit(each.blowupImages[mid_enemy_blowup_img_index], each.rect)
                    mid_enemy_blowup_img_index = (mid_enemy_blowup_img_index + 1) % 4
                    # 处理毁灭图片索引切换
                    if not mid_enemy_blowup_img_index:
                        each.reset()
                        each.active = True

        for each in small_enemies:
            # print(id(each))
            if each.active:
                # 存活
                each.move()
                screen.blit(each.flyImages[0], each.rect)
            else:
                # 毁灭
                if not (delay % 3):
                    if not small_enemy_blowup_img_index:
                        enemy1_down.play()
                    screen.blit(each.blowupImages[small_enemy_blowup_img_index], each.rect)
                    small_enemy_blowup_img_index = (small_enemy_blowup_img_index + 1) % 4
                    # 处理毁灭图片索引切换
                    if not small_enemy_blowup_img_index:
                        each.reset()
                        each.active = True

        # 碰撞检测(敌机-英雄)
        enemies_blowup = pygame.sprite.spritecollide(hero, enemies, False, pygame.sprite.collide_mask)

        if enemies_blowup:
            # 碰撞免疫, 简称无敌
            hero.active = False
            for i in enemies_blowup:
                i.active = False

        # 绘制我方飞机
        if hero.active:
            # 我方飞机存活
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
                print(hero.rect)
                screen.blit(hero.blowupImages[hero_blowup_img_index], hero.rect)
                hero_blowup_img_index = (hero_blowup_img_index + 1) % 4
                # 处理毁灭图片索引切换
                if not hero_blowup_img_index:
                    print("Game Over !!")
                    # running = False
                # 初始化飞机位置
                else:
                    hero = myPlane.MyPlane(bg_size)
                    hero.active = True
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
    # 解决Too broad exception clause提示
    # noinspection PyBroadException
    try:
        main()
    except SystemError:
        pass
    except Exception as e:
        traceback.print_exc()
        pygame.quit()
        input()







