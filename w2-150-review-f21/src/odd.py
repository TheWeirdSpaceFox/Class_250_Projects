"""
Script to test for odd numbers

We may be able to improve

WARNING: This works in Python, but in Java you'll learn
some subtle differences

@author Amanda Sanders
@version 9/7/21

"""

def is_odd(value):
    """
    Tests if the value is odd
    @return Boolean
    """
    if type(value) != int:
        return False

    return value %2 == 1

# if __name__ == '__main__':
#     print(is_odd(41))