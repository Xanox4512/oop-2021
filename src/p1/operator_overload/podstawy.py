from dataclasses import dataclass

"""
Na koniec zadaniem będzie utworzenie klasy Fract, z polami p:int, q:int, implementującej
ułamki zwykłe o wartości p/q


"""


class F:
    a: int

    def __init__(self, a: int) -> None:
        self.a = a

    def __repr__(self) -> str:
        return f'F(a={self.a})'

    # potrzebne do a<b, oraz .sort()
    def __lt__(self, other):
        return (self.a < other.__a)

    # potrzebne do set(), dict()
    def __hash__(self) -> int:
        return self.a.__hash__()

    def __eq__(self, other):
        return self.a == other.__a

    # implementacja arytmetyki
    def __add__(self, other):
        return F(self.a + other.__a)

    def __mul__(self, other):
        return F(self.a * other.__a)



"""
Zadanie(a): 

Utworzyć klasę Fract, z polami p:int, q:int, implementującą
ułamki zwykłe o wartości p/q

A) Konstruktor, repr
B) Operator potrzebny do .sort() (czyli __lt__)
C) Operator potrzebny do set()... ale napisać tak, żeby 2/3 == 4/6 .... 
D) Napisać metody from_float(), to_float() implementujące zamianę (jak najdokładniejszą) na ułamki dziesiętne...
   0.333333333333333333 → Fract(1,3)
E) Zaimplementować operatory arytmetyczne:
+	__add__(self, other)
–	__sub__(self, other)
*	__mul__(self, other)
/	__truediv__(self, other)

---> czyli dodawanie ułamków.... .... ale też dodawanie liczb całkowitych do ułamków... 
dla ostatniego -- wykorzystać isinstance(other), czyli coś typu:
        if isinstance(other, F):
            return F(self.a + other.a)
        else:
            return F(self.a + other)    #int

F*) Zaimplemntować operatory korzystając z (odwołując się do) __eq__ i __lt__: 
    def __ne__(self, other):
        return not(self.__eq__(self, other))

    def __le__(self, other):
        return ...

    def __gt__(self, other):
        return ...

    def __ge__(self, other):
        return ... 

"""




a = F(10)
b = F(20)
c = F(10)

w = [b, a, c]
# w.sort()
# print(w)
# print(a < b)

s = set(w)
print(s)
print(a.__hash__())
print(b.__hash__())
print(c.__hash__())
print(a == c)

d = dict()
d[a] = 90
d[b] = 50
d[c] = 100
print(d)

print(a + b)
