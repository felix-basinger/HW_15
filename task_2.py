import argparse

parser = argparse.ArgumentParser(description="Принимаем строку с числами a и b")
parser.add_argument("-a", type=int, default=1)
parser.add_argument("-b", type=int, default=10)

args = parser.parse_args()
print(args)


def sqrt_range(a, b):
    """
    Функция для возведения чисел в квадрат в определенном диапазоне.

    :param a: Начало диапазона.
    :param b: Конец диапазона.
    :return: Список чисел, возведенных в квадрат.
    """
    my_list = [i ** 2 for i in range(a, b)]
    return my_list


print(sqrt_range(args.a, args.b))
