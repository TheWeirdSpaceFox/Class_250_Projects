"""
Program 2

Module defines the functions/methods as defined by docstrings below

@author Amanda Sanders
"""

from src2.my_arithmetic_error import MyArithmeticError
def read_file(file_path):
    """
    This function should open a text file specified by "file_path" in read mode. If you are successful in opening the
    file you should return the opened file handle. If you are not able to open the file you should return -1.

    :param file_path:
    :return: as described above
    """
    try:
        with open(file_path, "rt") as file:
            return file
    except FileNotFoundError:
        return -1


def val_check(value):

    """
    This function checks if the "value" passed in will cause a "my_arithmetic_error"

    You must create a new class c in the file my_arithmetic_error in the src2 directory.
    This class should inherit from ArithmeticError.

       -This new class should be raised if "value" is greater than 12. The error message should be 'Number is too large!'
       -If the value is not a floating point number then you should raise an ArithmeticError. The error message should be "Must be a valid float"
       -return value

    :param value:
    :return: value
    """
    if type(value) is not float:
        raise ArithmeticError("Must be a valid float")
    elif value > 12:
        raise MyArithmeticError('Number is too large!')

    return value


def call_val_check(value):
    """
    This method calls val_check from above which checks the "value" passed in.
        If value is not a a valid number, return the message "Must be a valid float"
        If value is greater than 12, return ("Number is too large!", value)

    Otherwise, return the string corresponding to value

    :param func:
    :return: As described above
    """


    ## You may modify the below line with a single line of code (this added to preserve indenting)
    if True:  # You may this single line as needed as long as check_values is always called!
        ### vvvvvvv DO NOT MODIFY THIS BLOCK OF CODE vvvvvvvvvvvv
        val_check(value)
        ### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        # You may add whatever code is necessary down here, but the above value_check function must be called first!
    return "{}".format(value)