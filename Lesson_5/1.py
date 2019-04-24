"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

from collections import namedtuple, Counter
from random import randint


def gen_stat():
    """
    Генерирует список компаний, их наименования и прибыль за 4 квартала
    """

    Firm = namedtuple("Firm", 'name q1 q2 q3 q4')

    statistic = []
    # Генерируем от 4 до 7 компаний
    for i in range(randint(4, 7)):
        statistic.append(
            Firm("company_{}".format(randint(0, 1000)),
                 randint(0, 1000),
                 randint(0, 1000),
                 randint(0, 1000),
                 randint(0, 1000)))
    return statistic


def get_company_stat(stat: list):
    """определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего."""
    companies = Counter()

    for c in stat:
        companies[c.name] = sum([c.q1, c.q2, c.q3, c.q4]) / 4

    print("Статистика по предприятиям:")
    for name, val in companies.most_common():
        print(f"{name} : {val}")

    print("\nПредприятия, чья прибыль выше среднего:")
    for name, val in companies.most_common()[0:int(len(companies)/2)]:
        print(f"{name} : {val}")

    print("\nПредприятия, чья прибыль ниже среднего:")
    for name, val in companies.most_common()[-int(len(companies)/2)::1]:
        print(f"{name} : {val}")



if __name__ == '__main__':
    # Для упрощения, сгенерируем список компаний и их статистику
    stat = gen_stat()

    # Или попросим пользователя их ввести
    stat = []
    Firm = namedtuple("Firm", 'name q1 q2 q3 q4')
    comp_count = int(input("Введите количество компаний: "))
    for i in range(comp_count):
        name = input("Введите имя компании: ")
        q1 = int(input("Прибыль компании за 1 квартал: "))
        q2 = int(input("Прибыль компании за 2 квартал: "))
        q3 = int(input("Прибыль компании за 3 квартал: "))
        q4 = int(input("Прибыль компании за 4 квартал: "))
        stat.append(Firm(name, q1, q2, q3, q4))
        print()

    get_company_stat(stat)
