"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""
from math import sqrt, log2
from itertools import count, islice

import timeit
import cProfile


def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1)))


def get_prime(ind):
    prime_list = []
    for i in count(2):
        if len(prime_list) == ind:
            return prime_list[-1]
        if is_prime(i):
            prime_list.append(i)


def eratosphen(ind: int):
    ans = list(range(2, int(ind * log2(ind)) + 3))
    for i in range(len(ans)):
        if ans[i] == 0:
            continue
        for j in range(i+ans[i], len(ans), ans[i]):
            ans[j] = 0
    return [x for x in ans if x][ind-1]


if __name__ == '__main__':

        N = 1000
        ans = []

        time_it = lambda func, n, N: timeit.timeit(f"{func}({n})", number=N, setup=f"from __main__ import {func}")

        for n in [1, 2, 5, 10, 100, 200, 300]:
            ans.append([n,
                        time_it(get_prime.__name__, n, N),
                        time_it(eratosphen.__name__, n, N)])

        print(f"{'индекс':^7} {'Наивный':<8} {'Решето':<8}")
        for n, f1, f2 in ans:
            print(f"{n:>7} {f1:.5f} {f2:.5f}")



