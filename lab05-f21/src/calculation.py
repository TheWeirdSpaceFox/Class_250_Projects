"""
Calculate output given starting point an list of (operation, operand) tuples

I've given you some rough comments.  You need to convert to valid doc-strings
and method headers for the 3 methods you need to write.

See README for more information

@author <Your Name Here>
@version <Date Here>

"""
# pylint: disable=C0103

#calculate
"""
Calculate output given start and list of operations.
:param operations: List of operations as tuples of (operation, operand) (e.g. ('+',3) )
:param start: initial starting value with default value of 1
:return: solution as number
"""

#calculate_lists
"""
Calculate list of values given starting value and operations
:param start_list: list of starting values
:param operations_list: list of list of operations
:return: list of calculated values
"""


#calculate_file
"""
Read list of start and operations from a file, then calculate

:param file_path: Full path to file
@return list of calculated values
"""



"""
Simple output if you run as a script
"""
if __name__ == '__main__':

    import os
    output = calculate([('+', 3), ('*', 2)], 4) # should be 14
    print("Output of (4+3)*2 = ", output)
    print(30*"-")

    output = calculate_lists([4, 1], [[('+', 3), ('*', 2)], [('-', 2), ('*', 4)]]) # should be [14, -4]
    print("Output of [(4+3)*2, (1-2)*4] = ", output)
    print(30*"-")

    output = calculate_file(os.path.join("data", "calculate.csv"))
    print("Output for file = ", output)
