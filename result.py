import pygame

from settings import WHITE, SCREEN_WIDTH, SCREEN_HEIGHT, load_win_points


class Result:
    def __init__(self):
        self.points_p1 = 0
        self.points_p2 = 0
        self.font = pygame.font.Font("freesansbold.ttf", 32)
        self.text = self.font.render(f"{self.points_p1}:{self.points_p2}", True, WHITE)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.06)
        self.win_points = load_win_points()

    def add_point_player_1(self):
        self.points_p1 += 1

    def add_point_player_2(self):
        self.points_p2 += 1

    def check_win_player1(self):
        return self.points_p1 >= int(self.win_points)

    def check_win_player2(self):
        return self.points_p2 >= int(self.win_points)

    def reset(self):
        self.points_p1 = 0
        self.points_p2 = 0
        self.text = self.font.render(f"{self.points_p1}:{self.points_p2}", True, WHITE)
        self.text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.06)

    def update(self, screen):
        if self.check_win_player1():
            self.text = self.font.render("Player 1 wins. Press Space to play again.", True, WHITE)
            self.text_rect = self.text.get_rect()
            self.text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.06)
        elif self.check_win_player2():
            self.text = self.font.render("Player 2 wins. Press Space to play again.", True, WHITE)
            self.text_rect = self.text.get_rect()
            self.text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.06)
        else:
            self.text = self.font.render(f"{self.points_p1}:{self.points_p2}", True, WHITE)
            self.text_rect = self.text.get_rect()
            self.text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.06)
        screen.blit(self.text, self.text_rect)
