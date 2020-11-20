# lambda_func = lambda x: x + 1
#
# print(lambda_func(5))

def lambda_3():

    def add(n):
        def inline_add(x):
            return x + n
        return inline_add


    lambda_func = lambda n: lambda x: x + n
    add_5 = lambda_func(5)  # возвращаю функцию
    print(add_5(10))
    print(add_5(100))

    n = 5
    list_tuple = [(i, n - i) for i in range(n + 1)]
    print(list_tuple)


def lambda_1():
    n = 5
    list_tuple = [(n - i, i) for i in range(n + 1)]
    print(list_tuple)

    l = sorted(list_tuple,
               key=lambda x: x[1],
               reverse=True)
    print(l)


def lambda_2():
    str_ = "Один два шесть восемь"
    list_words = str_.split()  # ['Один', 'два', 'шесть', 'восемь']

    print(sorted(list_words,
                 key=len,
                 reverse=True))


def arg_lambda():
    f = lambda *args: '-'.join(args)
    print(f('1', '2', '3', '4'))


if __name__ == '__main__':
    # lambda_1()
    # lambda_2()
    arg_lambda()
