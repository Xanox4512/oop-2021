import datetime
import time
from math import sin
from random import randint

from cachetools import cached, TTLCache

from p1.decorators import profile


@cached(cache=TTLCache(maxsize=1024, ttl=10))
def foo(x):
    print(f'odpalamy "ciężką" funkcję - dla {x}')
    return x ** 2


"""
Cel: annotacje/interceptory... wykonać jakąś akcję przed i po wykonaniu funkcji
"""


def logged(fn):
    def wrapper(*args, **kw):
        print(f'{datetime.datetime.now()}] przed operacją, args={args}')
        ret = fn(*args, **kw)
        print(f'{datetime.datetime.now()}] po operacji')
        return ret

    return wrapper


def retry(times, backoff_type: str = 'linear', factor: int = 1):
    def decorator(fn):
        def wrapper(*args, **kw):
            for i in range(times):
                try:
                    ret = fn(*args, *kw)
                    return ret
                except:
                    # retry 0/5
                    print(f'Błąd przy wykonaniu funkcji {fn.__name__}, attempt {i + 1}/{times}')
            raise RuntimeError(f'Cannot execute {fn.__name__}')

        return wrapper

    return decorator


class Logger:
    def log(self, message):
        raise NotImplemented()


class FileBasedLogger(Logger):
    def log(self, message):
        print('message')


@logged(logger=FileBasedLogger(filename='app.log'))
@retry(times=5, backoff_type='exponential', factor=2)
@unsafe(ignored_errors=(IndexError, KeyError))
def get_money(bank, amount):
    if randint(0, 10) == 0:
        print('→→→→')
    else:
        raise IndexError('haha!!')


@logged
@retry(times=2)
def put_money(bank, amount):
    print('←←←←')


@logged
def transfer_money(bank1, bank2, amount):
    print('↔↔↔↔')


def wrapper(fn, arg):
    return fn(arg)


if __name__ == '__main__':
    put_money('b', 10)
    transfer_money('b', 'g', 10)
    get_money('c', 10)

    print(datetime.datetime.now())
