# 4.	Определить, какое число в массиве встречается чаще всего.
from random import randint


def max_counts_in_mass(mass: list):
    """Определяет, какое число в массиве встречается чаще всего"""
    # Генерируем словарь "Число: количество повторений в массиве"
    counts = dict()
    for el in mass:
        if el in counts:
            counts[el] += 1
        else:
            counts[el] = 1

    return max(counts, key=counts.get)


if __name__ == '__main__':

    # Инициализируем массив с повторяющимеся элементами
    N = 24
    m = [randint(0, 8) for _ in range(N)]

    print(max_counts_in_mass(m))
