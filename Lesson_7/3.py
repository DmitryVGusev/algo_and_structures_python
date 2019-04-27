"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""

"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""
from random import randint


def find_median(m):
    """Находит медиану в массиве"""
    for i in range(len(m)):
        L = 0  # Количество эелементов меньше
        R = 0  # Количество эелементов больше
        M = 0  # Количество эелементов равно
        for j in range(len(m)):
            if m[j] > m[i]:
                R += 1
            elif m[j] < m[i]:
                L += 1
            else:
                M += 1
        if abs(L - R) <= (M - 1):
            return m[i]


def find_median_via_sort(m):
    """Находит медиану в массиве используя сортировку"""
    return sorted(m)[len(m)//2]


if __name__ == '__main__':

    M = 4
    rnd_mass = [randint(1, 50) for _ in range(2*M + 1)]

    # Получаем ответ
    ans = find_median(rnd_mass)
    ans_sort = find_median_via_sort(rnd_mass)

    print(rnd_mass)
    print(f"Медиана без сортировки: {ans}")
    print(sorted(rnd_mass))
    print(f"Медиана с сортировкой:  {ans_sort}")

    """
    [11, 40, 15, 16, 33, 24, 37, 40, 6]
    Медиана без сортировки: 24
    [6, 11, 15, 16, 24, 33, 37, 40, 40]
    Медиана с сортировкой:  24
    """