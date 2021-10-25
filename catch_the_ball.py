import pygame
from pygame.draw import *

from random import *

import numpy as np

pygame.init()

# Параметры шариков
max_ball_radius = 50
min_speed = 2
max_speed = 4
max_angle = 2 * np.pi
ball_quantity = 3
super_ball_quantity = 2

# Цвета используемые в игре
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, CYAN, MAGENTA]
COLORS_NUM = 6



# Настройки прорисовки и экрана
FPS = 24
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))

pygame.display.update()


def new_ball():
    '''
    Функция создаёт новый обычный шарик.
    :return: (списком) координаты центра шарика, его радиус, угол направления движения, скорость, цвет.
    '''

    x = randint(max_ball_radius, width - max_ball_radius)
    y = randint(max_ball_radius, height - max_ball_radius)
    radius = randint(40, max_ball_radius)
    angle = randint(0, int(max_angle))
    speed = randint(min_speed, max_speed)
    color = COLORS[randint(0, COLORS_NUM - 1)]


    return [x, y, radius, angle, speed, color]


def new_super_ball():
    '''
    Функция создаёт новый супер шарик.
    :return:  координаты центра шарика, его радиус, угол направления движения, скорость, цвет
    '''
    x = randint(max_ball_radius, width - max_ball_radius)
    y = randint(max_ball_radius, height - max_ball_radius)
    rad = randint(30, max_ball_radius)
    color = BLACK
    angle = randint(0, int(max_angle))
    speed = max_speed +4

    return [x, y, rad, angle, speed, color]


def ball_load(ball_quantity):
    '''
    Функция выводит на экран определённое число обычных шариков.
    :param ball_quantity: количество обычных шариков в конкретном раунде.
    :return: список из характеристик оставшихся шариков на экране.
    '''
    ball_setup_list = []
    for i in range(ball_quantity):
        list.append(ball_setup_list, list(new_ball()))
    return ball_setup_list


def super_ball_load(super_ball_quantity):
    '''
    Функция выводит на экран определённое число супер шариков.
    :param super_ball_quantity: количество супер шариков в конкретном раунде.
    :return: список из характеристик оставшихся супер шариков на экране.
    '''
    super_ball_setup_list = []
    for i in range(super_ball_quantity):
        list.append(super_ball_setup_list, list(new_super_ball()))
    return super_ball_setup_list


ball_setup_list = ball_load(ball_quantity)
super_ball_setup_list = super_ball_load(super_ball_quantity)


def click_ball(ball, ball_setup_list, event, points, ball_quantity):
    '''
    Функция обеспечивает обработку клика по обычному шарику
    :param ball: параметры текущего шарика.
    :param ball_setup_list: списков списков характеристик обычных шариков.
    :param event: параметр контроля событий мыши.
    :param points: текущее количество очков.
    :param ball_quantity: количество обычных шариков в конкретном раунде.
    :return: списков с характеристиками для всех обычных шариков на экране,
             текущее количество очков,
             количество обычных шариков в конкретном раунде.
    '''
    x = ball[0]
    y = ball[1]
    rad = ball[2]
    distance = (event.pos[0] - x)**2 + (event.pos[1] - y)**2
    if distance <= rad**2:
        points += 1
        del ball_setup_list[ball_setup_list.index(ball)]
    return ball_setup_list, points, ball_quantity



def click_super_ball(super_ball, super_ball_setup_list, event, points, super_ball_quantity):
    '''
    Функция обеспечивает обработку клика по особому шарику.
    :param super_ball: нпараметры текущего супер шарика.
    :param super_ball_setup_list: список с характеристиками для всех супер шариков на экране.
    :param event: параметр контроля событий мыши.
    :param points: текущее количество очков.
    :param super_ball_quantity: количество супер шариков в конкретном раунде.
    :return: список с характеристиками для всех супер шариков на экране,
             текущее количество очков,
             количество обычных шариков в конкретном раунде.
    '''
    x = super_ball[0]
    y = super_ball[1]
    rad = super_ball[2]
    distance = (event.pos[0] - x)**2 + (event.pos[1] - y)**2
    if distance <= rad**2:
        points = points + 3
        del super_ball_setup_list[super_ball_setup_list.index(super_ball)]
    return super_ball_setup_list, points, super_ball_quantity


def balls_moving(ball):
    '''
    Функция заставляет шарики двигаться а так же отскакивать от границ.
    :param ball: параметры текущего шарика.
    :return: измененные параметры текущего шарика.
    '''
    x = ball[0]
    y = ball[1]
    rad = ball[2]

    speed = ball[4]
    color = ball[5]
    if x >= width - rad:
        ball[3] = np.pi / 2 + random() * np.pi
    if y >= height - rad:
        ball[3] = random() * np.pi
    if rad >= x:
        ball[3] = random() * np.pi - np.pi / 2
    if rad >= y - 40:
        ball[3] = random() * np.pi + np.pi
    angle = ball[3]
    x += int(speed * np.cos(angle))
    y -= int(speed * np.sin(angle))
    ball[0] = x
    ball[1] = y
    circle(screen, color, (x, y), rad)
    return ball


def points_table(points):
    '''
    Функция обеспечивает работу счетчика очков.
    :param points: количество очков, выводимое на экран.
    :return: отображение колличества пунктов.
    '''
    my_font = pygame.font.Font(None, 50)
    string = "Счёт: " + str(points)
    text = my_font.render(string, 1, BLACK)
    screen.blit(text, (5, 4))


def round_table(game_round):
    '''
    Функция отображает номер раунда на экране.
    :param game_round: порядковый номер текущего раунда.
    :return: отображение текущего раунда.
    '''
    my_font = pygame.font.Font(None, 50)
    string = "Раунд: " + str(game_round)
    text = my_font.render(string, 1,  BLACK)
    screen.blit(text, (570, 4))




# Начальные показатели счетчиков
points = 0
game_round = 1




finished = False

while not finished:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for ball in ball_setup_list:
                ball_setup_list, points, ball_quantity = click_ball(ball, ball_setup_list, event, points, ball_quantity)
            for super_ball in super_ball_setup_list:
                super_ball_setup_list, points, super_ball_quantity = click_super_ball(super_ball, super_ball_setup_list, event, points, super_ball_quantity)

    for ball in ball_setup_list + super_ball_setup_list:
        balls_moving(ball)

    if super_ball_setup_list == [] and ball_setup_list == []:
        game_round += 1
        max_speed +=1

        super_ball_setup_list = super_ball_load(super_ball_quantity)
        ball_setup_list = ball_load(ball_quantity)

    rect(screen, BLUE, (0, 0, width, 40))
    rect(screen, BLACK, (0, 0, width, 40), 1)

    points_table(points)
    round_table(game_round)



    pygame.display.update()
    screen.fill(WHITE)






pygame.quit()