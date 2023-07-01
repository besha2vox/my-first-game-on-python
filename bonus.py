import pygame
import random

from create_hit_box import create_hit_box
from display import HEIGHT, WiDTH
from services import check_intersection


def create_enemy_speed():
    return [random.randint(-4, -1), 0]


bonus_size = (30, 25)
bonus_color = (255, 255, 51)
create_bonus_hit_box = create_hit_box(
    bonus_size, bonus_color, ([0, WiDTH - 15], 0), (0, 1))
bonuses_list = []

CREATE_BONUS = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_BONUS, 3000)


def delete_bonus(playerr_rect):
    for bonus in bonuses_list:
        if bonus[1].bottom > HEIGHT or check_intersection(bonus[1], playerr_rect):
            bonuses_list.pop(bonuses_list.index(bonus))
