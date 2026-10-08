import unittest
import os

from src import homework


class TestHomework(unittest.TestCase):

    def test_homework_numbers(self):
        self.assertTrue("1" in homework.cnu_captains())
        self.assertTrue("11" in homework.cnu_captains())
        self.assertTrue("99" in homework.cnu_captains())

    def test_homework_cnu(self):
        self.assertTrue("cnu" in homework.cnu_captains().lower())

    def test_homework_cnu_exact(self):
        self.assertTrue("CNU" in homework.cnu_captains())

    def test_homework_captains(self):
        self.assertTrue("captains" in homework.cnu_captains().lower())

    def test_homework_captains_exact(self):
        self.assertTrue("CAPTAINS" in homework.cnu_captains())

    def test_homework_lines(self):
        lines = homework.cnu_captains().split(os.linesep)
        self.assertEquals(101, len(lines), msg="Incorrect number of lines - between 1 and 100 inclusive!")

    def test_homework_exact(self):

        # Do your solution with a loop.  DO NOT copy this line!
        test_string = "1" + os.linesep + "CNU" + os.linesep + "3" + os.linesep + "CNU" + os.linesep + "CAPTAINS" + os.linesep + "CNU" + os.linesep + "7" + os.linesep + "CNU" + os.linesep + "9" + os.linesep + "CNUCAPTAINS" + os.linesep + "11" + os.linesep + "CNU" + os.linesep + "13" + os.linesep + "CNU" + os.linesep + "CAPTAINS" + os.linesep + "CNU" + os.linesep + "17" + os.linesep + "CNU" + os.linesep + "19" + os.linesep + "CNUCAPTAINS" + os.linesep + "21" + os.linesep + "CNU" + os.linesep + "23" + os.linesep + "CNU" + os.linesep + "CAPTAINS" + os.linesep + "CNU" + os.linesep + "27" + os.linesep + "CNU" + os.linesep + "29" + os.linesep + "CNUCAPTAINS" + os.linesep + "31" + os.linesep + "CNU" + os.linesep + "33" + os.linesep + "CNU" + os.linesep + "CAPTAINS" + os.linesep + "CNU" + os.linesep + "37" + os.linesep + "CNU" + os.linesep + "39" + os.linesep + "CNUCAPTAINS" + os.linesep + "41" + os.linesep + "CNU" + os.linesep + "43" + os.linesep + "CNU" + os.linesep + "CAPTAINS" + os.linesep + "CNU" + os.linesep + "47" + os.linesep + "CNU" + os.linesep + "49" + os.linesep + "CNUCAPTAINS" + os.linesep + "51" + os.linesep + "CNU" + os.linesep + "53" + os.linesep + "CNU" + os.linesep + "CAPTAINS" + os.linesep + "CNU" + os.linesep + "57" + os.linesep + "CNU" + os.linesep + "59" + os.linesep + "CNUCAPTAINS" + os.linesep + "61" + os.linesep + "CNU" + os.linesep + "63" + os.linesep + "CNU" + os.linesep + "CAPTAINS" + os.linesep + "CNU" + os.linesep + "67" + os.linesep + "CNU" + os.linesep + "69" + os.linesep + "CNUCAPTAINS" + os.linesep + "71" + os.linesep + "CNU" + os.linesep + "73" + os.linesep + "CNU" + os.linesep + "CAPTAINS" + os.linesep + "CNU" + os.linesep + "77" + os.linesep + "CNU" + os.linesep + "79" + os.linesep + "CNUCAPTAINS" + os.linesep + "81" + os.linesep + "CNU" + os.linesep + "83" + os.linesep + "CNU" + os.linesep + "CAPTAINS" + os.linesep + "CNU" + os.linesep + "87" + os.linesep + "CNU" + os.linesep + "89" + os.linesep + "CNUCAPTAINS" + os.linesep + "91" + os.linesep + "CNU" + os.linesep + "93" + os.linesep + "CNU" + os.linesep + "CAPTAINS" + os.linesep + "CNU" + os.linesep + "97" + os.linesep + "CNU" + os.linesep + "99" + os.linesep + "CNUCAPTAINS"+ os.linesep

        self.assertEqual(test_string, homework.cnu_captains(), msg='String is not an exact match')


if __name__ == '__main__':
    unittest.main()
