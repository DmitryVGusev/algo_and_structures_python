#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.


def max_negative(mass: list):
    """Находит самый максимальный отрицательный элемент массива и его позицию"""

    # Инициализируем пустой ответ
    ans_ind = None
    ans_val = float("-inf")

    for i in range(len(mass)):
        if mass[i] < 0 and mass[i] > ans_val:
            ans_ind = i
            ans_val = mass[i]

    print(f"Максимальный отрицательный элемент массива: {ans_val}, индекс {ans_ind}")


if __name__ == '__main__':
    m = [-3, -2, -5, -1, 0, 1, 3, 5]
    max_negative(m)

