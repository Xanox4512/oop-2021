class Car:
    def __init__(self, on: bool):
        self.on = on

    def power_on(self):
        self.on = True

    def power_off(self):
        self.on = False

# bardziej specyficzne wyjątki dla naszego systemu
class OverchargeError(RuntimeError):
    pass


class ChargeWhileOnError(RuntimeError):
    pass


class ElectricCar(Car):
    def __init__(self, on: bool, battery_charge: int, max_battery_charge: int):
        # super.__init__(self, on)
        super().__init__(on)
        self.battery_charge = battery_charge
        self.max_battery_charge = max_battery_charge

    def get_battery_charge(self):
        return self.battery_charge

    def get_max_battery_charge(self):
        return self.max_battery_charge

    def get_on_info(self):
        return self.on

    def charge(self, Ah):
        if not self.on:
            if self.battery_charge + Ah <= self.max_battery_charge:
                self.battery_charge = self.battery_charge + Ah
            else:
                # print('too much power')
                raise OverchargeError('too much power')
        else:
            raise ChargeWhileOnError('cannot charge powered on car')


class Charger:
    def __init__(self, totalAh):
        self.totalAh = totalAh

    def getAh(self):
        return self.totalAh

    def charge(self, car: ElectricCar, value):
        if not car.get_on_info():
            if car.get_battery_charge() + value <= car.get_max_battery_charge():
                car.charge(value)
                self.totalAh = self.totalAh - value
            else:
                raise OverchargeError('too much power')
                # print('too much power')


if __name__ == '__main__':
    electricCar1 = ElectricCar(True, 10, 100)
    print(electricCar1.get_battery_charge())
    electricCar1.power_off()
    electricCar1.charge(10)
    print(electricCar1.get_battery_charge())

    newCharger = Charger(1000)
    newCharger.charge(electricCar1, 10)
    print(electricCar1.get_battery_charge())

    newCharger.charge(electricCar1, 500)
    print(electricCar1.get_battery_charge())

    print(newCharger.getAh())
