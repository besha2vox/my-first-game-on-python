import pygame
import random

from create_hit_box import create_hit_box
from display import HEIGHT, WiDTH


def create_enemy_speed():
    return [random.randint(-4, -1), 0]


enemy_size = (30, 30)
enemy_color = (255, 20, 147)
create_enemy_hit_box = create_hit_box(
    enemy_size, enemy_color, (WiDTH, [0, HEIGHT - 30]), ([-2, -1], 0))
enemies_list = []

CREATE_ENEMY = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_ENEMY, 500)
