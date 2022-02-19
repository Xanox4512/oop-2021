

def foo():
    # raise RuntimeError('too bad')
    raise IndexError('too bad')



if __name__ == '__main__':
    gg = (IndexError, AssertionError)
    try:
        foo()
    except gg:
        print(f'catched one of {gg} exceptions')
    except RuntimeError as e:
        print(f'ok; komunikat błedu: {str(e)}')
        raise e
    except KeyError:
        print('ke')