from time import time as t
from time import sleep


def counter(fn):
    def wrapper(*args, **kwargs):
        # до вызыва функции
        print('-' * 10)

        result = fn(*args, **kwargs)

        # действия после вызыва
        wrapper.count += 1
        print(f'Функция "{fn.__name__}" была вызвана {wrapper.count} раз')

        return result

    wrapper.count = 0  # инициализируем атрибут функции, для подсчета вызовов

    return wrapper


def counter_main():
    # @counter  # my_print = counter(my_print)
    def my_print():
        print('Hello, World')

    # for _ in range(10):
    #     my_print()

    print(my_print.__dict__)
    my_print.attr = 'Hello World'
    print(my_print.__dict__)


def time(fn):
    def wrapper(*args, **kwargs):
        t0 = t()  # время начала
        sleep(1)

        fn(*args, **kwargs)

        dt = t() - t0
        print(f"Функция {fn.__name__} выполнялась {dt:.7f} секунд")

    return wrapper


def time_main():
    @time
    def pow_2(n):
        print(2 ** (10 * n))

    for i in range(10):
        pow_2(i)


def cache(fn):
    def wrapper(*args):
        local_cache = fn.__dict__  # кеш свой для каждой функции

        print(f"Кеш до вызова функции {local_cache}")
        if args not in local_cache:
            result = fn(*args)
            local_cache[args] = result
            print(f'Помещаем в кеш новый результат {args}: {result}')

        print(f"Кеш после вызова функции {local_cache}")
        return local_cache[args]

    return wrapper


def cache_main():
    @cache
    def mul(a, n):
        return a * n

    for i in range(10):
        print(mul(i, i ** 2))
        print('-' * 5)
        print(mul(i, i ** 2))


def timeit(count=1):
    def time_decorator(fn):
        def wrapper(*args, **kwargs):
            total_time = 0
            for _ in range(count):
                t0 = t()  # время начала
                fn(*args, **kwargs)
                dt = t() - t0
                total_time += dt
            print(f"Функция {fn.__name__} выполнялась {total_time / count:.7f} секунд")
        return wrapper
    return time_decorator


def timeit_main():
    @timeit(100)
    def pow_():
        return 2 ** 20

    pow_()


if __name__ == '__main__':
    # counter_main()
    # time_main()
    # cache_main()
    timeit_main()
