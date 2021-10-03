import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 700))

# цвета которые используются в работе
white = (255, 255, 255)
black = (0, 0, 0)
green = (175, 237, 87)
brown = (118, 71, 0)
grey = (190, 189, 182)
orange = (254, 108, 4)
blue = (98, 222, 255)
pink = (255, 187, 209)
kote = (144, 149, 171)
lightbrown = (168, 102, 2)
lightblue = (168, 203, 255)

# Рисуем фон
rect(screen, brown, (0, 0, 600, 370))
rect(screen, lightbrown, (0, 370, 600, 430))


def okno(x):
    rect(screen, lightblue, (x, 50, 150, 200))
    rect(screen, white, (x, 50, 150, 200), 15)
    line(screen, white, (x, 100), (x + 150, 100), 10)
    line(screen, white, (x + 75, 50), (x + 75, 250), 10)


def klubok(x, y, r):
    pi = 3.14
    circle(screen, grey, (x, y), r)
    circle(screen, black, (x, y), r, 1)
    arc(screen, black, (x - r, y - r * 4 / 5, 1.5 * r, 2 * r), 0, 1 / 2 * pi, 1)
    arc(screen, black, (x - r * 3 / 4, y - r * 9 / 10, 1.5 * r, 2 * r), 0, 1 / 2 * pi)
    arc(screen, black, (x - r * 6 / 5, y - 4 / 6 * r, 1.5 * r, 2 * r), 0, 1 / 2 * pi)
    arc(screen, black, (x - r * 2 / 3, y - r * 4 / 7, 5 / 3 * r, 5 / 3 * r), pi * 3 / 4, pi * 7 / 6)
    arc(screen, black, (x - r * 3 / 7, y - r * 4 / 8, 5 / 3 * r, 5 / 3 * r), pi * 3 / 4, pi * 7 / 6)
    arc(screen, black, (x - r * 2 / 10, y - r * 2 / 9, 2 * r, 3 / 2 * r), pi * 3 / 4, pi * 7 / 6)
    arc(screen, black, (x - r * 2 / 10, y - r * 2 / 9, 2 * r, 3 / 2 * r), pi * 3 / 4, pi * 7 / 6)


