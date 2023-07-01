import random
import pygame
from pygame.constants import QUIT
import this

from player import player, player_rect, player_move
from bullet import player_attack, bullets_list, delete_bullet
from enemy import enemies_list, create_enemy_hit_box, delete_enemy, CREATE_ENEMY
from bonus import bonuses_list, create_bonus_hit_box, delete_bonus, CREATE_BONUS
from display import main_display
from services import add_on_display, destruction_enemy

print(this)
pygame.init()

FPS = pygame.time.Clock()

COLOR_BLACK = (0, 0, 0)

playing = True
while playing:
    FPS.tick(240)
    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
        if event.type == CREATE_ENEMY:
            enemies_list.append(create_enemy_hit_box())

        if event.type == CREATE_BONUS:
            bonuses_list.append(create_bonus_hit_box())

    main_display.fill(COLOR_BLACK)

    keys = pygame.key.get_pressed()

    player_rect = player_move(keys, player_rect)
    player_attack(keys, player_rect)

    add_on_display(enemies_list)
    add_on_display(bonuses_list)
    add_on_display(bullets_list)

    destruction_enemy(bullets_list, enemies_list)

    main_display.blit(player, player_rect)

    pygame.display.flip()

    delete_enemy()
    delete_bonus(player_rect)
    delete_bullet()
