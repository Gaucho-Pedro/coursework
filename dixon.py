import logging
import math
from math import sqrt, gcd

import numpy as np

import utils


def factor(n):
    logging.debug("Начало разложения числа ")

    # Выбор факторной базы
    base = utils.primes(math.floor(math.exp(math.sqrt(math.log(n) * math.log(math.log(n))))))

    # Начинаем поиск с sqrt(n)
    start = int(sqrt(n))

    # Хранение связанных квадратов
    pairs = []

    for i in range(start, n):

        # Ищем связанные квадраты
        for j in range(len(base)):
            # a^2 mod(n)
            lhs = i ** 2 % n
            # b^2 mod(n)
            rhs = base[j] ** 2 % n

            # Если a^2 = b^2 mod(N), то добавляем в массив пару
            if lhs == rhs:
                pairs.append([i, base[j]])

    new = []

    # Проверяем НОД(a - b, N)
    for i in range(len(pairs)):
        factor = gcd(pairs[i][0] - pairs[i][1], n)

        # Если НОД !=1, то добавляем коллекцию результатов
        if factor != 1:
            new.append(factor)

    x = np.array(new)
    logging.debug("Конец разложения")
    return np.unique(x)
