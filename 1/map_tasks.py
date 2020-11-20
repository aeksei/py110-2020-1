from math import sqrt
from operator import add, getitem


def _get_dist(point):  # ToDo: Change to lambda function
    return (point[0] ** 2 + point[1] ** 2) ** 0.5


def map_1():
    """
    Дан список точек, найти самую удаленную точку
    от начала координат
    """
    pts = [
        (3, 4),
        (4.5, 3),
        (2.1, -1),
        (6.8, -3),
        (1.4, 2.9)
    ]

    # list_dist = list(map(_get_dist, pts))
    # print(list_dist)
    # print(max(list_dist))

    print(max(map(_get_dist, pts)))


def map_2():
    """
    Дан список чисел в различных форматах,
    привести их к типу int
    """

    num_list = [
        "12",
        "14",
        3.1415926,
        5,
        0xFF,
        0b1010101010
    ]
    num_list = list(map(int, num_list))
    print(num_list)
    print(0xFF)


def map_3():
    """
    Дан список чисел округлить их до 2 знаков после запятой
    """
    my_floats = [
        4.356345,
        6.0934,
        3.245235,
        9.77545,
        2.164234234,
        8.884234235,
        4.595235346645
    ]

    def _round(a, n=2):  # ToDo: Change to lambda function
        return round(a, n)

    print(list(map(_round, my_floats)))
    print(list(map(round, my_floats, [2] * len(my_floats))))  # ToDo: Change to lambda function


def map_4():
    """
    Найти длину самого длинного слова
    """

    list_words = [
        "Goldenrod",
        "Purple",
        "Salmon",
        "Turquoise",
        "Cyan"
    ]

    print(max(map(len, list_words)))


def map_5():
    """
    Перевести все слова в верхний регистр
    """
    list_words = [
        "Goldenrod",
        "Purple",
        "Salmon",
        "Turquoise",
        "Cyan"
    ]
    print(list(map(str.upper,
                   list_words)))


def map_6():
    a = [1, 2, 3]
    b = [4, 5, 6]

    def _add(first, second):  # ToDo: Change to lambda function
        return first + second

    print(list(map(_add, a, b)))
    print(list(map(add, a, b)))


if __name__ == '__main__':
    # map_1()
    # map_2()
    # map_3()
    # map_4()
    # map_5()
    map_6()
