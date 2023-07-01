import random
import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_RIGHT, K_LEFT

from player import player, player_rect, bullets_list, player_actions, player_move_up, player_move_down, player_move_left, player_move_right
from enemy import enemies_list, create_enemy_hit_box, CREATE_ENEMY
from bonus import bonuses_list, create_bonus_hit_box, CREATE_BONUS
from display import HEIGHT, WiDTH, main_display
from services import add_on_display, delete_from_display


pygame.init()

FPS = pygame.time.Clock()

COLOR_BLACK = (0, 0, 0)


# * >----|GAME LOGIC|----<
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

    # if keys[K_DOWN] and player_rect.bottom < HEIGHT:
    #     player_rect = player_rect.move(player_move_down)

    # if keys[K_UP] and player_rect.top > 0:
    #     player_rect = player_rect.move(player_move_up)

    # if keys[K_RIGHT] and player_rect.right < WiDTH:
    #     player_rect = player_rect.move(player_move_right)

    # if keys[K_LEFT] and player_rect.left > 0:
    #     player_rect = player_rect.move(player_move_left)

    player_actions(keys, player_rect)

    add_on_display(enemies_list)
    add_on_display(bonuses_list)
    add_on_display(bullets_list)

    main_display.blit(player, player_rect)

    pygame.display.flip()

    delete_from_display(enemies_list, 'left', 0)
    delete_from_display(bonuses_list, 'bottom', HEIGHT)
    delete_from_display(bullets_list, 'right', WiDTH)
