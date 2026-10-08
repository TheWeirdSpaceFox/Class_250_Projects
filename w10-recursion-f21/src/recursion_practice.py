def max_list_recursive(lst):
    """
    recursive method to find maximum in a list
    :param: lst - list with > operator defined
    :return: max value
    """
    #base

    if len(lst) == 0:
        return None
    elif len(lst) == 1:
        return lst[0]
    #recursive
    else:
        first = lst[0]
        rest_of_list = lst[1:]
        max_rest_of_list = max_list_recursive(rest_of_list)
        if first > max_rest_of_list:
            return first
        else:
            return max_rest_of_list



def sum_list_recursive(lst):
    """
    recursive method to find sum of a list
    :param lst:
    :return: sum of list, 0 if empty
    """

    if len(lst) == 0:
        return 0
    else:
        return lst[0] + sum_list_recursive(lst[1:])


def calc_seq(index):
    """
    Write a function `calc_seq` that returns the value of a sequence at a
    given index. The sequence is defined as the prior element minus the
    second and third prior elements .

    The 0th element returns 0, element 1 returns 1, and element 2 returns 2.
    The calculation for element 3 returns 1 (i.e. 2-1-0=1)

    The first seven elements are:

    element: 0 1 2 3  4  5  6 7 ...
    value  : 0 1 2 1 -2 -5 -4 3 ...

    :param index:
    :return:
    """
    if index < 0:
        raise IndexError("must be greater then 0")
    if index == 0:
        return 0
    elif index == 1:
        return 1
    elif index == 2:
        return 2
    else:
        return calc_seq(index-1) - calc_seq(index-2) - calc_seq(index-3)