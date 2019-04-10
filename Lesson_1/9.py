# 9.Вводятся три разных числа. Найти, какое из них
# является средним (больше одного, но меньше другого).


def get_medial_number():
    """определяет среднее из трех чисел"""

    n1 = int(input("n1: "))
    n2 = int(input("n2: "))
    n3 = int(input("n3: "))

    average = (n1 + n2 + n3)/3

    if abs(n1 - average) < abs(n2 - average):
        if abs(n1 - average) < abs(n3 - average):
            print(n1)
        else:
            print(n3)
    else:
        if abs(n2 - average) < abs(n3 - average):
            print(n2)
        else:
            print(n3)


if __name__ == '__main__':
    get_medial_number()
