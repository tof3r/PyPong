import pygame

from settings import SCREEN_HEIGHT
from settings import PADDLE_WIDTH, PADDLE_HEIGHT
from settings import WHITE


class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, dy):
        self.rect.y += dy
        self.rect.y = max(0, min(SCREEN_HEIGHT - PADDLE_HEIGHT, self.rect.y))
