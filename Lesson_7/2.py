"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""
from random import randint


def merge_sort(m):
    if len(m) <= 1:
        return m
    middle = len(m) // 2
    left = merge_sort(m[:middle])
    right = merge_sort(m[middle:])

    return merge_mass(left, right)


def merge_mass(left: list, right: list):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    result += left
    result += right

    return result


if __name__ == '__main__':
    N = 10
    mass = [randint(0, 49) for _ in range(N)]

    print(mass)
    print(merge_sort(mass))
    """
    [3, 29, 41, 35, 6, 10, 10, 4, 6, 11]
    [3, 4, 6, 6, 10, 10, 11, 29, 35, 41]
    """
