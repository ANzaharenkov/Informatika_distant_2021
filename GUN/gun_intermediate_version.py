import math
from random import *

import pygame
from pygame.draw import *

import math

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGHTBLUE = (168, 203, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
DARKGREEN = (7, 95, 7)
GOLD = (212, 175, 55)

FPS = 30
width = 1080
height = 720
bottom_line = 55  # величина поля в нижней части экрана

target_colors = [RED, YELLOW, GREEN, BLUE, CYAN, MAGENTA]
target_quantity = 2
special_target_quantity = 1
target_min_radius = 30
target_max_radius = 50
min_deflection_angle = 0
max_deflection_angle = int(math.pi)
target_speed = 15
special_target_speed = 30

gun_len = 70
min_gun_power = 5
max_gun_power = 100
gun_movement_speed = 3

bullet_radius = 15

g = 1  # "типа" ускорение свободного падения


class Target:
    def __init__(
            self, surface, color=None,
            min_angle=min_deflection_angle, max_angle=max_deflection_angle,
                ):
        self.surface = surface
        self.color = color or choice(target_colors)
        width, height = self.surface.get_size()
        self.x = randint(target_max_radius + bottom_line, width - target_max_radius)
        self.y = randint(target_max_radius, height - target_max_radius)
        self.rad = randint(target_min_radius, target_max_radius)
        self.angle = randint(min_angle, max_angle)
        self.speed = target_speed

    def draw(self):
        '''
        Функция рисует мишени.
        :return:
        '''
        circle(self.surface, self.color, (self.x, self.y), self.rad)
        circle(self.surface, BLACK, (self.x, self.y), self.rad * 3 / 4, 10)
        circle(self.surface, BLACK, (self.x, self.y), self.rad / 5, 10)

    def move(self):
        '''
        Функция заставляет мишени двигаться по экрану и отражаться от стен.
        :return:
        '''
        width, height = self.surface.get_size()
        if self.x >= width - self.rad:
            self.angle = math.pi / 2 + random() * math.pi
        if self.y >= height - self.rad - bottom_line:
            self.angle = random() * math.pi
        if self.rad >= self.x:
            self.angle = random() * math.pi - math.pi / 2
        if self.rad >= self.y:
            self.angle = random() * math.pi + math.pi
        self.x += int(self.speed * math.cos(self.angle))
        self.y -= int(self.speed * math.sin(self.angle))


class Special_Target:
    def __init__(
            self, surface,
            min_angle=min_deflection_angle, max_angle=max_deflection_angle
                ):
        self.surface = surface
        self.color = GOLD
        width, height = self.surface.get_size()
        self.x = randint(target_max_radius + bottom_line, width - (target_max_radius // 2))
        self.y = randint(target_max_radius, height - target_max_radius)
        self.rad = randint(target_min_radius // 2, target_min_radius // 2)
        self.angle = randint(min_angle, max_angle)
        self.speed = special_target_speed

    def draw(self):
        '''
        Функция рисует особые мишени.
        :return:
        '''
        circle(self.surface, self.color, (self.x, self.y), self.rad)

    def move(self):
        '''
        Функция заставляет особые мишени двигаться по экрану и отражаться от стен.
        :return:
        '''
        width, height = self.surface.get_size()
        if self.x >= width - self.rad:
            self.angle = math.pi / 2 + random() * math.pi
        if self.y >= height - self.rad - bottom_line:
            self.angle = random() * math.pi + math.pi * 2
        if self.rad >= self.x:
            self.angle = random() * math.pi - math.pi / 2
        if self.rad >= self.y:
            self.angle = random() * math.pi + 3 * math.pi
        self.x += int(self.speed * math.cos(self.angle))
        self.y -= int(self.speed * math.sin(self.angle))


class Gun:
    def __init__(self, surface):
        self.surface = surface
        self.width = 50
        self.height = 20
        self.bottom_x = surface.get_width() // 2
        self.bottom_y = surface.get_height() - bottom_line
        self.len = gun_len
        self.angle = 0
        self.color_1 = BLACK
        self.color_2 = DARKGREEN
        self.power = min_gun_power

    def draw(self):
        '''
        Функция рисует танк.
        :return:
        '''
        x = int(self.bottom_x + self.len * math.cos(self.angle))
        y = int(self.bottom_y - self.len * math.sin(self.angle))
        line(self.surface, self.color_1, (self.bottom_x, self.bottom_y - self.height), (x, y), 8)
        rect(self.surface, self.color_2,
             (self.bottom_x - self.width / 2, self.bottom_y - self.height, self.width, self.height))

    def move(self):
        '''
            Функция передвигает танк.
            :return:
        '''

    def aim(self, x, y):
        '''
        Функция изменяет угол наклона дуола в зависимости от положения курсора на экране.
        :param x: координата x курсора.
        :param y: координата y курсора.
        :return:
            self.angle: мгновенное значение угла наклона.
        '''
        self.angle = math.atan2(self.bottom_y - y, x - self.bottom_x)
        return self.angle

    def power_up(self):
        '''
        Функция наращивает мощность пушки.
        :return:
        '''
        self.color_1 = RED
        if self.power < max_gun_power:

            self.power += 0.75



    def shoot(self):
        '''
        Функция обрабатывает момент "выстрела".
        :return:
            списком:
            x: координата x "дула" при выстреле.
            y: координата y "дула" при выстреле.
            power: мощность пушки при выстреле.
        '''
        x = self.bottom_x + self.len * math.cos(self.angle)
        y = self.bottom_y - self.len * math.sin(self.angle)
        power = self.power
        self.color = BLACK
        self.power = min_gun_power
        self.len = gun_len
        return x, y, power

    def move_right(self):
        self.bottom_x += gun_movement_speed
        if self.bottom_x + self.width / 2 >= width:
            self.bottom_x -= gun_movement_speed

    def move_left(self):
        self.bottom_x -= gun_movement_speed
        if self.bottom_x - self.width / 2 <= 0:
            self.bottom_x += gun_movement_speed


class Bullet:
    def __init__(self, surface, x, y, power, angle):
        self.x = x
        self.y = y
        self.vx = power * math.cos(angle)
        self.vy = power * math.sin(angle)
        self.surface = surface
        self.rad = bullet_radius
        self.color = BLACK
        self.wall_hits = 0

    def draw(self):
        '''
        Функция рисует снаряд.
        :return: шарик....
        '''
        circle(self.surface, self.color, (int(self.x), int(self.y)), self.rad)
        circle(self.surface, BLACK, (int(self.x), int(self.y)), self.rad, 1)

    def move(self):
        '''
        Функция перемещает снаряды пушки.
        :return: self.wall_hits: число ударов ядра о стены.
        '''
        width, height = self.surface.get_size()

        if not self.rad < self.x < width - self.rad or not self.rad < self.y < height - self.rad - bottom_line:
            self.wall_hits += 1

            if self.x >= width + self.rad:
                self.x = width - self.rad
                self.vx *= -0.75
                self.vy *= 0.9
            elif self.y >= height - self.rad - bottom_line:
                self.y = height - self.rad - bottom_line
                self.vy *= -0.75
                self.vx *= 0.9
            elif self.rad >= self.x:
                self.x = self.rad
                self.vx *= -0.75
                self.vy *= 0.9
            elif self.rad >= self.y:
                self.y = self.rad
                self.vy *= -0.75
                self.vx *= 0.9

        self.x += self.vx
        self.y -= self.vy
        self.vy -= g
        return self.wall_hits

    def hit_check(self, target):
        '''
        Функция проверяет, попал ли снаряд в мишень.
        :param target: мишень, попадание в которую проверяется.
        :return: True или False, то есть попал или нет.
        '''
        return ((target.x - self.x) ** 2 + (target.y - self.y) ** 2) <= (target.rad + self.rad) ** 2


class Score:
    def __init__(self, surface, x, y, pre_text):
        self.surface = surface
        self.my_font = pygame.font.Font(None, 50)
        self.x = x
        self.y = y
        self.pre_text = pre_text

    def write(self, num):
        '''
        Функция выводит надпись со счетом.
        :param num: выводимое число очков.
        :return:
        '''
        text = self.my_font.render(self.pre_text + str(num), 1, BLACK)
        self.surface.blit(text, (self.x, self.y))


pygame.init()
screen = pygame.display.set_mode((width, height))

Gun = Gun(screen)

shots = 0
points = 0
bullet_list = []

target_list = []
special_target_list = []
for i in range(target_quantity):
    target_list.append(Target(screen))
for i in range(special_target_quantity):
    special_target_list.append(Special_Target(screen))

t_points = Score(screen, 5, 3, "Счёт: ")

finished = False
clock = pygame.time.Clock()

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            break
        elif event.type == pygame.MOUSEMOTION:
            angle = Gun.aim(*pygame.mouse.get_pos())
        elif event.type == pygame.MOUSEBUTTONUP:
            x, y, power = Gun.shoot()
            bullet_list.append(Bullet(screen, x, y, power, Gun.angle))

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_a]:
        Gun.move_left()

    if pressed_keys[pygame.K_d]:
        Gun.move_right()

    if pygame.mouse.get_pressed()[0]:
        Gun.power_up()

    Gun.draw()

    for bullet in bullet_list:
        bullet.draw()
        wall_hits = bullet.move()
        for target in target_list:
            if bullet.hit_check(target):
                target_list.remove(target)
                target_list.append(Target(screen))
                points += 1

        for special_target in special_target_list:
            if bullet.hit_check(special_target):
                special_target_list.remove(special_target)
                special_target_list.append(Special_Target(screen))
                points += 3

        if wall_hits > 8:
            bullet_list.remove(bullet)

    for target in target_list:
        target.draw()
        target.move()

    for special_target in special_target_list:
        special_target.draw()
        special_target.move()

    t_points.write(points)

    pygame.display.update()
    screen.fill(WHITE)

    rect(screen, LIGHTBLUE, (0, height - bottom_line, width, bottom_line))

pygame.quit
