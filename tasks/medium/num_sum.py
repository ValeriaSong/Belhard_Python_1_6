"""
Написать рекурсивную функцию sum_of_numbers, которая будет вычислять сумму
цифр целого числа.

Можно пользоваться только функциями, операторами и условиями.
"""


def sum_of_numbers(n, sum=0):
    if n == 0:
        return sum
    digit = n % 10
    sum = sum + digit
    return sum_of_numbers(n // 10, sum=sum)
