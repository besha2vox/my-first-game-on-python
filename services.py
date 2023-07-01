from display import main_display


def check_intersection(rect1, rect2):
    x1, y1, w1, h1 = rect1
    x2, y2, w2, h2 = rect2

    if (x1 < x2 + w2 and x1 + w1 > x2 and y1 < y2 + h2 and y1 + h1 > y2):
        return True
    else:
        return False


def add_on_display(list):
    for el in list:
        el[1] = el[1].move(el[2])
        main_display.blit(el[0], el[1])


def destruction_enemy(bullets_list, enemies_list):
    for enemy in enemies_list:
        for bullet in bullets_list:
            if check_intersection(enemy[1], bullet[1]):
                enemies_list.pop(enemies_list.index(enemy))
                bullets_list.pop(bullets_list.index(bullet))
