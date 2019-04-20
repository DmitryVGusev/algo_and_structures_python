"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""


def reverse_num(num):
    """Возвращает заданное число в обратном порядке"""
    reverse = ''
    while num > 0:
        reverse += str(num % 10)
        num //= 10
    return reverse


def reverse_num_recursive(num, rev=''):
    """Возвращает заданное число в обратном порядке"""
    if num > 0:
        rev += str(num % 10)
        return reverse_num_recursive(num // 10, rev=rev)
    else:
        return rev


if __name__ == '__main__':
    import timeit
    print(timeit.timeit("reverse_num(1234567)",
                        setup="from __main__ import reverse_num"))
    print(timeit.timeit("reverse_num_recursive(1234567)",
                        setup="from __main__ import reverse_num_recursive"))
