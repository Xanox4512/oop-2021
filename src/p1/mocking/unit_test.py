import math
import unittest
from unittest.mock import MagicMock, Mock, call


class Calculator:
    def add(self, a, b):
        return a + b


class TestSum(unittest.TestCase):

    def test_sum(self):
        c = Calculator()
        c.add = MagicMock(return_value=5)
        self.assertEqual(c.add(2, 2), 5, 'Używamy wartości zwracanych z mock-a, a nie klasy')

    def test_called(self):
        m = Mock()
        m.kadabra(15)
        m.kadabra(18)
        # m.kadabra()

        # m.kadabra.assert_called_once()
        print(m.kadabra.mock_calls)
        m.kadabra.assert_called()
        m.kadabra.assert_has_calls(calls=[call.kadabra(15), call.kadabra(18)])


if __name__ == '__main__':
    unittest.main()
