"""Игра угадай число
Компьютер сам загадывает и сам угадывает число за минимальное количество попыток
"""

import numpy as np

def game_core_v3(number: int = 1) -> int:
    """ Угадываем число с помощью ограничения интервалов угадывания.
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Задаем начальные значения для счетчика попыток, значения-предсказания, минимальной и максимальной границы интервала (значение-предсказание является серединой интервала)
    count = 0
    predict = 50
    limit_min = 0
    limit_max = 101

    # Цикл для корректировки значения предсказания
    while predict != number:
      # Если предсказание меньше загаданного числа, увеличиваем счетчик попыток, смещаем границы интервала в большую сторону, определяем новое предсказание (середина нового интервала)
      if predict < number:
        count += 1
        limit_min = predict
        predict =  limit_min + round((limit_max - limit_min) / 2)
      # Если предскзание больше загаданного числа, увеличиваем счетчик попыток, смещаем границы интервала в меньшую сторону, определяем новое предсказание (середина нового интервала)
      elif predict >= number:
        count += 1
        limit_max = predict
        predict =  limit_min + round((limit_max - limit_min) / 2)

    return count

if __name__ == "__main__":
    # RUN
    from game_v2 import score_game
    score_game(game_core_v3)