import unittest
from src1 import program1
from given.car import Car
import os


class TestProgram1(unittest.TestCase):

    def setUp(self):
        # self.file_path = opj("data", ".csv")
        # with open(self.file_path, "rt") as fin:
        #     reader = c(fin, delimiter=",", lineterminator="\n")
        #     self.data = []
        #     for line in reader:
        #         self.data.append((int(line[0]), line[1], float(line[2]), int(line[3])))
        self.__delta = 0.000001
        self.data1 = ([1.0, 3.0, 5.0], [3.0, 6.0, 8.0], [5, 7, 12], [1,2,3], ['x', 'y', 'z', "n"])
        self.fpath = os.path.join("data", "data.txt")

    def test_load_text_tuple(self):
        data = program1.load_text(self.fpath)
        self.assertIsInstance(data, tuple)

    def test_load_text_tuple_lists(self):
        data = program1.load_text(self.fpath)
        self.assertIsInstance(data, tuple)
        for my_list in data:
            self.assertIsInstance(my_list, list)

    def test_load_text_exact(self):
        data = program1.load_text(self.fpath)
        x = data[0]
        y = data[1]
        z = data[2]
        n = data[3]
        for i in range(len(data[0])):
            self.assertAlmostEquals(x[i], self.data1[0][i], delta=self.__delta, msg=f"{x[i]} != {self.data1[0][i]}")
            self.assertAlmostEquals(y[i], self.data1[1][i], delta=self.__delta, msg=f"{x[i]} != {self.data1[1][i]}")
            self.assertAlmostEquals(z[i], self.data1[2][i], delta=self.__delta, msg=f"{x[i]} != {self.data1[2][i]}")
            self.assertAlmostEquals(n[i], self.data1[3][i], delta=self.__delta, msg=f"{x[i]} != {self.data1[3][i]}")
            self.assertIs(type(x[i]), float)
            self.assertIs(type(y[i]), float)
            self.assertIs(type(z[i]), int)
            self.assertIs(type(n[i]), int)


    def test_load_text_and_colnames_exact(self):
        data = program1.load_text(self.fpath)
        x = data[0]
        y = data[1]
        z = data[2]
        n = data[3]
        col_names = data[4]
        for i in range(len(data[0])):
            self.assertAlmostEquals(x[i], self.data1[0][i], delta=self.__delta, msg=f"{x[i]} != {self.data1[0][i]}")
            self.assertAlmostEquals(y[i], self.data1[1][i], delta=self.__delta, msg=f"{x[i]} != {self.data1[1][i]}")
            self.assertAlmostEquals(z[i], self.data1[2][i], delta=self.__delta, msg=f"{x[i]} != {self.data1[2][i]}")
            self.assertAlmostEquals(n[i], self.data1[3][i], delta=self.__delta, msg=f"{x[i]} != {self.data1[3][i]}")
            self.assertIs(type(x[i]), float)
            self.assertIs(type(y[i]), float)
            self.assertIs(type(z[i]), int)
            self.assertIs(type(n[i]), int)
            self.assertEquals(col_names[i], self.data1[4][i],  msg=f"{col_names[i]} != {self.data1[4][i]}")

    def test_write_data_exists(self):
        fpath = os.path.join("data", "test.txt")
        if os.path.exists(fpath):
            os.remove(fpath)
        cars = [Car("Ford", "Focus", 2017, "Grey"), Car("Ford", "Explorer", 2019, "Red"), Car("Ford", "F-150", 2015, "White"), Car("Ford", "Explorer", 2019, "Red")]
        program1.write_text_file(fpath, cars)
        self.assertTrue(os.path.exists(self.fpath), msg="File from write_data does not exist")
        os.remove(fpath)

    def test_write_data_almost(self):
        fpath = os.path.join("data", "test.txt")
        if os.path.exists(fpath):
            os.remove(fpath)
        cars = [Car("Ford", "Focus", 2017, "Grey"), Car("Ford", "Explorer", 2019, "Red"), Car("Ford", "F-150", 2015, "White"), Car("Ford", "Exploder", 2019, "Red")]
        program1.write_text_file(fpath, cars)
        self.assertTrue(os.path.exists(self.fpath), msg="File from write_data does not exist")
        for i, line in enumerate(open(fpath).readlines()):
            self.assertIn(cars[i].color, line)
            self.assertIn(cars[i].make, line)
            self.assertIn(cars[i].model, line)
            self.assertIn(str(cars[i].year), line)
        os.remove(fpath)

    def test_write_data_exact(self):
        fpath = os.path.join("data", "test.txt")
        if os.path.exists(fpath):
            os.remove(fpath)
        cars = [Car("Ford", "Focus", 2017, "Grey"), Car("Ford", "Explorer", 2019, "Red"), Car("Ford", "F-150", 2015, "White"), Car("Ford", "Exploder", 2019, "Red")]
        program1.write_text_file(fpath, cars)
        self.assertTrue(os.path.exists(self.fpath), msg="File from write_data does not exist")
        for i, line in enumerate(open(fpath).readlines()):
            self.assertIn(f"{cars[i].make}:{cars[i].model}:{cars[i].year}:{cars[i].color}", line)
        os.remove(fpath)


if __name__ == '__main__':
    unittest.main()
