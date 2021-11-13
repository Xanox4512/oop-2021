class Power:
    power_consumption: int
    def get_power_consumtion(self):
        return self.power_consumption
    pass
    # def __init__(polygonType):
    #     print('Polygon is a ', polygonType)


class Triangle(Power):
    def __init__(self):
        Power.__init__('triangle')


print(issubclass(Triangle, Power))
# print(issubclass(Triangle, list))
# print(issubclass(Triangle, (list, Polygon)))
# print(issubclass(Polygon, (list, Polygon)))