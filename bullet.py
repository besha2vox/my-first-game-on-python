from pygame.constants import K_SPACE

from display import WiDTH
from create_hit_box import create_hit_box
from services import check_intersection
from enemy import enemies_list

bullet_sise = (10, 5)
bullet_move = [10, 0]
bullet_collor = (255, 255, 255)
bullets_list = []


def player_attack(keys, rect):
    if keys[K_SPACE]:
        create_bullet = create_hit_box(
            bullet_sise, bullet_collor, rect.center, bullet_move)

        if len(bullets_list) < 1:
            bullets_list.append(create_bullet())


def delete_bullet():
    for bullet in bullets_list:
        intersection = False
        for enemy in enemies_list:
            intersection = check_intersection(bullet[1], enemy[1])

        if bullet[1].right > WiDTH or intersection:
            bullets_list.pop(bullets_list.index(bullet))
