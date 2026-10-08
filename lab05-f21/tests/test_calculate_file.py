import unittest

from src import calculation


class TestCalculateFileMethod(unittest.TestCase):
    """
        Test Class for calculation.py
    """

    def test_file_reading(self):
        self.assertAlmostEqual([20., 4.0, 4.0, 100.0], calculation.calculate_file('data/calculate.csv'),
                msg="Failed to process list of operations correctly")

        self.assertAlmostEqual([10., 6.0, 3.0, 5.0], calculation.calculate_file('data/calculate2.csv'),
                msg="Failed to process list of operations correctly")


if __name__ == '__main__':
    unittest.main()