def kot(x, y, r, bodycolor, eyecolor, pos):
    pi = 3.14
    if pos == 1 :       # дадим возможность выбора с какой стороны будет находится тело кота (1- слева, остальные
        # значения- справа)
        ellipse(screen, bodycolor, (x - 5 * r, y + r, 3 * r, 0.5 * r))  # хвост(слева)
        ellipse(screen, black, (x - 5 * r, y + r, 3 * r, 0.5 * r), 1)

        ellipse(screen, bodycolor, (x - 2.7 * r, y, 4 * r, 2.4 * r))  # туловище(слева)
        ellipse(screen, black, (x - 2.7 * r, y, 4 * r, 2.4 * r), 1)

        ellipse(screen, bodycolor, (x, y + r * 1.8, r, 0.6 * r))  # передние лапы(слева)
        ellipse(screen, black, (x, y + r * 1.8, r, 0.6 * r), 1)
        ellipse(screen, bodycolor, (x + r * 1, y + r, 0.6 * r, r))
        ellipse(screen, black, (x + r * 1, y + r, 0.6 * r, r), 1)

        circle(screen, bodycolor, (x - r * 2, y + r * 1.7), r * 0.7)  # задняя лапа(слева)
        circle(screen, black, (x - r * 2, y + r * 1.7), r * 0.7, 1)
        ellipse(screen, bodycolor, (x - r * 2.8, y + r * 1.8, 0.4 * r, 1.3 * r))
        ellipse(screen, black, (x - r * 2.8, y + r * 1.8, 0.4 * r, 1.3 * r), 1)
    else:
        ellipse(screen, bodycolor, (x + 4 * r, y + r, 3 * r, 0.5 * r))  # хвост(справа)
        ellipse(screen, black, (x + 4 * r, y + r, 3 * r, 0.5 * r), 1)

        ellipse(screen, bodycolor, (x + 0.7 * r, y, 4 * r, 2.4 * r))  # туловище(справа)
        ellipse(screen, black, (x + 0.7 * r, y, 4 * r, 2.4 * r), 1)

        ellipse(screen, bodycolor, (x + r, y + r * 1.8, r, 0.6 * r))  # передние лапы(справа)
        ellipse(screen, black, (x + r, y + r * 1.8, r, 0.6 * r), 1)
        ellipse(screen, bodycolor, (x + 0.4 * r, y + r, 0.6 * r, r))
        ellipse(screen, black, (x + 0.4 * r, y + r, 0.6 * r, r), 1)

        circle(screen, bodycolor, (x + r * 4, y + r * 1.7), r * 0.7)  # задняя лапа(справа)
        circle(screen, black, (x + r * 4, y + r * 1.7), r * 0.7, 1)
        ellipse(screen, bodycolor, (x + r * 4.4, y + r * 1.8, 0.4 * r, 1.3 * r))
        ellipse(screen, black, (x + r * 4.4, y + r * 1.8, 0.4 * r, 1.3 * r), 1)

    ellipse(screen, bodycolor, (x, y, r * 2, r * 1.75))  # голова
    ellipse(screen, black, (x, y, r * 2, r * 1.75), 1)

    polygon(screen, bodycolor,
            [(x + r * 1.2, y + r * 0.09), (x + r * 1.55, y + r * 0.2), (x + r * 1.45, y - r * 0.3)])  # левое ухо
    polygon(screen, black, [(x + r * 1.2, y + r * 0.09), (x + r * 1.55, y + r * 0.2), (x + r * 1.45, y - r * 0.3)], 1)
    polygon(screen, pink, [(x + r * 1.26, y + r * 0.07), (x + r * 1.5, y + r * 0.15), (x + r * 1.44, y - r * 0.24)])

    polygon(screen, bodycolor,
            [(x + r * 0.5, y + r * 0.2), (x + r * 0.85, y + r * 0.09), (x + r * 0.57, y - r * 0.3)])  # правое ухо
    polygon(screen, black, [(x + r * 0.5, y + r * 0.2), (x + r * 0.85, y + r * 0.09), (x + r * 0.57, y - r * 0.3)], 1)
    polygon(screen, pink, [(x + r * 0.54, y + r * 0.15), (x + r * 0.8, y + r * 0.07), (x + r * 0.59, y - r * 0.22)])

    ellipse(screen, eyecolor, (x + r * 0.5, y + r * 0.45, r * 0.4, r * 0.5))  # правый глаз
    ellipse(screen, black, (x + r * 0.5, y + r * 0.45, r * 0.4, r * 0.5), 1)
    ellipse(screen, black, (x + r * 0.68, y + r * 0.5, r * 0.1, r * 0.4))
    polygon(screen, white, [(x + r * 0.64, y + r * 0.49), (x + r * 0.6, y + r * 0.55), (x + r * 0.7, y + r * 0.6)])

    ellipse(screen, eyecolor, (x + r * 1.2, y + r * 0.45, r * 0.4, r * 0.5))  # левый глаз
    ellipse(screen, black, (x + r * 1.2, y + r * 0.45, r * 0.4, r * 0.5), 1)
    ellipse(screen, black, (x + r * 1.38, y + r * 0.5, r * 0.1, r * 0.4))
    polygon(screen, white, [(x + r * 1.34, y + r * 0.49), (x + r * 1.3, y + r * 0.55), (x + r * 1.4, y + r * 0.6)])

    polygon(screen, pink, [(x + r * 1, y + r * 1.05), (x + r * 1.2, y + r * 1.05), (x + r * 1.1, y + r * 1.2)])  # нос
    arc(screen, black, (x + r * 0.85, y + r * 1.11, r * 0.3, r * 0.3), 1.5 * pi, 0, 1)
    arc(screen, black, (x + r * 1.11, y + r * 1.11, r * 0.3, r * 0.3), pi, 1.5 * pi, 1)

    line(screen, black, (x + r * 1.5, y + r * 1.1), (x + r * 2.2, y + r * 0.9))  # усы....
    line(screen, black, (x + r * 1.5, y + r * 1.15), (x + r * 2.15, y + r * 1.2))
    line(screen, black, (x + r * 1.5, y + r * 1.20), (x + r * 2.1, y + r * 1.5))
    line(screen, black, (x + r * 0.6, y + r * 1.1), (x - r * 0.36, y + r * 0.9))
    line(screen, black, (x + r * 0.58, y + r * 1.15), (x - r * 0.32, y + r * 1.2))
    line(screen, black, (x + r * 0.58, y + r * 1.20), (x - r * 0.30, y + r * 1.5))


okno(50)
okno(300)
okno(550)
klubok(80, 530, 30)
klubok(300, 400, 20)

kot(200, 400, 30, orange, lightblue, 1)
kot(200, 550, 40, kote, green, 0)
kot(500, 350, 19, kote, lightblue, 1)
klubok(520, 630, 40)
kot(350, 450, 23, orange, green, 0)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

