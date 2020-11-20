from itertools import count, repeat, zip_longest
import random
from operator import getitem


def check_odd(n): return n % 2 == 0  # ToDo: Change to lambda function


def pow_2(n): return n ** 2  # ToDo: Change to lambda function


def filter_1():
    n = 10
    all_number = count(1, 1)
    all_odd = filter(check_odd, all_number)
    all_odd_pow_2 = map(pow_2, all_odd)

    print(f'Первые {n} элементов')
    for _ in range(n):
        print(next(all_odd_pow_2))

    print(f'Вторые {n} элементов')
    for _ in range(n):
        print(next(all_odd_pow_2))


def filter_2():
    """
    Все отрицательные кратные 3
    """
    # import random

    def neg_and_3(n): return (n < 0) and (n % 3 == 0)  # ToDo: Change to lambda function

    n = 100
    list_num = [random.randint(-100, 100) for _ in range(n)]
    print(list(filter(neg_and_3, list_num)))


def get_char(i, str_): return getitem(str_, i)  # ToDo: Change to lambda function


def filter_3():
    """
    filter
    list comprehensions
    """
    # from operator import getitem, index
    index = [1, 3, 5]
    print(list(map(get_char, index, repeat("Всем привет", len(index)))))


def zip_1():
    figures = ['Круг', 'Квадрат', 'Ромб', "Овал"]
    colors = ['Красный', 'Синий', 'Зеленый']
    default_color = 'Желтый'

    for fig, col in zip(figures, colors):
        print(f"Фигура {fig} окрашена в {col} цвет")

    print("--------")

    for fig, col in zip_longest(figures, colors, fillvalue=default_color):
        print(f"Фигура {fig} окрашена в {col} цвет")


def enumerate_1():
    str_ = 'Всем привет'
    print(list(enumerate(str_)))


def enumerate_2(sequence, start=0, step=1):
    """
    #todo step
    :param sequence:
    :param start:
    :param step:
    :return:
    """

    index = range(start, len(sequence) + start, step)
    return zip(index, sequence)


def debug():
    print("1")
    print("2")
    print("3")
    print("4")


g = 1000


# def loop_for():
#     for i in range(-100, 100):
#         a = g / i
#         print(i, a)


if __name__ == '__main__':
    # filter_1()
    # filter_2()
    # filter_3()
    # zip_1()
    # enumerate_1()
    # for index, value in enumerate_2((5, 7, 10)):
    #     print(f"Index: {index} | Value: {value}")
    # loop_for()

    int('123F')
    int([2121])
