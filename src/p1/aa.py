class A:
    on: bool

    def __init__(self, on: bool):
        self.on = on


class EV(A):

    def __init__(self, on: bool):
        super().__init__(on)


ev = EV(True)


print(ev.on)