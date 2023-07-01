import pygame
import random


def create_coordinates(x, y):
    if isinstance(x, list):
        x_value = random.randint(*x)
    else:
        x_value = x
    if isinstance(y, list):
        y_value = random.randint(*y)
    else:
        y_value = y
    return x_value, y_value


def create_hit_box(size, color, position, move):
    def func():

        block_size = size
        block = pygame.Surface(block_size)
        block.fill(color)
        block_rect = pygame.Rect(
            *create_coordinates(*position), *block_size)
        block_move = create_coordinates(*move)
        return [block, block_rect, block_move]

    return func
