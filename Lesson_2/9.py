"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""

def get_num_sum(num):
    """Возвращает сумму цифр числа"""
    ans = 0
    while num > 0:
        ans += (num % 10)
        num //= 10
    return ans


def get_num_sum_recursive(num):
    """Возвращает сумму цифр числа"""
    if num == 0:
        return 0
    else:
        return num % 10 + (get_num_sum_recursive(num // 10))


if __name__ == '__main__':
    # Переключение на использование рекурсивной функции
    recursive = False
    if recursive:
        num_sum = get_num_sum_recursive
    else:
        num_sum = get_num_sum

    biggest = 1
    while True:
        num = int(input("Введите натуральное число (0 - завершение): "))
        if num == 0:
            break
        if num_sum(num) > num_sum(biggest):
            biggest = num

    print(f"Число с наибольшой суммой из введенных: {biggest} (сумма = {num_sum(biggest)})")

