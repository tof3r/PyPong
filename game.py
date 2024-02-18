import random
from math import sin, cos

import pygame
import sys

from ball import Ball
from paddle import Paddle
from result import Result
from settings import *


def game_fun():
    clock = pygame.time.Clock()
    ball = Ball(BALL_X_MID_SCREEN, BALL_Y_MID_SCREEN)
    left_paddle = Paddle(LEFT_PADDLE_MARGIN, PADDLE_Y_MID_SCREEN)
    right_paddle = Paddle(RIGHT_PADDLE_MARGIN, PADDLE_Y_MID_SCREEN)
    result = Result()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def handle_controls():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            left_paddle.update(-PADDLE_SPEED)
        if keys[pygame.K_s]:
            left_paddle.update(PADDLE_SPEED)

        if keys[pygame.K_i]:
            right_paddle.update(-PADDLE_SPEED)
        if keys[pygame.K_k]:
            right_paddle.update(PADDLE_SPEED)

        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        if keys[pygame.K_SPACE]:
            reset_game()

    def reset_ball():
        ball.rect.x = BALL_X_MID_SCREEN
        ball.rect.y = BALL_Y_MID_SCREEN
        ball.ball_speed = random.randint(4, 9)
        ball.random_num = random.uniform(0, 1)
        if ball.random_num <= 0.4:
            ball.random_num = 0.4
        ball.dx = ball.ball_speed * sin(360 * ball.random_num) * random.choice([-1, 1])
        ball.dy = ball.ball_speed * cos(360 * ball.random_num) * random.choice([-1, 1])

    def bounce_ball():
        if ball.rect.colliderect(left_paddle.rect) or ball.rect.colliderect(right_paddle.rect):
            ball.dx = -ball.dx

    def handle_events():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def ball_reaches_screen_edge():
        if ball.rect.x <= 0:
            result.add_point_player_2()
            result.update(screen)
            if result.check_win_player2():
                return
            else:
                reset_ball()
        elif ball.rect.x >= SCREEN_WIDTH - BALL_SIZE:
            result.add_point_player_1()
            result.update(screen)
            if result.check_win_player1():
                return
            else:
                reset_ball()

    def display_on_screen():
        screen.fill(BLACK)
        screen.blit(left_paddle.image, left_paddle.rect)
        screen.blit(right_paddle.image, right_paddle.rect)
        screen.blit(ball.image, ball.rect)

        screen.blit(result.text, result.text_rect)

    def reset_paddles():
        left_paddle.rect.y = PADDLE_Y_MID_SCREEN
        right_paddle.rect.y = PADDLE_Y_MID_SCREEN

    def reset_game():
        reset_ball()
        reset_paddles()
        result.reset()
        result.update(screen)

    while True:
        handle_events()
        handle_controls()

        ball.update()
        bounce_ball()
        ball_reaches_screen_edge()
        display_on_screen()

        pygame.display.flip()

        clock.tick(60)


if __name__ == "__main__":
    game_fun()
