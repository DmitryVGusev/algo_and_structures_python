"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.
"""


def count_figure_in_line(num, f):
    ans = 0
    while num > 0:
        # Проверка что правая цифра совпадает с искомой
        if num % 10 == f:
            ans += 1
        num //= 10
    return ans


def count_figure_in_line_recursive(num, f):
    # Условие выхода из рекурсии
    if num == 0:
        return 0

    # Проверка что правая цифра совпадает с искомой
    if num % 10 == f:
        ans = 1
    else:
        ans = 0

    return ans + count_figure_in_line_recursive(num//10, f)


if __name__ == '__main__':
    print(count_figure_in_line(424442, 4))
    print(count_figure_in_line_recursive(3113, 3))
