import unittest

from src import calculation


class TestCalculateListsMethod(unittest.TestCase):
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

    def test_operations_empty(self):
        self.assertIsNone(calculation.calculate_lists([1,2],[]),
            msg="Empty list returns None")
        self.assertIsNone(calculation.calculate_lists([], [self.list_plus]),
            msg="Empty list returns None")

    def test_operations_mismatch(self):
        self.assertIsNone(calculation.calculate_lists([1,2],[self.list_plus]),
            msg="Mismatched list lengths returns None")
        self.assertIsNone(calculation.calculate_lists([1], [self.list_plus, self.list_plus]),
            msg="Mismatched list lengths returns None")

    def test_default_minus(self):
        self.assertEqual([-1], calculation.calculate_lists([2], [self.list_minus]),
            msg="Minus 3 list returns start value - 3 = -2 for default")

    def test_default_plus(self):
        self.assertEqual([4], calculation.calculate_lists([1], [self.list_plus]),
            msg="Plus 3 list returns start value + 3 = 4 for default")

    def test_default_times(self):
        self.assertEqual([6], calculation.calculate_lists([2], [self.list_times]),
            msg="Times 3 list returns start value times 3 = 6 for start = 2")

    def test_default_divide(self):
        self.assertAlmostEqual([1.], calculation.calculate_lists([3], [self.list_divide]),
            msg="Divide by 3 list returns start value divided 3 = 1/3 for default")


    def test_4_operation_lists(self):
        input_list = [1, 2, 3, 4]
        self.assertAlmostEqual([14,4.4,6,12], calculation.calculate_lists(input_list,
            [self.list1, self.list2, self.list_plus, self.list_times]),
                msg="Failed to process list of operations correctly")
        self.assertEqual([1, 2, 3, 4], input_list, msg="Do not modify the input list!")


    def test_3_operation_lists(self):
        input_list = [-1,-3,-4]
        actual = calculation.calculate_lists(input_list,
            [self.list1, self.list_plus, self.list_times])
        print("actual = ")
        self.assertEqual([6, 0, -12], actual,
                msg="Failed to process list of operations correctly")
        self.assertEqual([-1, -3, -4], input_list, msg="Do not modify the input list!")


if __name__ == '__main__':
    unittest.main()
