import random
import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_RIGHT, K_LEFT

pygame.init()

FPS = pygame.time.Clock()

# * >----|SIZE|----<
HEIGHT = 800
WiDTH = 1200

# * >----|COLORS|----<
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 51)
COLOR_BLACK = (0, 0, 0)
COLOR_PINK = (255, 20, 147)

main_display = pygame.display.set_mode((WiDTH, HEIGHT))

# * >----|PLAYER|----<
player_size = (20, 20)
player = pygame.Surface(player_size)
player.fill(COLOR_WHITE)
player_rect = player.get_rect()
player_move_down = [0, 1]
player_move_up = [0, -1]
player_move_right = [1, 0]
player_move_left = [-1, 0]

# * >----|CREATE BLOCKS|----<


def create_block_position(x, y):
    def func():
        if isinstance(x, list):
            x_value = random.randint(*x)
        else:
            x_value = x

        if isinstance(y, list):
            y_value = random.randint(*y)
        else:
            y_value = y

        return [x_value, y_value]

    return func


def create_blocks(size, color, position, move):
    block_size = size
    block = pygame.Surface(block_size)
    block.fill(color)
    block_rect = pygame.Rect(*position, *block_size)
    block_move = move
    return [block, block_rect, block_move]


# * >----|BONUSES|----<
bonus_size = (15, 15)
create_bonus_position = create_block_position([0, WiDTH - 15], 0)
bonuses = []

CREATE_BONUS = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_BONUS, 3000)


# * >----|EMEMY|----<
enemy_size = (30, 30)
create_enemy_position = create_block_position(WiDTH, [0, HEIGHT - 30])
enemies = []

CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 500)


# * >----|GAME LOGIC|----<
i = 0
playing = True
while playing:
    i += 1
    FPS.tick(500000)
    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
        if event.type == CREATE_ENEMY:
            enemies.append(create_blocks(enemy_size, COLOR_PINK,
                           create_enemy_position(), [random.randint(-4, -1), 0]))
        if event.type == CREATE_BONUS:
            bonuses.append(create_blocks(
                bonus_size, COLOR_YELLOW, create_bonus_position(), [0, 1]))

    main_display.fill(COLOR_BLACK)

    keys = pygame.key.get_pressed()

    if keys[K_DOWN] and player_rect.bottom < HEIGHT:
        player_rect = player_rect.move(player_move_down)

    if keys[K_UP] and player_rect.top > 0:
        player_rect = player_rect.move(player_move_up)

    if keys[K_RIGHT] and player_rect.right < WiDTH:
        player_rect = player_rect.move(player_move_right)

    if keys[K_LEFT] and player_rect.left > 0:
        player_rect = player_rect.move(player_move_left)

    for enemy in enemies:
        enemy[1] = enemy[1].move(enemy[2])
        main_display.blit(enemy[0], enemy[1])

    for bonus in bonuses:
        bonus[1] = bonus[1].move(bonus[2])
        main_display.blit(bonus[0], bonus[1])

    main_display.blit(player, player_rect)

    pygame.display.flip()

    for enemy in enemies:
        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))

    for bonus in bonuses:
        if bonus[1].left < 0:
            bonuses.pop(bonuses.index(bonus))
