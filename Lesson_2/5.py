"""
5.	Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""


def simbol_key_val(n):
    return f"{n}-{chr(n)} "


def get_simbol_table(first, last, col=5):
    """Вывести на экран коды и символы таблицы ASCII"""
    ans = ''
    counter = 0
    while first <= last:
        ans += simbol_key_val(first)
        first += 1
        counter += 1

        # Перенос строки при превышении количества колонок в строке
        if counter == col:
            ans += '\n'
            counter = 0

    return ans


if __name__ == '__main__':
    print(get_simbol_table(32, 127))
