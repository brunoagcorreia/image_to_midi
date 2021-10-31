import random
from scales import pitches

_value_ = 500


def value_parser(value):
    if between(value, 48, 59):
        value_new = value / 1
    elif between(value, 48*2, 59*2):
        value_new = value / 2
    elif between(value, 48*3, 59*3):
        value_new = value / 3
    elif between(value, 48*4, 59*4):
        value_new = value / 4
    elif between(value, 48*5, 59*5):
        value_new = value / 5
    elif between(value, 48*6, 59*6):
        value_new = value / 6
    elif between(value, 48*7, 59*7):
        value_new = value / 7
    elif between(value, 48*8, 59*8):
        value_new = value / 8
    elif between(value, 48*9, 59*9):
        value_new = value / 9
    elif between(value, 48*10, 59*10):
        value_new = value / 10
    # else:
    #     value_new = random.randint(48, 59)
    else:
        value_new = random.randint(48, 59)
    return round(value_new)


def between(val, val_1, val_2):
    if val_1 <= val < val_2:
        return True
    else:
        return False


print(value_parser(_value_))
