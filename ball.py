import random
from math import sin, cos

import pygame.sprite
from settings import BALL_SIZE, SCREEN_HEIGHT
from settings import WHITE


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((BALL_SIZE, BALL_SIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.random_num = random.uniform(0, 1)
        self.ball_speed = random.randint(4, 9)
        self.dx = self.ball_speed * sin(360 * self.random_num)
        self.dy = self.ball_speed * cos(360 * self.random_num)

    def update(self):
        print(f"Ball speed: {self.ball_speed}")
        print(f"Random: {self.random_num}")
        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.y <= 0 or self.rect.y >= SCREEN_HEIGHT - BALL_SIZE:
            self.dy = -self.dy
