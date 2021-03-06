"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""

"""
Python не допускает чтобы имена модулей начинались с цифры,
так что мы не можем импортировать функцию min_in_mass из 3.py
Реализуем функцию еще раз, но подразумеваем что реализовали в третьей задаче

from 3 import min_in_mass
"""
from random import randint


def min_in_mass(mass: list):
    """Находит индекс первого минимального элемента в массиве"""
    return mass.index(min(mass))


def two_min_in_mass(mass: list):
    """Находит значения двух минимальных элементов массива"""
    ans = []

    for _ in range(2):
        # Находим индекс минимального элемента
        ind_min = min_in_mass(mass)
        # Записываем значение минимального элемента в ответ
        ans.append(mass[ind_min])
        # Меняем значение в массиве по найденному индексу на заведомо максимальное
        mass[ind_min] = float("inf")

    return ans


if __name__ == '__main__':
    m1 = [5, 6, 3, 8, 2, 10, 1]
    print(m1)
    print(f"Наименьшие : {two_min_in_mass(m1)}")  # Минимальные (1, 2)

    print()

    N = 20
    m2 = [randint(0, 50) for _ in range(N)]
    print(m2)
    print(f"Наименьшие : {two_min_in_mass(m2)}")

