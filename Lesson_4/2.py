"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""
import timeit


def prime_list(num):
    """
    Выводит список простых чисел до указанного
    :param num:
    :return:
    """
    ans = [2]
    for i in range(3, num+1):
        if [x for x in range(2, i) if i % x == 0]:
            continue
        ans.append(i)
    return ans


def prime_list_2(num):
    """
    Выводит список простых чисел до указанного
    :param num:
    :return:
    """
    ans = [2]
    for i in range(3, num+1):
        if [x for x in range(2, i) if i % x == 0]:
            continue
        ans.append(i)
    return ans


def resheto(num):
    """
    Решето Эратосфена. Возвращает список простых чисел до введенного.
    :param num:
    :return:
    """
    ans = [x for x in range(2, num+1)]
    for i in ans:
        if i == 0:
            continue
        ind = 2*i - 2
        while ind <= num -2:
            ans[ind] = 0
            ind += i
    return [x for x in ans if x != 0]




if __name__ == '__main__':
    print(timeit.timeit("prime_list(100)", number=1000, setup="from __main__ import prime_list"))
    print(timeit.timeit("resheto(100)", number=1000, setup="from __main__ import resheto"))
    # print(prime_list(40))
    # print(resheto(40))
# print(timeit.timeit("gen_list(20)", setup="from __main__ import gen_list"))
