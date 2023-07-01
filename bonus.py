import pygame
import random

from create_hit_box import create_hit_box
from display import HEIGHT, WiDTH


def create_enemy_speed():
    return [random.randint(-4, -1), 0]


bonus_size = (15, 15)
bonus_color = (255, 255, 51)
create_bonus_hit_box = create_hit_box(
    bonus_size, bonus_color, ([0, WiDTH - 15], 0), (0, 1))
bonuses_list = []

CREATE_BONUS = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_BONUS, 3000)
