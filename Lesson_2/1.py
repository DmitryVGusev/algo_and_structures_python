"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
"""


def simple_calc(num1, num2, operation):
    """Возвращает результат арифметической операции над двумя числами"""
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Деление на ноль!"
        else:
            return num1 / num2
    else:
        return f"неизвестный оператор - {operation}"


def input_form():
    """
    Запрашивает ввод с клавиатуры и вызывает функцию арифметической операции.

    :return: True при штатном завершении, False при необходимости выйти из программы
    """

    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второк число: "))

    # Обработка арифметического знака
    while True:
        operation = input("Введите знак операции: ")

        if operation is '0':
            return False
        if (
            operation == '+'
            or operation == '-'
            or operation == '*'
            or operation == '/'
        ):  # равносильно if operation in ['+', '-', '*', '/']
            break
        else:
            print("Ошибка арифметического знака!")

    print(f"Результат: {simple_calc(num1, num2, operation)}\n")
    return True


def input_form_recursive():
    """Обертка для рекурсивного вызова функции"""
    input_form() and input_form_recursive()


if __name__ == '__main__':
    # Установить при проверки рекурсии
    recursion = False

    if recursion:
        # С рекурсией
        input_form_recursive()

    else:
        # Без рекурсии
        ret = True
        while ret:
            ret = input_form()


