import pygame
import pygame_menu as pm

from game import game_fun
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, load_win_points
from settings import load_settings

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")


def main_fun():

    def on_win_point_change(index: tuple) -> None:
        with open("settings.dat", "r") as dat:
            data = dat.read()
            data = data.replace(f"{old_value_win}", f"{index}")
        with open("settings.dat", "w") as dat:
            dat.write(data)
        win_points_drop.set_value(index[1])

    def on_sound_change(value: bool) -> None:
        with open("settings.dat", "r") as dat:
            data = dat.read()
            data = data.replace(f"{old_value_sound}", f"{value}")
        with open("settings.dat", "w") as dat:
            dat.write(data)
        sound_toggle.set_value(value)

    win_points_items = ["3", "5", "7"]

    menu_settings = pm.Menu(title="Settings", width=SCREEN_WIDTH,
                            height=SCREEN_HEIGHT, theme=pm.themes.THEME_DARK)

    win_points_drop = menu_settings.add.dropselect(title="Points to win", items=win_points_items,
                                                   dropselect_id="win_points", default=0)

    sound_toggle = menu_settings.add.toggle_switch(title="Sound", default=True, toggleswitch_id="sound")

    menu_settings.add.label(title="")
    menu_settings.add.button(title="Back to Main Menu", action=pm.events.BACK,
                             font_color=WHITE, background_color=(200, 200, 255))

    load_settings(menu_settings)

    old_value_win = win_points_drop.get_value()
    win_points_drop.set_onchange(on_win_point_change)
    old_value_sound = sound_toggle.get_value()
    sound_toggle.set_onchange(on_sound_change)

    menu = pm.Menu(title="PyPong", width=SCREEN_WIDTH,
                   height=SCREEN_HEIGHT, theme=pm.themes.THEME_DARK)

    menu.add.button(title="New Game", font_color=WHITE, background_color=(100, 255, 100), action=game_fun)
    menu.add.label(title="")
    menu.add.button(title="Settings", font_color=WHITE, background_color=(100, 100, 255), action=menu_settings)
    menu.add.label(title="")
    menu.add.button(title="Quit", font_color=WHITE, background_color=(255, 100, 100), action=pm.events.EXIT)

    menu.mainloop(screen)


if __name__ == "__main__":
    main_fun()
