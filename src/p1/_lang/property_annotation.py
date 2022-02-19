class A:
    __a: int

    @property
    def a(self):
        print('getting a')
        return self.__a

    @a.setter
    def a(self, value):
        print(f'setting a={value}')
        self.__a = value

ref = A()
ref.a = 15
print(ref.a)
try:
    # print(ref.__a)
    ref.__a = 11
except AttributeError as e:
    print('ok')
# ref.__a = 11