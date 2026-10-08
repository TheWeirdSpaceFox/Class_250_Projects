import unittest

from src4 import program4
import numpy as np
import os


class TestProgram4(unittest.TestCase):

    def setUp(self):
        self.short_y = np.array([ 0., -0.32996548,  0.33585379, -0.22045965,  0.1008401,  -0.02153704])
        self.short_x = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
        self.short_amp = 1.0
        self.short_freq = 10.0
        self.decay = .5
        self.full_path_test = os.path.join("data", "program4_plot.png")


    def test_get_x(self):
        x_data = program4.gen_linearly_spaced_values(0.0, 5.0, 6)
        np.testing.assert_array_almost_equal(x_data, self.short_x, err_msg="get_x_data does not return proper numpy array")

    def test_get_y(self):
        y_data = program4.get_y_data(self.short_x, self.short_amp, self.short_freq, self.decay)
        np.testing.assert_array_almost_equal(y_data, self.short_y, err_msg="get_y_data does not return proper numpy array")

    def test_gen_plot(self):
        program4.generate_plot(self.full_path_test,
                               self.short_amp, self.short_freq, self.decay,
                               0.0, 6.0, 250)
        self.assertTrue(os.path.exists(self.full_path_test), msg="Plot file does not exist")


if __name__ == '__main__':
    unittest.main()
