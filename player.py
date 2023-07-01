import pygame
from pygame.constants import K_DOWN, K_UP, K_RIGHT, K_LEFT, K_SPACE

from display import HEIGHT, WiDTH
from create_hit_box import create_hit_box

player_color = (255, 255, 255)
player_size = (20, 20)
player = pygame.Surface(player_size)
player.fill(player_color)
player_rect = pygame.Rect(100, HEIGHT / 2, *player_size)
player_move_down = [0, 2]
player_move_up = [0, -2]
player_move_left = [-2, 0]
player_move_right = [2, 0]


def player_move(keys, rect):
    if keys[K_DOWN] and rect.bottom < HEIGHT:
        rect = rect.move(player_move_down)

    if keys[K_UP] and rect.top > 0:
        rect = rect.move(player_move_up)

    if keys[K_RIGHT] and rect.right < WiDTH:
        rect = rect.move(player_move_right)

    if keys[K_LEFT] and rect.left > 0:
        rect = rect.move(player_move_left)

    return rect
