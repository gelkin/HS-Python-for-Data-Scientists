from string import ascii_lowercase, ascii_uppercase
from random import choice


def sequence_of_lowercase(size):
    return [choice(ascii_lowercase) for _ in range(size)]


def sequence_of_uppercase(size):
    return [choice(ascii_uppercase) for _ in range(size)]


def sequence_of_numbers(size, max_num=10):
    possible_numbers = list(range(max_num))
    return [str(choice(possible_numbers)) for _ in range(size)]


def generate_test_files(files_n=10, size=100):
    sequence_generators = [sequence_of_lowercase, sequence_of_uppercase, sequence_of_numbers]
    for i in range(files_n):
        generator = choice(sequence_generators)
        sequence = generator(size)
        with open("./test_files/test_{}_{}".format(i, size), 'w') as file:
            file.write(" ".join(sequence))

generate_test_files()