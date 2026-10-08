"""
We will demo so debugging techniques, and highlight some issues
with style, and testing.

Please follow along, commit as I do, and don't rush ahead if you
see the errors of my ways as we plan to demonstrate debugging.

@author Amanda Sanders
@version 9/2/21
"""

def int_calc(x):
    """
    # Warning - this method written by an under caffeinated 150 student

    Calculates an integer value as follows:
    Given integer value, calculate the product of all values from 1 up
    to and including the value.

    If the input value is odd, then add 100,000;
    if even, then add 1,000.
    So if value is 1, then output is 100,001
    if value is 2, then output is 1,002
    if value is 4, then value is 1,024  (4*3*2*1 + 1000)

    @param x - integer input
    @return integer value

    """

    prod = 1
    for i in range(1, x+1):
        prod = prod * i

    if prod % 2 == 0:
        # Even add 1000
        return prod + 1000
    else:
        return prod + 100000

if __name__ == '__main__':

    print("int_calc(1)=", int_calc(1))
    print("int_calc(2)=", int_calc(2))
    print("int_calc(4)=", int_calc(4))
