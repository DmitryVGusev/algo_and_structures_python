"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
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


def series_sum_recursive(n, el=(-0.5), summ=1):
    """Возвращает сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ..."""
    if n == 1:
        return summ
    else:
        return summ + series_sum_recursive(n-1, el*(-0.5), el)


if __name__ == '__main__':
    number = int(input("Введите количество элементов: "))
    print(series_sum(number))
    print(series_sum_recursive(number))