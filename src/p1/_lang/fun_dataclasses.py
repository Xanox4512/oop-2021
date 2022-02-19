from dataclasses import dataclass, asdict


@dataclass
class A:
    a: int
    b: str

ref = A(b='abc', a=1)

ref.a = 12

g = asdict(ref)
h = ref.__dict__
print(type(g))

z = A(**g)
print(z == ref)
print(g == h)
