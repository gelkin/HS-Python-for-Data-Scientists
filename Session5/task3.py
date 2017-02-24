from functools import reduce
import itertools


# task 1
def sin_monomes_generator(x, a):
    """
    Generates taylor of sin(x) at 'a'
    :param evaluation_point: - x
    :param decomposition_point: - a
    :return:
    """
    n = 0
    coef = 1
    mult = x - a
    fac = 1
    while True:
        yield coef * mult / fac
        coef = -coef
        n += 1
        mult *= mult * mult
        fac *= 2 * n * (2 * n + 1)

print(list(itertools.islice(sin_monomes_generator(1, 0), 0, 4)))


# task 2
def approximate_sin(x, a, eps):
    check = lambda monome: abs(monome) >= eps
    sum = lambda x, y: x + y
    return reduce(sum, itertools.takewhile(check, sin_monomes_generator(x, a)), 0)

print(approximate_sin(1, 0, 0.001))


# task 3
def taylor_sin_order(x, a, eps):
    check = lambda monome: abs(monome) >= eps
    return sum(1 for _ in itertools.takewhile(check, sin_monomes_generator(x, a)))

print(taylor_sin_order(1, 0, 0.000001))
