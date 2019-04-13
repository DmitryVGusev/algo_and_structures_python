"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
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
    number = int(input("Введите число: "))
    print(reverse_num(number))
    print(reverse_num_recursive(number))