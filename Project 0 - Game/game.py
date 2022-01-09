"""Игра угадай число
Компьютер сам загадывает и сам угадывает число путем бинарного поиска
"""

import numpy as np


def binary_search(number=1) -> int:
    """Угадываем число бинарным поиском!

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count_try = 0
    low = 0 # нижняя граница
    high = 100 # верхняя граница

    while low <= high:
        count_try += 1
        predict_number = (low + high)/2 # поиск среднего значения в диапазоне
        
        if number < predict_number:
            high = predict_number - 1 # меняем верхнюю границу, если число велико       
        if number > predict_number:
            low = predict_number + 1 # меняем нижнюю границу, если мало
        if number == predict_number:
            break  # выход из цикла если угадали
        
    return count_try


def score_game(binary_search) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size = (1000))  # загадали список чисел

    for numb in random_array:
        count_ls.append(binary_search(numb))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(binary_search)