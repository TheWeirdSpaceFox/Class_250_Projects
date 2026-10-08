"""
  Calculate factorial using both loop and recursion

  @author Amanda Sanders
  @version 0
 """

def factorial_loop(n):
    """
      Calculate factorial using a loop (150 style)
        Raise a ValueError if n < 0
    :param n: number
    :return: n!
    """
    fact = 1
    if n < 0:
        return ValueError("n must be greater then 0")
    for i in range(1, n+1):
            fact *= i
    return fact

def factorial_recursion(n):
    """
    Calculate factorial using recursion (250 style!)
        Raise a ValueError if n < 0
    :param n:
    :return: n!
    """

    if n < 0:
        return ValueError("n must be greater then 0")
    #base case
    if n < 2:
        return 1
    #recursive case
    return n * factorial_recursion(n-1)

if __name__ == '__main__':
    for i in range(16):
    # i = 5;
        print(" {:2d}! = {:15d} {:15d}".format(i, factorial_loop(i), factorial_recursion(i)))
