# 8.	Определить, является ли год, который ввел пользователем,
# високосным или не високосным.
#Год является високосным в двух случаях: либо он кратен 4,
# но при этом не кратен 100, либо кратен 400.

def is_leap_year():
    """Определяет, является ли введенный год високосным"""

    year = int(input("Введите год: "))
    if year % 400 == 0:
        print("Год является високосным")
    else:
        if year % 4 == 0 and year % 100 != 0:
            print("Год является високосным")
        else:
            print("Год не является високосным")


if __name__ == '__main__':
    is_leap_year()
