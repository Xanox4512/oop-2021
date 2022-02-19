class A:
    _a: int = 5

    def square_a(self):
        self._a **= 2

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a = value


class Wrapper(A):
    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        raise RuntimeError('Setter not allowed')


ref = Wrapper()
print(ref.a)
ref.a = 'abc'
