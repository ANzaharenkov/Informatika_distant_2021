import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
screen = pygame.display.set_mode((1200, 600))

# Цвета используемые в игре
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, BLACK]


def new_ball():
    '''
        Функция рисует новый шарик со случайными координатами
    центра, цветом и радиусом.
        x,y - это позиуия шарика на экране.
        ball_radius - радиус шарика.
        color - это цвет шарика который случайно выбирается из
    6-ти представленных.
    '''
    global x, y, ball_radius
    x = randint(100,800)
    y = randint(100,500)
    ball_radius = randint(30,50)
    color = COLORS[randint(0, 6)]
    circle(screen, color, (x, y), ball_radius)


score = 0


def click(points):
    '''
        Функция анализирует нажатия левой кнопки мыши,
    подсчитывает и выводит количество набранных очков.
        points - количество очков, набранных игроком ранее.
        distance - это расстояние от места нажатия кнопкой.
    мыши на экранедо центра шарика.
    '''
    distance = (event.pos[0] - x)**2 + (event.pos[1] - y)**2

    if distance <= ball_radius**2:
        print('Попал!')
        global score
        score = points + 1
    else:
        print('Промах!')
        score = points - 1
    print('Счет:', score)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(score)
    screen.fill(WHITE)
    new_ball()
    pygame.display.update()


pygame.quit()