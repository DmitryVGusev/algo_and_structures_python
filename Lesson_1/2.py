# 2. Выполнить логические побитовые операции "И", "ИЛИ" и др.
# над числами 5 и 6. Выполнить
# над числом 5 побитовый сдвиг вправо и влево на два знака.


def binary_operations():
    """
    Логические побитовые операции:
    "И", "ИЛИ", "искИЛИ",
    >> 2 , << 2
    """

    num1 = 5
    num2 = 6

    and_op = num1 & num2
    or_op = num1 | num2
    nor_op = num1 ^ num2

    shift_2_to_right = num2 >> 2
    shift_2_to_left = num1 << 2

    print(f"{num1} И {num2} = {and_op}")
    print(f"{num1} ИЛИ {num2} = {or_op}")
    print(f"{num1} искл_ИЛИ {num2} = {nor_op}")

    print(f"{num1} >> 2 = {shift_2_to_right}")
    print(f"{num1} << 2 = {shift_2_to_left}")


if __name__ == '__main__':
    binary_operations()
