import unittest
from src3.program3 import Program3


class TestProgram3(unittest.TestCase):
    def setUp(self):
        self.__delta = 0.000001
        self.exp = [6, 7, 8, 17, 35, 79, 176]
        self.expc = [1, 1, 1, 4, 7, 13, 25]

        self.exp2 = [6, 7, 8, 17, 35, 79, 176, 396, 889, 1998, 4489, 10087, 22665, 50928, 114434, 257131, 577768, 1298233, 2917103, 6554671]
        self.exp2c = [1, 1, 1, 4, 7, 13, 25, 46, 85, 157, 289, 532, 979, 1801, 3313, 6094, 11209, 20617, 37921, 69748]

    def test_start_cases1(self):
        for i in range(2):
            p = Program3()
            v = p.pattern(i)
            self.assertEqual(v, self.exp[i], msg='base case failed')
            self.assertEqual(p.counter2, self.expc[i], msg='invalid recursion counter for base case (should be 1)')

    def test_n_2(self):
        n = 2
        p = Program3()
        v = p.pattern(n)
        self.assertEqual(v, self.exp[n], msg='f({:d}) failed'.format(n))
        # self.assertEqual(p.counter2, self.expc[n], msg='Check to make sure you do not have extra base cases')

    def test_recursive_sequence_exact1(self):

        for i in range(len(self.exp)):
            p = Program3()
            v = p.pattern(i)
            self.assertEqual(v, self.exp[i], msg='incorrect recursion_sequence value')
            self.assertEqual(p.counter2, self.expc[i], msg='invalid recursion counter, make sure you have the minimum number of base cases')

    def test_recursive_sequence_exact2(self):

        for i in range(len(self.exp2)):
            p = Program3()
            v = p.pattern(i)
            self.assertEqual(v, self.exp2[i], msg='incorrect recursion_sequence value')
            self.assertEqual(p.counter2, self.exp2c[i], msg='invalid recursion counter, make sure you have the minimum number of base cases')

    def test_n_neg(self):
        n = -3
        try:
            p = Program3()
            v = p.pattern(n)
            self.fail(msg=" raise ValueError for negative index")
        except ValueError as e:
            pass
        except Exception as e:
            self.fail(msg=" raise ValueError for negative index")

    def test_vowels_1(self):
        p = Program3()
        n_vowels = p.remove_vowels("e")
        self.assertEqual(n_vowels, "", msg='incorrect string, you must remove vowels')

    def test_vowels_2(self):
        p = Program3()
        n_vowels = p.remove_vowels("pineapple")
        self.assertEqual(n_vowels, "pnppl" , msg='incorrect number of vowels')
        self.assertEqual(p.counter1, 10, msg='incorrect number recursive calls')

    def test_vowels_exact(self):
        p = Program3()
        n_vowels = p.remove_vowels("pineapple")
        self.assertEqual(n_vowels, "pnppl", msg='incorrect number of vowels')
        self.assertEqual(p.counter1, 10, msg='incorrect number recursive calls')
        n_vowels = p.remove_vowels("pineapple")
        self.assertEqual(p.counter1, 20, msg='incorrect number recursive calls')




if __name__ == '__main__':
    unittest.main()
