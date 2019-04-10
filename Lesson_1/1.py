# -*- coding: utf-8 -*-
# 1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.


def sum_and_mult():
    """Находит сумму и произведение цифр трехзначного числа"""
    three_digit_num = int(input("Введите трехзначное число: "))

    first_num = three_digit_num // 100
    second_num = three_digit_num // 10 % 10
    third_num = three_digit_num % 10

    summ = first_num + second_num + third_num
    mult = first_num * second_num * third_num

    print(f"Сумма цифр трехзначного числа - {summ}")
    print(f"Произведение цифр трехзначного числа - {mult}")


if __name__ == '__main__':
    sum_and_mult()