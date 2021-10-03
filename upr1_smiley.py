import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 800))

rect(screen, (250, 250, 250), (0, 0, 800, 800))

circle(screen, (255, 255, 0), (400, 400), 250)  # голова
circle(screen, (255, 255, 255), (400, 400), 250, 10)


def glaz(x, y, r):  # глаза
    circle(screen, (250, 0, 0), (x, y), r)
    circle(screen, (0, 0, 0), (x, y), r, int(r / 15))
    circle(screen, (0, 0, 0), (x, y), int(r / 2))


glaz(300, 300, 60)
polygon(screen, (0, 0, 0), [(195, 180), (150, 195), (410, 290), (395, 275)])  # левая бровь

glaz(500, 300, 40)
polygon(screen, (0, 0, 0), [(565, 200), (620, 195), (420, 310), (425, 295)])  # левая бровь

rect(screen, (0, 0, 0), (300, 500, 240, 30))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()