# 6.	Пользователь вводит номер буквы в алфавите. Определить, какая это буква.


def ident_letter_by_position():
    """Определяет букву по положению в алфавите"""
    position = int(input("Введите номер буквы: "))
    print(f"Буква '{chr(96 + position)}' находится под номером {position}")


if __name__ == '__main__':
    ident_letter_by_position()
