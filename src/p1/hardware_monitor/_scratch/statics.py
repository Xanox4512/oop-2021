class A:
    g: str

    def print_g(self):
        print(self.g)

    @staticmethod
    def first_letter(s: str) -> str:
        return s[0]


# a = A()
# print(a.first_letter('abc'))

print(A.first_letter('abc'))
print(A().first_letter('abc'))
