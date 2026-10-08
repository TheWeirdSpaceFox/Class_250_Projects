import unittest
from src import homework_weather_data
import numpy as np
import os
import glob

class TestHomeworkWeatherData(unittest.TestCase):

    def setUp(self):
        self.headerfile = os.path.join("data", "headers.csv")
        self.datafile = os.path.join("data", "weather_09_06.csv")
        self.smalldata = homework_weather_data.read_all_data_list(self.datafile)
        self.headers = ['date_time', 'temperature', 'heat_index', 'humidity', 'barometric_pressure', 'wind_speed']


    def test_headers(self):
        self.assertListEqual(homework_weather_data.read_headers(self.headerfile), self.headers, msg="The list of column headers do not match")

    def test_headers_size(self):
        self.assertEqual(len(homework_weather_data.read_headers(self.headerfile)), 6, msg="Incorrect length of header list, check to see that you are splitting by commas")

    def test_np_datetime64(self):
        self.assertEqual(type(self.smalldata[0][0]), np.datetime64, msg="Use np.datetime64 as the datatype to get a datetime axis")

    def test_datatypes_not_strings(self):
        self.assertNotEqual(type(self.smalldata[1][0]), str, msg="Datatype cannot be a string, use float")
        self.assertNotEqual(type(self.smalldata[2][0]), str, msg="Datatype cannot be a string, use float")
        self.assertNotEqual(type(self.smalldata[3][0]), str, msg="Datatype cannot be a string, use float")
        self.assertNotEqual(type(self.smalldata[4][0]), str, msg="Datatype cannot be a string, use float")
        self.assertNotEqual(type(self.smalldata[5][0]), str, msg="Datatype cannot be a string, use float")

    def test_ncolumns(self):
        self.assertEqual(len(self.smalldata), 6, msg="You should have 6 columns of data, you are not reading all of the columns")

    def test_nrows(self):
        self.assertEqual(len(self.smalldata[0]), 142, msg="You are not reading the entire file, number of rows is incorrect")

    def test_minmax_temp_09_06_exact(self):
        solution = (64.5, np.datetime64('2019-09-06T23:50'), 75.7, np.datetime64('2019-09-06T03:00'))
        self.assertEqual(homework_weather_data.get_time_max_min(self.smalldata[0], self.smalldata[1]), solution)

    def test_minmax_temp_09_06_length(self):
        self.assertEqual(len(homework_weather_data.get_time_max_min(self.smalldata[0], self.smalldata[1])), 4, msg="You need to return a tuple of with 4 elements")

    def test_minmax_temp_09_06_tuple(self):
        self.assertEqual(type(homework_weather_data.get_time_max_min(self.smalldata[0], self.smalldata[1])), tuple, msg="You need to return a tuple!")

    # def test_figures_exist(self):
    #     self.assertGreater(len(glob.glob(os.path.join("fig","*"))),1,msg="Your fig directory only contains the sample figure. You need to save the figures here and upload them to scholar")


if __name__ == '__main__':
    unittest.main()
