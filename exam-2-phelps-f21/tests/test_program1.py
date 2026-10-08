import unittest
import os
from src import program1
import numpy as np


class TestProgram1(unittest.TestCase):

    def setUp(self):
        self.poly1 = np.array([1.00000000e+00, 8.73664453e+03, 2.01755100e+06, 5.07779773e+07, 5.04030201e+08])
        self.poly2 = np.array([8.97932922e-09, 7.84492075e-05, 1.81162546e-02, 4.55952175e-01, 4.52585311e+00])

        self.poly3 = np.array([1.0000000e+00, 1.3068750e+02, 1.9260000e+03, 9.6056875e+03, 3.0201000e+04])
        self.poly4 = np.array([1.19433289e-04, 1.56084380e-02, 2.30028515e-01, 1.14723885e+00, 3.60700476e+00])
        self.short_x = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
        self.long_x = np.array([1.        , 1.21052632, 1.42105263, 1.63157895, 1.84210526,
        2.05263158, 2.26315789, 2.47368421, 2.68421053, 2.89473684,
        3.10526316, 3.31578947, 3.52631579, 3.73684211, 3.94736842,
        4.15789474, 4.36842105, 4.57894737, 4.78947368, 5.        ])


    def test_write_file_writes_file(self):
        file_path = os.path.join("data", "test_fall2021.txt")
        program1.write_file(file_path)
        self.assertTrue(os.path.exists(file_path), msg="Test File not written by write_file!")
        os.remove(file_path)

    def test_write_file_exact(self):
        file_path = os.path.join("data", "test_fall2020_2.txt")
        program1.write_file(file_path)
        with open(file_path) as file:
            self.assertEqual(file.read(), "Happy 60th Anniversary, CNU!\n",
                             msg="Test File does not contain the exact solution to write_file!")
        os.remove(file_path)

    def test_write_file_almost(self):
        file_path = os.path.join("data", "test_fall2020_2.txt")
        program1.write_file(file_path)
        with open(file_path) as file:
            self.assertEqual(file.read().lower().strip(), "happy 60th anniversary, cnu!",
                             msg="Check write_file capitalization, punctuation, or newline")
        os.remove(file_path)

    def test_plancks_law_data_tuple(self):
        test_file = os.path.join("data", "radiation.txt")
        self.assertEqual(type(program1.plancks_law_data(test_file)), tuple, msg="Did not return a tuple")

    def test_plancks_law_data_1(self):
        test_file = os.path.join("data", "radiation.txt")
        import numpy as np
        vals = [[float(j) for j in i.strip().split("~")] for i in open(test_file).readlines()]
        vals = np.array(vals)
        results = program1.plancks_law_data(test_file)
        results = np.column_stack((np.array(results[0]), np.array(results[1]), np.array(results[2]), np.array(results[3]), np.array(results[4])))
        np.testing.assert_almost_equal(vals, results, decimal=2)

    def test_plancks_law_data_2(self):
        test_file = os.path.join("data", "write_text_test.txt")
        import numpy as np
        vals = np.random.rand(100, 5)*100
        np.savetxt(test_file, vals, delimiter="~", newline='\n')
        results = program1.plancks_law_data(test_file)
        results = np.column_stack((np.array(results[0]), np.array(results[1]), np.array(results[2]), np.array(results[3]), np.array(results[4])))
        np.testing.assert_almost_equal(vals, results, decimal=2)
        os.remove(test_file)

    def test_get_x_list_or_array(self):
        x_data = program1.get_x_data(0.0, 5.0, 6)
        list_or_array = False
        if type(x_data) == list or type(x_data) == np.ndarray:
            list_or_array = True
        self.assertTrue(list_or_array, msg="Must return a list or numpy ndarray")

    def test_get_x(self):
        x_data = np.array(program1.get_x_data(0.0, 5.0, 6))
        self.assertEquals(len(x_data), 6, msg="Incorrect number of elements in your array or list")
        np.testing.assert_array_almost_equal(x_data, self.short_x)

    def test_get_x_exact(self):
        x_data = np.array(program1.get_x_data(1.0, 5.0, 20))
        np.testing.assert_array_almost_equal(x_data, self.long_x)
        x_data2 = np.array(program1.get_x_data(0.0, 5.0, 6))
        np.testing.assert_array_almost_equal(x_data2, self.short_x)

    def test_polynomial_tuple(self):
        coef = [1, 2, 3, 4, 5]
        x = np.linspace(0, 10, num=5)
        vals = program1.numpy_polynomial(x, coef)
        self.assertEqual(type(vals), tuple, msg="Did not return a tuple")

    def test_polynomial(self):
        coef = [1, 2, 3, 4, 5]
        x = np.linspace(0,10,num=5)
        vals = program1.numpy_polynomial(x, coef)
        np.testing.assert_array_almost_equal(vals[0], self.poly1, decimal=1)

    def test_polynomial_normalized(self):
        coef = [1, 2, 3, 4, 5]
        x = np.linspace(0,10,5)
        vals = program1.numpy_polynomial(x, coef)
        np.testing.assert_array_almost_equal(vals[1], self.poly2, decimal=3)

    def test_polynomial_2(self):
        coef = [1, 2, 3]
        x = np.linspace(0, 10, num=5)
        vals = program1.numpy_polynomial(x, coef)
        np.testing.assert_array_almost_equal(vals[0], self.poly3, decimal=3)

    def test_polynomial_normalized_2(self):
        coef = [1, 2, 3]
        x = np.linspace(0, 10, 5)
        vals = program1.numpy_polynomial(x, coef)
        np.testing.assert_array_almost_equal(vals[1], self.poly4, decimal=3)


if __name__ == '__main__':
    unittest.main()
