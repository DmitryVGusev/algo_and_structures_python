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
from memory_profiler import profile


def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1)))


@profile()
def get_prime(ind):
    prime_list = []
    for i in count(2):
        if len(prime_list) == ind:
            return prime_list[-1]
        if is_prime(i):
            prime_list.append(i)

@profile()
def eratosphen(ind: int):
    ans = list(range(2, int(ind * log2(ind)) + 3))
    for i in range(len(ans)):
        if ans[i] == 0:
            continue
        for j in range(i+ans[i], len(ans), ans[i]):
            ans[j] = 0
    return [x for x in ans if x][ind-1]


def test_speed():
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


if __name__ == '__main__':

    ### Для начала, проанализируем затраты памяти при использования наивного поиска и решета Эратосфена

    get_prime(5000)

    '''
    Line #    Mem usage    Increment   Line Contents
================================================
    21     13.6 MiB     13.6 MiB   @profile()
    22                             def get_prime(ind):
    23     13.6 MiB      0.0 MiB       prime_list = []
    24     13.8 MiB      0.2 MiB       for i in count(2):
    25     13.8 MiB      0.0 MiB           if len(prime_list) == ind:
    26     13.8 MiB      0.0 MiB               return prime_list[-1]
    27     13.8 MiB      0.0 MiB           if is_prime(i):
    28     13.8 MiB      0.0 MiB               prime_list.append(i)
    '''

    eratosphen(5000)
    '''
    Line #    Mem usage    Increment   Line Contents
================================================
    30     13.8 MiB     13.8 MiB   @profile()
    31                             def eratosphen(ind: int):
    32     16.0 MiB      2.2 MiB       ans = list(range(2, int(ind * log2(ind)) + 3))
    33     16.0 MiB      0.0 MiB       for i in range(len(ans)):
    34     16.0 MiB      0.0 MiB           if ans[i] == 0:
    35     16.0 MiB      0.0 MiB               continue
    36     16.0 MiB      0.0 MiB           for j in range(i+ans[i], len(ans), ans[i]):
    37     16.0 MiB      0.0 MiB               ans[j] = 0
    38     16.0 MiB      0.0 MiB       return [x for x in ans if x][ind-1]
    '''



