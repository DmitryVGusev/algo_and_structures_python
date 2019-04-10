"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""


def get_sum(n):
    ans = 0
    while n > 0:
        ans += n
        n -= 1
    return ans


def get_sum_recursive(n):
    if n == 1:
        return 1
    else:
        return n + get_sum_recursive(n - 1)


if __name__ == '__main__':

    # При смене этой переменной используется или не используется рекурсивная сумма
    recursive = False
    if recursive:
        left_sum = get_sum_recursive
    else:
        left_sum = get_sum

    n = 65
    if left_sum(n) == (n * (n + 1) / 2):
        print("Равенство выполняется")
    else:
        print("Равенсвто не выполняется")

