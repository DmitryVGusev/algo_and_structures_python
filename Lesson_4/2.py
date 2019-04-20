"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""
import timeit
import cProfile

"""
Первый вариант реализации поиска массива простых чисел:
проверяем что сисло не делится на все числа до него
Сложность алгоритма, как я понимаю O=n*(sum(0,N))
"""


def prime_list(num):
    if num < 2:
        return []
    ans = [2]
    for i in range(3, num+1):
        if [x for x in range(2, i) if i % x == 0]:
            continue
        ans.append(i)
    return ans


# 0.424сек - результат вызова функции 1000 раз
print(timeit.timeit("prime_list(100)", number=1000, setup="from __main__ import prime_list"))


"""
Второй вариант реализации поиска массива простых чисел:
проверяем что число не делится на числа в диапозоне (2, корень числа)
"""


def prime_list_2(num):
    if num < 2:
        return []
    ans = [2]
    for i in range(3, num+1):
        if [x for x in range(2, int(i**0.5) + 1) if i % x == 0]:
            continue
        ans.append(i)
    return ans


# 0.182сек - результат вызова функции 1000 раз
print(timeit.timeit("prime_list_2(100)", number=1000, setup="from __main__ import prime_list_2"))

"""
Третий вариант - поиск массива простых чисел через решето Эратосфена
"""


def resheto(num):
    if num < 2:
        return []
    ans = [x for x in range(2, num+1)]
    for i in ans:
        if i == 0:
            continue
        ind = 2*i - 2
        while ind <= num -2:
            ans[ind] = 0
            ind += i
    return [x for x in ans if x != 0]
    

# 0.037сек - результат вызова функции 1000 раз
print(timeit.timeit("resheto(100)", number=1000, setup="from __main__ import resheto"))

"""
В среднем, решето Эратосфена быстрее исходного алгоритма на порядок, 
и более чем в четыре раза быстрее улучшенного исходного алгоритма
"""


def main():
    n = 10000
    prime_list(n)
    prime_list_2(n)
    resheto(n)


cProfile.run('main()')

"""
22461 function calls in 4.808 seconds
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.038    0.038    4.748    4.748 2.py:15(prime_list) - Первый алгоритм
     9998    4.710    0.000    4.710    0.000 2.py:18(<listcomp>)
        1    0.011    0.011    0.053    0.053 2.py:34(prime_list_2) - Второй алгоритм
     9998    0.042    0.000    0.042    0.000 2.py:37(<listcomp>)
        1    0.005    0.005    0.006    0.006 2.py:51(resheto) - Решето Эратосфена
        1    0.001    0.001    0.001    0.001 2.py:52(<listcomp>)
        1    0.001    0.001    0.001    0.001 2.py:60(<listcomp>)
        1    0.000    0.000    4.808    4.808 2.py:71(main)
        1    0.000    0.000    4.808    4.808 <string>:1(<module>)
        1    0.000    0.000    4.808    4.808 {built-in method builtins.exec}
     2456    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""


"""
По итогам эмпирической оценки алгоритмов 
можно с уверенностью сказать что Решето Эратосфена работает быстрее всего.
"""