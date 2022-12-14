import math


# Функция нахождения всех простых чисел, меньших n
def primes(n):
    result = [2]

    for i in range(3, n + 1, 2):
        k = 0
        q = math.sqrt(n) + 2
        for j in result:
            if j > q:
                break
            if i % j == 0:
                k = 1
                break
        if k == 0:
            result.append(i)
    return result
