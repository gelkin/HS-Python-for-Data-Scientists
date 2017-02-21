from os import listdir
from Session1.hw1 import average_counter
import timeit


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


def time_func_on_arg(func, arg, repeat_n=100):
    wrapped = wrapper(func, arg)
    return timeit.timeit(wrapped, number=repeat_n)


def test_hw1():
    path = "./test_files"
    test_files = [f for f in listdir(path)]
    print("filename\ttime")
    for test_file in test_files:
        with open("{}/{}".format(path, test_file), 'r') as file:
            sequence = file.readline().split()
            time = time_func_on_arg(average_counter, sequence)
            print("{}\t{:.4f}".format(test_file, time))

test_hw1()