"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""


def count_even_and_odd(digit):
    """Возвращает количество четных и нечетных цифр введенного натурального числа"""
    even = 0
    odd = 0

    while digit > 0:
        # Берем правую цифру
        last = digit % 10

        # Записываем цифру к четным или нечетным
        if last % 2 == 0:
            even += 1
        else:
            odd += 1

        # Смещаемся на цифру влево
        digit //= 10

    print(f"Четных: {even}, нечетных: {odd}")


def count_even_and_odd_recursive(digit, even=0, odd=0):
    """Возвращает количество четных и нечетных цифр введенного натурального числа"""

    # Берем правую цифру
    last = digit % 10

    # Записываем цифру к четным или нечетным
    if last % 2 == 0:
        even += 1
    else:
        odd += 1

    # Условие остановки рекурсии
    if digit == last:
        print(f"Четных: {even}, нечетных: {odd} (Рекурсивно)")
    else:
        # Смещаемся на цифру влево
        count_even_and_odd_recursive(digit=(digit // 10), even=even, odd=odd)


if __name__ == '__main__':
    digit = int(input("Введите число: "))
    count_even_and_odd(digit)
    count_even_and_odd_recursive(digit)
