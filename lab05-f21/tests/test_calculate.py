import unittest

from src import calculation


class TestCalculateMethod(unittest.TestCase):
    """
        Test Class for list_methods.py
    """

    def setUp(self):

        self.list1 = [('+', 3), ('*',4), ('-',2)]
        self.list2 = [('+', 3), ('*',4), ('+', 2), ('/',5)]
        self.list_minus = [('-', 3)]
        self.list_plus = [('+', 3)]
        self.list_times = [('*', 3)]
        self.list_divide = [('/', 3)]

    def test_default_start_empty(self):
        self.assertEqual(1, calculation.calculate([]),
            msg="Empty list returns start value")

    def test_default_minus(self):
        self.assertEqual(-2, calculation.calculate(self.list_minus),
            msg="Minus 3 list returns start value - 3 = -2 for default")

    def test_default_plus(self):
        self.assertEqual(4, calculation.calculate(self.list_plus),
            msg="Plus 3 list returns start value + 3 = 4 for default")

    def test_default_times(self):
        self.assertEqual(3, calculation.calculate(self.list_times),
            msg="Times 3 list returns start value times 3 = 3 for default")

    def test_default_divide(self):
        self.assertAlmostEqual(1./3, calculation.calculate(self.list_divide),
            msg="Divide by 3 list returns start value divided 3 = 1/3 for default")

    def test_start_4_minus(self):
        self.assertEqual(1, calculation.calculate(self.list_minus, 4),
            msg="Minus 3 list returns start value - 3 = 1 for start=4")

    def test_start_4_plus(self):
        self.assertEqual(7, calculation.calculate(self.list_plus, 4),
            msg="Plus 3 list returns start value + 3 = 7 for start=4")

    def test_start_4_times(self):
        self.assertEqual(12, calculation.calculate(self.list_times, 4),
            msg="Times 3 list returns start value times 3 = 12 for start=4")

    def test_start_4_divide(self):
        self.assertAlmostEqual(4./3, calculation.calculate(self.list_divide, 4),
            msg="Divide by 3 list returns start value divided 3 = 4/3 for start=4")

    def test_default_start(self):
        self.assertEqual(14, calculation.calculate(self.list1),
            msg="Using default value of 1 for start, should be 14 for "+str(self.list1))
        self.assertAlmostEqual(18/5, calculation.calculate(self.list2),
            msg="Using default value of 1 for start, should be 18/5 for "+str(self.list2))

    def test_4_start(self):
        self.assertEqual(26, calculation.calculate(self.list1,4),
            msg="Using value of 4 for start, should be 26 for "+str(self.list1))
        self.assertEqual(6, calculation.calculate(self.list2, 4),
            msg="Using value of 4 for start, should be 6 for "+str(self.list2))

    def test_N3_start(self):
        self.assertEqual(-2, calculation.calculate(self.list1,-3),
            msg="Using value of 4 for start, should be -2 for "+str(self.list1))
        self.assertAlmostEqual(2/5, calculation.calculate(self.list2, -3),
            msg="Using value of 4 for start, should be 2/5 for "+str(self.list2))

    def test_empty_operations(self):
        self.assertEqual(1, calculation.calculate([]),
            msg="Using value of 1 for start, empty list returns 1")
        self.assertEqual(5, calculation.calculate([], 5),
            msg="Using value of 5 for start, empty list returns 5")



if __name__ == '__main__':
    unittest.main()
