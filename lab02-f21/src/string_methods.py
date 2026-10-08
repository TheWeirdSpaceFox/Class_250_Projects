"""
We will practice with a few string string_methods

You may assume that the input is a valid string, therefore
the solutions only require one line of code at the return statement

If you take more than 1-line of code, review your string methods:
https://docs.python.org/3/library/stdtypes.html#str
https://docs.python.org/3/library/stdtypes.html#str.format


@author Amanda Sanders
@version 9/1/21

"""


# pylint: disable-msg=C0103

def lower(input_str):
    # input_str = input_str.upper()
    # i = 0
    # string = ''
    # while i <= len(input_str)-1:
    #     if i % 2 != 0:
    #         string += input_str[i].lower()
    #     else:
    #         string += input_str[i]
    #     i += 1
    input_str = input_str.upper()
    i = 0
    string = ''
    while i <= len(input_str)-1:
        if i % 2 == 0:
            string += input_str[i].lower()
        else:
            string += input_str[i]
        i += 1
    """
    @param input_str  a valid reference to a str instance
    @return String with every other letter lowercase
    starting with the first letter
    """
    return string


def upper(input_str):
    input_str = input_str.upper()
    """
    @param input_str  a valid reference to a str instance
    @return String with all upper case string
    """
    return input_str


def first_three(input_str):
    """
    Get the first three characters of a string of at least 3 characters
    @param input_str a valid reference to a str instance
    @return String of three letters or None
    """
    string = ''
    string += input_str[0:3]
    return string


def last_four(input_str):
    """
    Get the last four characters of a string
    @param input_str a valid reference to a str instance of at least 4 characters
    @return String of four letters
    """
    string = ''
    string += input_str[-4]
    string += input_str[-3]
    string += input_str[-2]
    string += input_str[-1]
    return string


def every_third(input_str):
    """
    Given  'abcdefghijk'
    return 'cfi'
    @param input_str a valid reference to a str instance of at least 6 characters
    @return String containing every three letters of input starting at 3rd
    """
    i = 2
    string = ''
    while i <= len(input_str)-1:
        string += input_str[i]
        i += 3
    return string



def format_name(first, last):
    """
    Given first and last names, return a single "Last, First" with proper
    capitalization

    Do this in one line of code!

    @param first - a valid str type first name with undetermined capitalization
    @param last - a valid str type first name with undetermined capitalization

    @return String formatted as "Last, First" with Initial-capital style
    """

    return "{}, {}".format(last.capitalize(), first.capitalize())



if __name__ == '__main__':
    # Here is simple test - no need to modify below
    print("  lower('abcdef') = ", lower('abcdef'))
    print("  upper('abcDef') = ", upper('abcDef'))
    print("  first_three('abcdefghijk') = ", first_three('abcdefghijk'))
    print("  last_four('abcdefghijk') = ", last_four('abcdefghijk'))
    print("  every_third('abcdefghijk') = ", every_third('abcdefghijk'))
    print("  format_name:", format_name("paul", "trible"))
