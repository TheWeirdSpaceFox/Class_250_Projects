import unittest
import os
from src2 import program2
import math
import struct
import numpy as np


class TestProgram2(unittest.TestCase):

    def test_my_error(self):
        from src2.my_arithmetic_error import MyArithmeticError
        se = MyArithmeticError("test msg")
        self.assertIsInstance(se, Exception, msg="SmallOverflowError must be Exception")

    def test_my_error_msg(self):
        from src2.my_arithmetic_error import MyArithmeticError
        se = MyArithmeticError("test msg")
        self.assertIsInstance(se, Exception, msg="SmallOverflowError must be Exception")
        self.assertEqual("test msg", str(se), msg="did not handle message properly")

    def test_raise_exception_1(self):
        try:
            val = program2.val_check(1.0)
            self.assertIsNotNone(val, msg="must return value for valid data")
        except Exception:
            self.fail(msg="Don't raise exception for valid data")

        try:
            val = program2.val_check(3.5)
            self.fail(msg="Must raise exception for invalid data")
        except Exception:
            pass

    def test_raise_exception_2(self):
        try:
            val = program2.val_check(1.0)
            self.assertIsNotNone(val, msg="must return value for valid data")
        except Exception:
            self.fail(msg="Don't raise exception for valid data")

        try:
            val = program2.val_check("Ima string!")
            self.fail(msg="Must raise exception for invalid data")
        except ArithmeticError as e:
            pass
        except Exception:
            self.fail(msg="Must raise ArithmeticError for non-numeric values")

    def test_raise_exception_exact(self):
        try:
            val = program2.val_check(1.0)
            self.assertIsNotNone(val, msg="must return value for valid data")
        except Exception:
            self.fail(msg="Don't raise exception for valid data")

        try:
            val = program2.val_check("Ima string!")
            self.fail(msg="Must raise exception for invalid data")
        except ArithmeticError as e:
            pass
        except Exception:
            self.fail(msg="Must raise ArithmeticError for non-numeric values")

        try:
            val = program2.val_check(20000000.0)
            self.fail(msg="Must raise exception for invalid data")
        except ValueError as e:
            self.fail(msg="Must raise other than ValueError for val < 0")
        except Exception as e:
            from src2.my_arithmetic_error import MyArithmeticError
            if not isinstance(e, MyArithmeticError):
                self.fail(msg="Must raise MyArithmeticError for val > 12.0")


    def test_call_function_1(self):
        expected = ("Number is too large!", 12.1)
        self.assertEquals(expected[1], program2.call_val_check(12.1)[1])
        self.assertEquals(expected[0], program2.call_val_check(12.1)[0])


    def test_call_function_2(self):
        self.assertEqual(str(5.0), program2.call_val_check(5.0))

    def test_call_function_3(self):
        self.assertEqual("Must be a valid float", program2.call_val_check("Turkey day!"))

    def test_call_function_4(self):
        self.assertEqual("Must be a valid float", program2.call_val_check(15))

    def test_open_file(self):
        if os.path.isfile("tmp.txt"):
            os.remove("tmp.txt")
        self.assertEqual(-1, program2.read_file("tmp.txt"))

    def test_open_file2(self):
        import io
        txt = open("tmp2.txt","wt")
        txt.close()
        self.assertIsInstance(program2.read_file("tmp2.txt"), io.TextIOWrapper)
        os.remove("tmp2.txt")

if __name__ == '__main__':
    unittest.main()
