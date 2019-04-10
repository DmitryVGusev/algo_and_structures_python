# 6.	Пользователь вводит номер буквы в алфавите. Определить, какая это буква.


def find_letter_position():
    """Определяет положение буквы в алфафите"""
    letter = input("Введите букву: ")
    letter_pos = ord(letter) - ord('a') + 1

    print(f"Буква '{letter}' находится в алфавите на {letter_pos} месте")


if __name__ == '__main__':
    find_letter_position()