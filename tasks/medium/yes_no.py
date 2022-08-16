"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""


def yes_or_no(numbers):
    occur_before = set()
    for num in numbers:
        if num in occur_before:
            print('Yes')
        else:
            print('No')
            occur_before.add(num)
