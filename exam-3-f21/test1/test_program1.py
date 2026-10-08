import unittest
from src1 import program1
from src1.commercial_building import CommercialBuilding
from given.table import Table
from csv import reader as c
from os.path import join as opj


class TestProgram1(unittest.TestCase):
    def setUp(self):
        self.full_path = opj("data", "buildings.txt")
        with open(self.full_path, "rt") as fin:
            reader = c(fin, delimiter=",", lineterminator="\n")
            self.data = []
            for line in reader:
                if not "#" in line[0]:
                    self.data.append([line[0], line[1], int(line[2])])

    def test_create_table_instance(self):
        p1 = program1.create_table()
        self.assertIsNotNone(p1, msg="must create something")
        self.assertIsInstance(p1, Table, msg="must create instance of Table")

    def test_create__instance(self):
        p1 = program1.create_table()
        self.assertIsNotNone(p1, msg="must create something")
        self.assertIsInstance(p1, Table, msg="must create instance of Table")

    def test_read_buildings_list(self):
        data = program1.read_city_data(self.full_path)
        self.assertIsInstance(data, list, msg="must return a list")
        self.assertEqual(len(data), len(self.data), msg="must return a list")

    def test_read_buildings_1(self):
        data_test = program1.read_city_data(self.full_path)
        self.assertIsInstance(data_test, list, msg="must return a list")
        self.assertEqual(len(data_test), len(self.data), msg="must return a list")
        for i, dat in enumerate(data_test):
            self.assertTrue(isinstance(dat, CommercialBuilding))

    def test_read_buildings_2(self):
        data_test = program1.read_city_data(self.full_path)
        self.assertIsInstance(data_test, list, msg="must return a list")
        self.assertEqual(len(data_test), len(self.data), msg="must return a list")
        for i, dat in enumerate(data_test):
            self.assertIsInstance(dat, CommercialBuilding, msg="should be list of CommercialBuilding instances")
            self.assertEqual(dat.name, self.data[i][0],
                                   msg="Name ={} at i={} not equal {}".format(dat.name, i, self.data[i][0]))
            self.assertEqual(dat.country, self.data[i][1],
                                   msg="Country={} at i={} not equal {}".format(dat.country, i, self.data[i][1]))
            self.assertAlmostEqual(dat.floor_area, self.data[i][2],
                                   msg="Floor area={} at i={} not equal {}".format(dat.floor_area, i, self.data[i][2]))

    def test_equal_to(self):
        building1 = CommercialBuilding("Luter Hall", "United States", 135000)
        building2 = CommercialBuilding("Luter Hall", "United States", 135000)

        self.assertIsInstance(building1, CommercialBuilding, msg="must create instance of CommercialBuilding")
        self.assertEqual(building1, building2, msg="These two instances of CommercialBuilding must be equal. Compare the name, size, and location")

    def test_equal_to_2(self):
        building1 = CommercialBuilding("Luter Hall", "United States", 135000)
        building2 = CommercialBuilding("Luter Hall", "USA", 135000)

        self.assertIsInstance(building1, CommercialBuilding, msg="must create instance of CommercialBuilding")
        self.assertNotEqual(building1, building2, msg="These two instances of CommercialBuildings must not be equal. Compare the name, size, and location")

    def test_equal_to_3(self):
        building1 = CommercialBuilding("Luter Hall", "United States", 135000)
        building2 = CommercialBuilding("Luter Hall", "United States", 135)

        self.assertIsInstance(building1, CommercialBuilding, msg="must create instance of CommercialBuilding")
        self.assertNotEqual(building1, building2, msg="These two instances of CommercialBuilding must not be equal. Compare the name, size, and location")

    def test_building_add(self):
        building1 = CommercialBuilding("Luter Hall", "United States", 135000)
        building2 = CommercialBuilding("Luter Hall", "United States", 135000)
        expected = 270000
        self.assertIsInstance(building1, CommercialBuilding, msg="must create instance of Investment")
        self.assertEqual(building1+building2, expected, msg="The addition method should add together the square footage")

    def test_building_add_int(self):
        building1 = CommercialBuilding("Luter Hall", "United States", 135000)
        building2 = CommercialBuilding("Luter Hall", "United States", 135000)
        expected = 270000
        self.assertIsInstance(building1, CommercialBuilding, msg="must create instance of Investment")
        self.assertEqual(building1+building2, expected, msg="The addition method should add together the square footage")
        self.assertEqual(building1+100000, 235000, msg="The addition method should be able to add an integer to the square footage")

    def test_building_str(self):
        building1 = CommercialBuilding("Luter Hall", "United States", 135000)
        self.assertIsInstance(building1, CommercialBuilding, msg="must create instance of Investment")
        self.assertEqual(building1+"a string", 0, msg="The addition method should return 0 if passed a string")

    def test_building_less_than(self):
        building1 = CommercialBuilding("Luter Hall", "United States", 135000)
        building2 = CommercialBuilding("Ferguson Center", "United States", 249750)
        self.assertIsInstance(building1, CommercialBuilding, msg="must create instance of Account")
        self.assertLess(building1, building2, msg="building1 should be less than building2.")

    def test_building_less_than_2(self):
        building1 = CommercialBuilding("Luter Hall", "United States", 135000)
        building2 = CommercialBuilding("Ferguson Center", "United States", 249750)
        self.assertIsInstance(building1, CommercialBuilding, msg="must create instance of Account")
        self.assertLess(building1, building2, msg="building1 should be less than building2.")
        self.assertFalse(building2 < building1, msg="building1 should be less than building2.")

    def test_str_method(self):
        building1 = CommercialBuilding("Luter Hall", "United States", 135000)
        actual = str(building1)
        self.assertTrue(str(135000) in actual, msg="str must contain the square footage of the floor area")

    def test_str_method_almost(self):
        building1 = CommercialBuilding("Luter Hall", "United States", 135000)
        actual = str(building1).replace(" ","")
        expected = "Luter Hall (United States) floor area:135000 ft^2".replace(" ","")
        self.assertEqual(expected, actual, msg="If test_str_method_exact is failing but this one is not, check your spacing.")

    def test_str_method_exact(self):
        building1 = CommercialBuilding("Luter Hall", "United States", 135000)
        actual = str(building1)
        expected = "Luter Hall (United States) floor area:135000 ft^2"
        self.assertEqual(expected, actual)


    def test_str_method_office_building_almost(self):
        from src1.office_building import OfficeBuilding
        building1 = OfficeBuilding("Christopher Newport Hall", "United States", 81000, 4, 80)
        actual = str(building1).replace(" ", "")
        expected = "Christopher Newport Hall (United States) floor area:81000 ft^2 floors:4 height:80 ft".replace(" ","")
        self.assertEqual(expected, actual)

    def test_str_method_office_building_exact(self):
        from src1.office_building import OfficeBuilding
        building1 = OfficeBuilding("Christopher Newport Hall", "United States", 81000, 4, 80)
        actual = str(building1)
        expected = "Christopher Newport Hall (United States) floor area:81000 ft^2 floors:4 height:80 ft"
        self.assertEqual(expected, actual)


    def test_inheritance_office_building(self):
        from src1.office_building import OfficeBuilding
        building1 = OfficeBuilding("Christopher Newport Hall", "United States", 81000, 4, 80)
        self.assertIsInstance(building1, OfficeBuilding, msg="Must be an instance of OfficeBuilding")
        self.assertIsInstance(building1, CommercialBuilding, msg="CommonStock must inherit from Building")

    # def test_equal_to_common_stock(self):
    #     from src1.common_stock import CommonStock
    #     transaction1 = CommonStock(10757,"AAPL",3.00,117.61,2020)
    #     transaction2 = CommonStock(10757,"AAPL",3.00,117.61,2020)
    #
    #     self.assertIsInstance(transaction1, Investment, msg="must create instance of Investment")
    #     self.assertEqual(transaction1, transaction2,
    #                      msg="These two instances of CommonStock must be equal. Only use the transaction number for comparison")
    #
    def test_make_make_commercial_buildings(self):
        from src1.office_building import OfficeBuilding
        building_list = program1.create_buildings()
        self.assertIsNotNone(building_list, msg="must make a list of CommercialBuildings")
        self.assertIsInstance(building_list, list, msg="must make a list of CommercialBuildings")
        self.assertTrue(len(building_list) > 1, msg="must make a list of CommercialBuildings with some data")
        building_count = 0
        office_building_count = 0
        for building in building_list:
            self.assertIsInstance(building, CommercialBuilding, msg="must all be CommercialBuilding instances")
            if type(building) == CommercialBuilding:
                building_count += 1
            if isinstance(building, OfficeBuilding):
                office_building_count += 1

        self.assertEqual(2, building_count, msg="Must contain 2 CommercialBuilding instances, not including office building instances")

    def test_make_make_commercial_buildings_2(self):
        from src1.office_building import OfficeBuilding
        building_list = program1.create_buildings()
        self.assertIsNotNone(building_list, msg="must make a list of CommercialBuildings")
        self.assertIsInstance(building_list, list, msg="must make a list of CommercialBuildings")
        self.assertTrue(len(building_list) > 1, msg="must make a list of CommercialBuildings with some data")
        building_count = 0
        office_building_count = 0
        for building in building_list:
            self.assertIsInstance(building, CommercialBuilding, msg="must all be CommercialBuilding instances")
            if isinstance(building, CommercialBuilding):
                building_count += 1
            if isinstance(building, OfficeBuilding):
                office_building_count += 1

        self.assertEqual(3, building_count, msg="Must contain 3 instances of CommercialBuilding")

    def test_make_make_commercial_buildings_exact(self):
        from src1.office_building import OfficeBuilding
        building_list = program1.create_buildings()
        self.assertIsNotNone(building_list, msg="must make a list of CommercialBuildings")
        self.assertIsInstance(building_list, list, msg="must make a list of CommercialBuildings")
        self.assertTrue(len(building_list) > 1, msg="must make a list of CommercialBuildings with some data")
        building_count = 0
        office_building_count = 0
        for building in building_list:
            self.assertIsInstance(building, CommercialBuilding, msg="must all be CommercialBuilding instances")
            if isinstance(building, CommercialBuilding):
                building_count += 1
            if isinstance(building, OfficeBuilding):
                office_building_count += 1

        self.assertEqual(3, building_count, msg="Must contain 3 instances of CommercialBuilding")
        self.assertEqual(1, office_building_count, msg="Must contain 1 instance of office building")


if __name__ == '__main__':
    unittest.main()


