from display import main_display


def add_on_display(list):
    for el in list:
        el[1] = el[1].move(el[2])
        main_display.blit(el[0], el[1])


def delete_from_display(list, side, value):
    for el in list:
        if side == 'left' and el[1].left < value or side == 'right' and el[1].right > value or side == 'bottom' and el[1].bottom > value:
            list.pop(list.index(el))
