from typing import List


class Gabon:
    w: List

    def __init__(self, w) -> None:
        self.w = w

    def __iter__(self):
        print('itera called...')
        self.x = -1
        return self

    def __next__(self):
        self.x += 1
        if self.x < len(self.w):
            return self.w[self.x-1]
        else:
            raise StopIteration

g = Gabon(['City1', 'City2'])

for i in g:
    print(i)


