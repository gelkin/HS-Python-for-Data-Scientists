# task 1


# Decorator, which checks compliance of function's signature to given interface
import string


def interface_decorator_maker(kwargs_interface):
    def interface_decorator(decorated_function):
        def wrapper(*args, **kwargs):
            if kwargs.keys() != set(kwargs_interface):
                print("Function doesn't satisfy the interface")
            else:
                return decorated_function(*args, **kwargs)
        return wrapper
    return interface_decorator


@interface_decorator_maker(['key_a'])
def test_func(key_a='a'):
    print(key_a)


# Decorator, which decorates function with a provided decorator
def decorator_with_decorator(input_decorator):
    def actual_decorator(decorated_function):
        def wrapper(*args, **kwargs):
            return decorated_function(*args, **kwargs)
        return input_decorator(wrapper)
    return actual_decorator


def sample_decorator(decorated_function):
    def wrapper():
        print('Statements executed before decorated_function is called')
        decorated_function()
        print('Statements executed after decorated_function is called')
    return wrapper


@decorator_with_decorator(sample_decorator)
def simple_function():
    print('Simple function')


# task 2
# Assume we have an arbitrary text and plan to prepare it for a further data analysis.
# The text might contain html tags, emails, latex commands. The task is to create a
# configurable text preprocessor, which allows to remove certain elements from provided text.
# The following filters should be supported:
# * Removal of punctuation symbols from a given list
# * Removal of stop words from a given list
# * Removal of HTML tags
# * Removal of e-mails

from nltk.corpus import stopwords
import re


# Sample chain of responsibility
class ChainLink:
    def __init__(self, chain, strategy):
        self.strategy = strategy
        self.chain = chain
        self.chain.append(self)

    def next(self):
        location = self.chain.index(self)  # where this link is in the chain
        if not self.end():
            return self.chain[location + 1]

    def end(self):
        return (self.chain.index(self) + 1 >=
                len(self.chain))

    def __call__(self, request):
        r = self.strategy(request)
        if self.end():
            print("Chain execution stopped")
            return r
        return self.next()(r)


class FirstHandle:
    def __call__(self, request):
        print('Trying first handle')
        return 1 == request  # Good practice to use a result object, which can be analysed by chain object


class SecondHandle:
    def __call__(self, request):
        print('Trying second handle')
        return 2 == request


class ThirdHandle:
    def __call__(self, request):
        print('Trying third handle')
        return 3 == request

#
# chain = []
# ChainLink(chain, FirstHandle())
# ChainLink(chain, SecondHandle())
# ChainLink(chain, ThirdHandle())


class PunctHandle:
    def __call__(self, request):
        print('Remove Punctuation Handle')
        res = [word for word in request.split() if word not in string.punctuation]
        return ' '.join(res)


class StopwordsHandle:
    def __call__(self, request):
        print('Remove stopwords Handle')
        stop = set(stopwords.words('english'))
        res = [word for word in request.split() if word not in stop]
        return ' '.join(res)


class RemoveHTMLHandle:
    def __call__(self, request):
        print('Remove html Handle')
        res = [word for word in request.split() if word[0] != '<' or word[-1] != '>']
        return ' '.join(res)


class RemoveEmailHandle:
    def __call__(self, request):
        pattern = re.compile(".+@.+\..+")
        print('Remove email Handle')
        res = [word for word in request.split() if not pattern.match(word)]
        return ' '.join(res)

chain = []
ChainLink(chain, PunctHandle())
print(chain[0]("dew, frevre . rev"))

chain = []
ChainLink(chain, RemoveHTMLHandle())
print(chain[0]("this <is> a </tree>"))

chain = []
ChainLink(chain, RemoveEmailHandle())
ChainLink(chain, PunctHandle())
print(chain[0]("this <is> a my@mail.ru . my@mailru && mymail.ru , "))


