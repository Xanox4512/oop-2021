import unittest
from unittest.mock import MagicMock

from p1.ev_tests_mocks.car_electric_charger import ElectricCar, ChargeWhileOnError, OverchargeError, Charger


class Calculator:
    def add(self, a, b):
        return a + b


class TestSum(unittest.TestCase):

    def test_sum(self):
        c = Calculator()
        c.add = MagicMock(return_value=5)
        self.assertEqual(c.add(2, 2), 5, 'Używamy wartości zwracanych z mock-a, a nie klasy')

    def test_create_car(self):
        # arrange
        c = ElectricCar(False, battery_charge=50, max_battery_charge=100)

        # act
        pass

        # assert
        assert c.get_on_info() is False
        assert c.get_battery_charge() == 50
        assert c.get_max_battery_charge() == 100

    def test_charge_car(self):
        # arrange
        c = ElectricCar(False, battery_charge=50, max_battery_charge=100)

        # act
        c.charge(10)

        # assert
        self.assertEqual(c.get_battery_charge(), 60)

    def test_charge_powered_on_car(self):
        # arrange
        c = ElectricCar(True, battery_charge=50, max_battery_charge=100)

        # act
        # c.charge(10)

        # assert
        with self.assertRaises(ChargeWhileOnError):
            c.charge(10)

    def test_overcharge_car(self):
        # arrange
        c = ElectricCar(on=False, battery_charge=50, max_battery_charge=100)

        # act + assert
        with self.assertRaises(OverchargeError):
            c.charge(100)

    def test_charger_mocking_car(self):
        # arrange
        ch = Charger(totalAh=100)
        ev = ElectricCar(False, 0, 100)

        # act

        ev.charge = MagicMock(return_value=None)

        # assert
        self.assertEqual(ev.charge(1000), None, 'Używamy metody za-mock-owanej, a nie tej zaimplementowanej')
        ch.charge(ev, 30)   # uruchomi metodę Charger.charge, ale ta metoda nie "uderzy" do manekina, czyli do ev.charge
        self.assertEqual(ch.totalAh, 70)    # pola klasy Charger są zmienione, mimo, że operacja wykonana na manekinie

    def test_charger_will_not_overcharge_car(self):
        # arrange
        ch = Charger(totalAh=100)
        ev = ElectricCar(False, 0, 100)

        # act

        ev.charge = MagicMock(return_value=None)

        # assert
        with self.assertRaises(OverchargeError):
            ch.charge(ev, 200)
