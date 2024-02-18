import pygame_menu as pm

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_WIDTH = 16
PADDLE_HEIGHT = 80
BALL_SIZE = 16
PADDLE_SPEED = 6

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

LEFT_PADDLE_MARGIN = SCREEN_WIDTH * 0.02
RIGHT_PADDLE_MARGIN = SCREEN_WIDTH - LEFT_PADDLE_MARGIN - PADDLE_WIDTH

PADDLE_Y_MID_SCREEN = SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2
BALL_X_MID_SCREEN = SCREEN_WIDTH // 2 - BALL_SIZE // 2
BALL_Y_MID_SCREEN = SCREEN_HEIGHT // 2 - BALL_SIZE // 2


def load_settings(settings: pm.Menu):
    with open("settings.dat", "r+") as dat:
        for line in dat.readlines():
            split = line.split("=")
            widget = settings.get_widget(split[0])
            if isinstance(widget, pm.widgets.widget.DropSelect):
                _, index = eval(split[1].strip())
                widget.set_value(index)
            elif isinstance(widget, pm.widgets.widget.ToggleSwitch):
                toggle_value = split[1].strip()
                bool_value = eval(toggle_value)
                widget.set_value(bool_value)


def load_win_points() -> int:
    with open("settings.dat", "r") as dat:
        win_point_line = dat.readline()
        return eval(win_point_line.split("=")[1].strip())[0]
