"""
We will practice with a few list methods

Many of these only require one line of code for base case,
plus protection from None

@author Amanda Sanders
@version 9/1/21

"""
# pylint: disable-msg=C0103


def first_two(input):
    list = []
    list.append(input[0])
    list.append(input[1])
    """
    Get the first two items in a list
    @param input a valid list with at least 2 items
    @return list of 2 items
    """
    # You only need 1 line of code to solve this
    return list

def exclude_first_and_last(input):
    """
    Get all of the list excluding the first and last item
    @param input  a valid list of at least 3 items
    @return list of items, excluding the first and last item
    """
    return input[1:-1]


def every_other(input):
    """
    Given ['A','b', 'c','d'] return ['A','c']

    @param input  a list of at least 3 items
    @return list containing every other item starting with first
    """
    i = 0
    list=[]
    while i <= len(input)-1:
        if i % 2 == 0:
            list.append(input[i])
        i += 1
    return list

if __name__ == '__main__':
    # Here is simple test - no need to modify below
    input0 = ['A', 'B', 'C', 'd', 'e', 'f']
    input1 = [1, 2, 3.14, 4, 5, 6]

    print("first_two result = ", first_two(input0))

    print("exclude_first_and_last result = ", exclude_first_and_last(input0))

    print("every_other result = ", every_other(input1))
