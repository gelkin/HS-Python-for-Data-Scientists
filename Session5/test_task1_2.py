# Write a decorator, which caches the results of the function
# call and if the function is called with the same argument
# values returns cached values instead of doing the actual
# function's computation.


def cache(decorated_function):
    data = {}

    def wrapper(*args, **kwargs):
        if (args, tuple(kwargs.items())) in data:
            return data[(args, tuple(kwargs.items()))]
        res = decorated_function(*args, **kwargs)
        data[(args, tuple(kwargs.items()))] = res
        return res
    return wrapper


@cache
def decorated_function(a, b, c=1):
    return a, b, c

