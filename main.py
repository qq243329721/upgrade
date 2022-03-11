"""
@tiele:打飞机
@author:喵
"""
import random
import sys
import time

import imgRect
import pygame
from pygame.locals import *
import traceback
import myPlane
import enemy
import bullet
import supply
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


def add_speed(groups, speed):
    """
    增加groups里所有敌机速度
    :param groups:  敌机组
    :param speed:  速度
    :return:
    """
    for i in groups:
        i.speed += speed


def main():
    # 初始化pygame
    pygame.init()
    # 初始化音乐模块
    pygame.mixer.init()
    # 初始画布大小
    bg_size = width, height = 550, 800

    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)

    screen = pygame.display.set_mode(bg_size)
    # 标题
    pygame.display.set_caption("Demo -- 飞机大战")
    # 背景图片
    background = pygame.image.load(r"spritesheets/gameArts-hd.png")
    # 重新开始图片
    again = pygame.image.load(r"images/again.png").convert_alpha()
    again_rect = again.get_rect()
    again_rect.left, again_rect.top = width // 2 - again_rect.width // 2, height - 350
    # 结束游戏图片
    gameover = pygame.image.load(r"images/gameover.png").convert_alpha()
    gameover_rect = gameover.get_rect()
    gameover_rect.left, gameover_rect.top = width // 2 - gameover_rect.width // 2, height - 300
    # 背景音乐和音效
    pygame.mixer.music.load(r'music/game_music.mp3')
    pygame.mixer.music.play(-1)
    # 子弹
    bullet_out = pygame.mixer.Sound(r'music/bullet.wav')
    bullet_out.set_volume(0.3)
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
    # 无敌时间
    INVINCIBLE_TIME = USEREVENT + 3
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

    # 发射子弹列表
    bullets = []
    # 实例化普通子弹
    bullet1s = []
    # TODO 注意子弹数量, 太少容易打穿屏幕
    # 向上取整
    b = bullet.Bullet1([0, 0])
    bullet_delay = 10
    BULLET1_NUM = math.ceil((height - hero.rect.height - 60) / (bullet_delay * b.speed))
    print(BULLET1_NUM)
    for i in range(BULLET1_NUM):
        # midtop稍微偏了一点, 手动调整
        bullet1s.append(bullet.Bullet1([hero.rect.midtop[0] - 5, hero.rect.midtop[1]]))

    # 实例化超级子弹
    bullet2s = []
    # TODO 注意子弹数量, 太少容易打穿屏幕
    # 向上取整
    # b = bullet.Bullet2([0, 0])
    bullet_delay = 10
    BULLET2_NUM = math.ceil((height - hero.rect.height - 60) / (bullet_delay * b.speed)) * 2
    print(BULLET2_NUM)
    for i in range(BULLET2_NUM):
        # midtop稍微偏了一点, 手动调整
        bullet2s.append(bullet.Bullet2([hero.rect.centerx - 50, hero.rect.midtop[1] + 40]))
        bullet2s.append(bullet.Bullet2([hero.rect.centerx + 35, hero.rect.midtop[1] + 40]))

    # 超级子弹定时器
    DOUBLE_BULLET_TIME = USEREVENT + 2
    double_bullet_flag = False

    # 初始化图片索引
    big_enemy_blowup_img_index = 0
    mid_enemy_blowup_img_index = 0
    small_enemy_blowup_img_index = 0
    hero_blowup_img_index = 0
    bullet1s_img_index = 0
    bullet2s_img_index = 0

    # 统计得分
    score = 0
    small_enemy_score = 1000
    mid_enemy_score = 3000
    big_enemy_score = 5000
    font1 = pygame.font.Font('font/Ruthie-Regular.ttf', 36)
    font2 = pygame.font.Font('font/Ruthie-Regular.ttf', 60)
    # score_font = pygame.font.SysFont("calibri", 50)
    # print(pygame.font.get_fonts())

    # 暂停功能
    paused_flag = False
    pause_nor = pygame.image.load('images/pause_nor.png').convert_alpha()
    pause_pressed = pygame.image.load('images/pause_pressed.png').convert_alpha()
    resume_nor = pygame.image.load('images/resume_nor.png').convert_alpha()
    resume_pressed = pygame.image.load('images/resume_pressed.png').convert_alpha()
    paused_rect = pause_nor.get_rect()
    paused_rect.left, paused_rect.top = width - paused_rect.width - 10, 10
    paused_img = pause_nor

    # 难度级别
    level = 1

    # 补给数量
    bomb_num = 3
    bomb_img = imgRect.get_bomb_img()[0]
    bomb_rect = bomb_img.get_rect()

    # 实例化补给(每30秒)
    bullet_supply = supply.BulletSupply(bg_size)
    bomb_supply = supply.BombSupply(bg_size)
    SUPPLY_TIME = USEREVENT
    pygame.time.set_timer(SUPPLY_TIME, 30 * 1000)
    # 暂停倒计时
    SUPPLY_UNPAUSE_TIME = USEREVENT + 1
    pygame.time.set_timer(SUPPLY_UNPAUSE_TIME, 0)

    # 大型飞机出场个数
    big_enemy_music_count = 0
    # 大型飞机出场音乐是否在播放
    big_enemy_music = False

    # 运行标识
    running = True
    # 游戏死亡界面
    death_flag = False
    # 初始化时钟（用于画面帧数）
    clock = pygame.time.Clock()
    # 切换图片标识
    switch_image = True
    # 手动增加延迟
    delay = 100

    # TODO 测试时停止背景音乐
    # pygame.mixer.music.stop()

    while running:
        # 获取事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # running = False
                pygame.quit()
                sys.exit()
            # 键盘按下事件
            elif event.type == pygame.KEYDOWN:
                # 监控空格键（全屏爆炸）
                if event.key == pygame.K_SPACE:
                    if bomb_num:
                        # TODO 炸弹音效
                        enemy4_out.play()
                        bomb_num -= 1
                        for i in enemies:
                            if i.rect.bottom > 0:
                                i.active = False
                                i.bomb_flag = True

            # 鼠标按下事件
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 点击暂停按钮
                if event.button == 1 and paused_rect.collidepoint(event.pos):
                    if paused_flag:
                        paused_img = pause_pressed
                        pygame.mixer.music.unpause()
                        pygame.mixer.unpause()
                        unpause_time = pygame.time.get_ticks()
                        count_time = int((pause_time - unpause_time) / 1000 % 30)
                        # print('count %s' % count_time)
                        pygame.time.set_timer(SUPPLY_UNPAUSE_TIME, 30 * 1000 - count_time * 1000)
                    else:
                        paused_img = resume_pressed
                        pygame.mixer.music.pause()
                        pygame.mixer.pause()
                        pygame.time.set_timer(SUPPLY_TIME, 0)
                        pause_time = pygame.time.get_ticks()
                    paused_flag = not paused_flag
                # 点击重新开始
                if event.button == 1 and again_rect.collidepoint(event.pos):
                    main()
                # 点击结束游戏
                if event.button == 1 and gameover_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

            # 鼠标移动事件
            elif event.type == pygame.MOUSEMOTION:
                if paused_rect.collidepoint(event.pos):
                    if paused_flag:
                        paused_img = resume_pressed
                    else:
                        paused_img = pause_pressed
                else:
                    if paused_flag:
                        paused_img = resume_nor
                    else:
                        paused_img = pause_nor

            # 补给倒计时(自定义事件)
            elif event.type == SUPPLY_TIME:
                enemy4_down.play()
                if random.choice([0, 1]):
                    bomb_supply.reset()
                else:
                    bullet_supply.reset()
            # 补给倒计时-暂停用(自定义事件)
            elif event.type == SUPPLY_UNPAUSE_TIME:
                enemy4_down.play()
                if random.choice([0, 1]):
                    bomb_supply.reset()
                else:
                    bullet_supply.reset()
                pygame.time.set_timer(SUPPLY_TIME, 30 * 1000)
                pygame.time.set_timer(SUPPLY_UNPAUSE_TIME, 0)

            # 关闭超级子弹
            elif event.type == DOUBLE_BULLET_TIME:
                double_bullet_flag = False
                pygame.time.set_timer(DOUBLE_BULLET_TIME, 0)

            # 关闭无敌
            elif event.type == INVINCIBLE_TIME:
                hero.invincible = False
                pygame.time.set_timer(INVINCIBLE_TIME, 0)

        # 背景
        screen.blit(background, (0, 0), (0, 0, width, height))

        if hero.life_num and not paused_flag:
            # 根据用户分数增加难度
            levels = [1, 2, 3, 4, 5]
            level_scores = [30000, 60000, 130000, 180000, 250000]
            if level == levels[level - 1] and score > level_scores[level - 1]:
                # TODO 难度增加音效
                # game_achievement.play()
                # print(level)
                if level < levels[-1]:
                    level = levels[level]
                else:
                    level = -1
                # 增加5小, 2中, 1大
                add_small_enemies(enemies, small_enemies, 5, bg_size)
                add_mid_enemies(enemies, mid_enemies, 2, bg_size)
                # 所有敌机速度+1
                add_speed(small_enemies, 1)
                add_speed(mid_enemies, 1)
                if level == 3:
                    add_speed(big_enemies, 1)
                    add_big_enemies(enemies, big_enemies, 1, bg_size)
                elif level == 5:
                    add_big_enemies(enemies, big_enemies, 1, bg_size)

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

            # 绘制补给并检查玩家是否获得
            if bomb_supply.active:
                bomb_supply.move()
                screen.blit(bomb_supply.image, bomb_supply.rect)
                if pygame.sprite.collide_mask(bomb_supply, hero):
                    game_achievement.play()
                    if bomb_num < 3:
                        bomb_num += 1
                    bomb_supply.active = False
            if bullet_supply.active:
                bullet_supply.move()
                screen.blit(bullet_supply.image, bullet_supply.rect)
                if pygame.sprite.collide_mask(bullet_supply, hero):
                    game_achievement.play()
                    double_bullet_flag = True
                    pygame.time.set_timer(DOUBLE_BULLET_TIME, 6 * 1000)
                    bullet_supply.active = False

            # 绘制子弹(10帧一次)
            if not (delay % bullet_delay):
                # 俩种子弹
                if double_bullet_flag:
                    _bullet = bullets[0]
                    if isinstance(_bullet, bullet.Bullet1) and len(bullets) > BULLET2_NUM:
                        bullets.pop(0)
                    elif isinstance(_bullet, bullet.Bullet1):
                        bullets.pop(0)
                        bullets.append(bullet2s[bullet2s_img_index])
                        bullets.append(bullet2s[bullet2s_img_index + 1])
                        bullet2s_img_index = (bullet2s_img_index + 2) % BULLET2_NUM
                        bullets[-2].reset([hero.rect.centerx - 50, hero.rect.midtop[1] + 40])
                        bullets[-1].reset([hero.rect.centerx + 35, hero.rect.midtop[1] + 40])
                    elif isinstance(_bullet, bullet.Bullet2) and len(bullets) == BULLET2_NUM:
                        bullets[bullet2s_img_index].reset([hero.rect.midtop[0] - 50, hero.rect.midtop[1] + 40])
                        bullets[bullet2s_img_index + 1].reset([hero.rect.midtop[0] + 35, hero.rect.midtop[1] + 40])
                        bullet2s_img_index = (bullet2s_img_index + 2) % BULLET2_NUM
                    bullet_out.play()
                else:
                    if len(bullets) > 0:
                        _bullet = bullets[0]
                        if isinstance(_bullet, bullet.Bullet2) and len(bullets) > BULLET1_NUM:
                            bullets.pop(0)
                            bullets.pop(1)
                            bullets.append(bullet1s[bullet1s_img_index])
                            bullets[-1].reset([hero.rect.midtop[0] - 5, hero.rect.midtop[1]])
                            bullet1s_img_index = (bullet1s_img_index + 1) % BULLET1_NUM
                        elif isinstance(_bullet, bullet.Bullet2) and len(bullets) <= BULLET1_NUM:
                            bullets.pop(0)
                            bullets.append(bullet1s[bullet1s_img_index])
                            bullets[-1].reset([hero.rect.midtop[0] - 5, hero.rect.midtop[1]])
                            bullet1s_img_index = (bullet1s_img_index + 1) % BULLET1_NUM
                        elif isinstance(_bullet, bullet.Bullet1) and len(bullets) <= BULLET1_NUM:
                            # midtop稍微偏了一点, 手动调整
                            bullets[bullet1s_img_index].reset([hero.rect.midtop[0] - 5, hero.rect.midtop[1]])
                            bullet1s_img_index = (bullet1s_img_index + 1) % BULLET1_NUM
                        print('--------')
                    else:
                        bullets = bullet1s[:]
                        # midtop稍微偏了一点, 手动调整
                        bullets[bullet1s_img_index].reset([hero.rect.midtop[0] - 5, hero.rect.midtop[1]])
                        bullet1s_img_index = (bullet1s_img_index + 1) % BULLET1_NUM
                    bullet_out.play()

            # 碰撞检测(子弹-敌机)
            for each in bullets:
                if each.active:
                    # bullet_out.play()
                    each.move()
                    # time.sleep(1)
                    screen.blit(each.image[0], each.rect)
                    bullet1_hit = pygame.sprite.spritecollide(each, enemies, False, pygame.sprite.collide_mask)
                    if bullet1_hit:
                        each.active = False
                        for i in bullet1_hit:
                            if i in mid_enemies or i in big_enemies:
                                i.hit = True
                                # 如果是超级子弹 hp-2
                                if double_bullet_flag:
                                    i.hp -= 2
                                else:
                                    i.hp -= 1
                                if i.hp < 0:
                                    i.active = False
                            else:
                                i.active = False
    
                else:
                    if not (delay % bullet_delay):
                        if double_bullet_flag:
                            # each.reset([hero.rect.centerx - 50, hero.rect.midtop[1] + 20])
                            pass
                        else:
                            # midtop稍微偏了一点, 手动调整
                            each.reset([hero.rect.midtop[0] - 5, hero.rect.midtop[1]])
    
            # 绘制敌方飞机(大 > 中 > 小)
            for each in big_enemies:
                # 炸毁
                if each.bomb_flag:
                    if not (delay % 3):
                        screen.blit(each.blowupImages[big_enemy_blowup_img_index], each.rect)
                        big_enemy_blowup_img_index = (big_enemy_blowup_img_index + 1) % 8
                        # 处理毁灭图片索引切换
                        if not big_enemy_blowup_img_index:
                            # 停止出场音乐
                            big_enemy_music_count -= 1
                            if not big_enemy_music_count:
                                enemy2_out.stop()
                                big_enemy_music = False
                            each.reset()
                            each.active = True
                            each.bomb_flag = False
                            score += big_enemy_score
                    continue
                if each.active:
                    # 存活
                    each.move()
                    # print(each.rect)
                    if each.hit:
                        each.hit = False
                        screen.blit(each.hitImages[0], each.rect)
                    else:
                        if switch_image:
                            screen.blit(each.flyImages[0], each.rect)
                        else:
                            screen.blit(each.flyImages[1], each.rect)
                    if (each.rect.bottom == -50 and each.speed == 1) or \
                            (each.rect.bottom in[-50, -49] and each.speed == 2):
                        # -50距离,如果没有播放出场音乐, 开始播放
                        if not big_enemy_music:
                            enemy2_out.play(-1)
                            big_enemy_music = True
                        big_enemy_music_count += 1
                        print(big_enemy_music_count, big_enemy_music)

                    # 绘制血量
                    pygame.draw.line(screen, BLACK, (each.rect.left, each.rect.top + each.rect.height + 5),
                                    (each.rect.right, each.rect.top + each.rect.height + 5), 2)
                    # 血量小于20%变成红色, 否则绿色
                    hp_ratio = each.hp / enemy.BigEnemy.hp
                    if hp_ratio > 0.2:
                        pygame.draw.line(screen, GREEN, (each.rect.left, each.rect.top + each.rect.height + 5),
                                         (each.rect.left + each.rect.width * hp_ratio, each.rect.top + each.rect.height
                                         + 5), 2)
                    else:
                        pygame.draw.line(screen, RED, (each.rect.left, each.rect.top + each.rect.height + 5),
                                         (each.rect.left + each.rect.width * hp_ratio, each.rect.top + each.rect.height
                                         + 5), 2)
    
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
                            big_enemy_music_count -= 1
                            if not big_enemy_music_count:
                                enemy2_out.stop()
                                big_enemy_music = False
                            each.reset()
                            each.active = True
                            score += big_enemy_score
    
            for each in mid_enemies:
                # 炸毁
                if each.bomb_flag:
                    if not (delay % 3):
                        screen.blit(each.blowupImages[mid_enemy_blowup_img_index], each.rect)
                        mid_enemy_blowup_img_index = (mid_enemy_blowup_img_index + 1) % 4
                        # 处理毁灭图片索引切换
                        if not mid_enemy_blowup_img_index:
                            each.reset()
                            each.active = True
                            each.bomb_flag = False
                            score += mid_enemy_score
                    continue
                if each.active:
                    # 存活
                    each.move()
                    if each.hit:
                        screen.blit(each.hitImages[0], each.rect)
                        each.hit = False
                    else:
                        screen.blit(each.flyImages[0], each.rect)
                    # 绘制血量
                    pygame.draw.line(screen, BLACK, (each.rect.left, each.rect.top + each.rect.height + 5),
                                     (each.rect.right, each.rect.top + each.rect.height + 5), 2)
                    # 血量小于20%变成红色, 否则绿色
                    hp_ratio = each.hp / enemy.MidEnemy.hp
                    if hp_ratio > 0.2:
                        pygame.draw.line(screen, GREEN, (each.rect.left, each.rect.top + each.rect.height + 5),
                                         (each.rect.left + each.rect.width * hp_ratio, each.rect.top + each.rect.height
                                         + 5), 2)
                    else:
                        pygame.draw.line(screen, RED, (each.rect.left, each.rect.top + each.rect.height + 5),
                                         (each.rect.left + each.rect.width * hp_ratio, each.rect.top + each.rect.height
                                          + 5), 2)
                else:
                    # 毁灭
                    if not (delay % 3):
                        if not mid_enemy_blowup_img_index:
                            # 播放毁灭音效
                            enemy3_down.play()
                        screen.blit(each.blowupImages[mid_enemy_blowup_img_index], each.rect)
                        mid_enemy_blowup_img_index = (mid_enemy_blowup_img_index + 1) % 4
                        # 处理毁灭图片索引切换
                        if not mid_enemy_blowup_img_index:
                            each.reset()
                            each.active = True
                            score += mid_enemy_score
    
            for each in small_enemies:
                # 炸毁
                if each.bomb_flag:
                    if not (delay % 3):
                        screen.blit(each.blowupImages[small_enemy_blowup_img_index], each.rect)
                        small_enemy_blowup_img_index = (small_enemy_blowup_img_index + 1) % 4
                        # 处理毁灭图片索引切换
                        if not small_enemy_blowup_img_index:
                            each.reset()
                            each.active = True
                            each.bomb_flag = False
                            score += small_enemy_score
                    continue
                if each.active:
                    # 存活
                    each.move()
                    screen.blit(each.flyImages[0], each.rect)
                else:
                    # 毁灭
                    if not (delay % 3):
                        if not small_enemy_blowup_img_index:
                            # 播放毁灭音效
                            enemy1_down.play()
                        screen.blit(each.blowupImages[small_enemy_blowup_img_index], each.rect)
                        small_enemy_blowup_img_index = (small_enemy_blowup_img_index + 1) % 4
                        # 处理毁灭图片索引切换
                        if not small_enemy_blowup_img_index:
                            each.reset()
                            each.active = True
                            score += small_enemy_score
    
            # 碰撞检测(敌机-英雄)
            enemies_blowup = pygame.sprite.spritecollide(hero, enemies, False, pygame.sprite.collide_mask)
            if enemies_blowup:
                # 是否无敌
                if not hero.invincible:
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
                    screen.blit(hero.blowupImages[hero_blowup_img_index], hero.rect)
                    hero_blowup_img_index = (hero_blowup_img_index + 1) % 4
                    # 处理毁灭图片索引切换
                    if hero_blowup_img_index == 0:
                        hero.life_num -= 1
                        if hero.life_num:
                            hero.reset()
                            pygame.time.set_timer(INVINCIBLE_TIME, 3 * 1000)
            # 左下角绘制炸弹数量
            bomb_text = font1.render('x  %d' % bomb_num, True, WHITE)
            screen.blit(bomb_text, (10 + bomb_rect.width + 10, height - bomb_rect.height))
            screen.blit(bomb_img, (10, height - 10 - bomb_rect.height))

            # 右下角绘制剩余生命
            if hero.life_num:
                for i in range(hero.life_num):
                    screen.blit(hero.life_img, (width - 10 - (i + 1) * hero.life_rect.width,
                                                height - 10 - hero.life_rect.height))
            # 绘制得分
            score_text = font1.render('Score : %s' % str(score), True, WHITE)
            screen.blit(score_text, (10, 5))

        # 游戏结束画面
        elif not hero.life_num:
            if not death_flag:
                death_flag = True
                # 停止音乐
                pygame.mixer.music.stop()
                pygame.mixer.stop()
                pygame.time.set_timer(SUPPLY_TIME, 0)
    
                # 读取历史最高分
                try:
                    with open('record.txt', 'r') as f:
                        record_score = int(f.read())
                except FileNotFoundError:
                    with open('record.txt', 'w') as f:
                        f.write('0')
                        record_score = 0
                except ValueError:
                    record_score = 0
                # 如果当前分数大于历史分则写入
                if record_score < score:
                    with open('record.txt', 'w') as f:
                        f.write(str(score))
            # 绘制结束画面
            screen.blit(background, (0, 0), (0, 0, width, height))
            death_text1 = font1.render('Record Score : %s' % str(record_score), True, WHITE)
            screen.blit(death_text1, (50, 30))
            death_text1 = font2.render('You Score', True, WHITE)
            screen.blit(death_text1, (width // 2 - font2.size('You Score')[0] // 2, 200))
            death_text2 = font2.render(str(score), True, WHITE)
            screen.blit(death_text2, (width // 2 - font2.size(str(score))[0] // 2, 270))
            screen.blit(again, again_rect)
            screen.blit(gameover, gameover_rect)

        # 绘制暂停按钮(失败页面不需要显示)
        if not death_flag:
            screen.blit(paused_img, paused_rect)

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







