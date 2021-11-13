def foo(n):
    print(f'foo with n={n}')
    goo(n)
    print('ok -- zakończyłem foo')


def goo(n):
    # funkcja powinna zwrócić krytyczny błąd gdy n=3....
    if n == 3:
        raise RuntimeError('błąd!!! n nigdy nie może być równe 3')
    print(f'goo with n={n}')
    print('ok zakończyłem goo')


if __name__ == '__main__':
    try:
        foo(3)
        print('koniec programu, operacje powiodły się')
    except RuntimeError as e:
        print(f'wystąpił błąd: {e}')
    finally:
        print('to się odpali zawsze')
    print('---------FIN--------------')
