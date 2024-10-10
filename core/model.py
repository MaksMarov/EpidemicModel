import random as rnd

def check_value(value, min_value, max_value):
    if value > max_value: return max_value
    if value < min_value: return min_value
    return value

def cast_param(referense, persent, min_value = 0, max_value = 1):
    return check_value(referense + rnd.uniform(-1, 1) * referense * persent, min_value, max_value)

def change_param(referense, value, persent, min_value = 0, max_value = 1):
        return check_value(referense + value * persent, min_value, max_value)

def calc_chanse(probability):
    return rnd.random() < probability