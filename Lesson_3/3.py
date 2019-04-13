#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.
from random import randint


def min_in_mass(mass: list):
    """Находит индекс первого минимального элемента в массиве"""
    return mass.index(min(mass))


def max_in_mass(mass: list):
    """Находит индекс первого минимального элемента в массиве"""
    return mass.index(max(mass))


if __name__ == '__main__':

    N = 5
    # Генерируем массив целых чисел
    m = [randint(1, 50) for _ in range(N)]

    # Отображаем изначальный массиы
    print(m)

    # Находим индексы минимального и максимального элемента
    ind_min = min_in_mass(m)
    ind_max = max_in_mass(m)

    # Меняем максимальный и минимальный элемент местами
    m[ind_min], m[ind_max] = m[ind_max], m[ind_min]

    # Отображаем итоговый массив
    print(m)

