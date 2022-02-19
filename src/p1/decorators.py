import time


def profile(fct):
    def wrapper(*args, **kw):
        start = time.time()
        ret = fct(*args, **kw)
        print(f'Function {fct.__name__} done in {time.time() - start:.3f}s')
        return ret

    return wrapper


def best_profile(arg, age):
    def decorator(fn):
        def wrapper(*args, **kw):
            print(f'ok, arg={arg}, age={age}')
            ret = fn(*args, *kw)
            return ret

        return wrapper

    return decorator


@profile
def foo():
    time.sleep(0.3)


@best_profile(arg=12, age=15)
def goo():
    time.sleep(0.3)


if __name__ == '__main__':
    goo()
