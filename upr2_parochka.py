import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1000, 800))

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 51, 51)
skin = (255, 229, 204)
green = (0, 204, 0)
brown = (118, 71, 0)
grey = (190, 189, 182)
orange = (254, 108, 4)
blue = (98, 222, 255)
pink = (255, 187, 209)
pink2 = (255, 0, 127)
grey2 = (144, 149, 171)
lightbrown = (168, 102, 2)
lightblue = (168, 203, 255)

rect(screen, lightblue, (0, 0, 1000, 400)) # фон
rect(screen, green, (0, 400, 1000, 400))

ellipse(screen, grey, (258, 238, 152, 314))  # туловище мужчины
line(screen, black, (148, 429), (287, 274))  # правая рука
line(screen, black, (484, 421), (377, 272))  # левая рука
circle(screen, skin, (341, 198), 55)    # глова
line(screen, black, (302, 534), (230, 716))  # правая нога
line(screen, black, (230, 716), (189, 718))
line(screen, black, (368, 526), (387, 718))  # левая нога
line(screen, black, (387, 718), (430, 720))
circle(screen, white, (96, 340), 28)  # шарики мороженого
circle(screen, pink, (126, 350), 28)
circle(screen, red, (96, 370), 25)
polygon(screen, orange, [(163, 433), (150, 326), (70, 384)])  # рожок для мороженого


polygon(screen, pink2, [(575, 546), (683, 223), (789, 547)])  # туловище женщины
circle(screen, skin, (683, 198), 55)  # глова
line(screen, black, (668, 270), (483, 420))  # правая рука
line(screen, black, (697, 273), (764, 330))  # левая рука
line(screen, black, (764, 330), (846, 283))
line(screen, black, (841, 314), (880, 170))  # шарик
polygon(screen, red, [(880, 170), (950, 113), (878, 85)])
circle(screen, red, (940, 96), 25)
circle(screen, red, (900, 80), 25)
line(screen, black, (644, 550), (640, 700))  # правая нога
line(screen, black, (640, 700), (595, 700))
line(screen, black, (710, 550), (707, 702))  # левая нога
line(screen, black, (707, 702), (747, 707))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
