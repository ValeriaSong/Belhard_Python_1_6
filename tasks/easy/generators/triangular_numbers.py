"""
Написать генератор triangular_numbers, который возвращает подряд числа
треугольные числа


Формула:
Tn = 1 / 2 * n * (n + 1)


Например:
tn_gen = triangular_numbers()

next(tn_gen) -> 1
next(tn_gen) -> 3
next(tn_gen) -> 6
next(tn_gen) -> 10
next(tn_gen) -> 15
next(tn_gen) -> 21
"""


def triangular_numbers(a=1):
    while True:
        yield 1 / 2 * a * (a + 1)
        a += 1
