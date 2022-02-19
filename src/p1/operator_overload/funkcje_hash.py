

class G:
    a: int
    b: str

    def __init__(self, a:int, b:str) -> None:
        self.a = a
        self.b = b

    def __hash__(self):
        return (self.a, self.b).__hash__()


x = (1,'abc')
y = (2,'abc')
z = (1,'abz')
print(x.__hash__())
print(y.__hash__())
print(z.__hash__())
print(len('7564483643688415740'))