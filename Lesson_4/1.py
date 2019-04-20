"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""
import timeit
import cProfile
import sys


"""
Ниже представлены алгоритмы суммы n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Первый вариант церез цикл. Алгоритм линейный
"""


def series_sum(n):
    """Возвращает сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ..."""
    summ = 1
    el = 1
    i = 1
    while i < n:
        el *= -0.5
        summ += el
        i += 1
    return summ


# 0.530сек - результат вызова функции 100000 раз
print(timeit.timeit("series_sum(40)",
                    setup="from __main__ import series_sum",
                    number=100000))


"""
Второй вариант реализации алгоритма - через рекурсию.
Алгоритм также линейный
"""


def series_sum_recursive(n, el=(-0.5), summ=1):
    """Возвращает сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ..."""
    if n == 1:
        return summ
    else:
        return summ + series_sum_recursive(n-1, el*(-0.5), el)


# 1.197сек - результат вызова функции 100000 раз
print(timeit.timeit("series_sum_recursive(40)",
                    setup="from __main__ import series_sum_recursive",
                    number=100000))


"""
Таким образом, решение через цикл показывает более чем в 2 раза прирост скорости исполнения задачи
"""


def main():
    sys.setrecursionlimit(10100)
    n = 10000
    series_sum(n)
    series_sum_recursive(n)


cProfile.run('main()')


"""
         10006 function calls (7 primitive calls) in 0.020 seconds

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.001    0.001 1.py:17(series_sum)
  10000/1    0.019    0.000    0.019    0.019 1.py:40(series_sum_recursive)
        1    0.000    0.000    0.020    0.020 1.py:54(main)
        1    0.000    0.000    0.020    0.020 <string>:1(<module>)
        1    0.000    0.000    0.020    0.020 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method sys.setrecursionlimit}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        
Здесь же решение через цикл показывает прирост скорости примерно в 20 раз
"""
