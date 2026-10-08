"""
  Calculate Fibonacci value using both loop and recursion

  @author Amanda Sanders
  @version 0
 """


class Fibonacci:

    def __init__(self):
        # Initialize counters
        self.loop_count = 0
        self.recursion_count = 0

    def fibonacci_loop(self, n):
        """
        Calculate value of Fibonacci sequence at given index
        using a loop (150 style)
            Raise a IndexError if n < 0
        :param n: index
        :return: value at index
        """
        if n < 0:
            raise IndexError("must be greater then 0")
        fn_m1 = 1
        fn_m2 = 0
        for i in range(1, n+1):
            tmp = fn_m2
            fn_m2 = fn_m1
            fn_m1 = tmp + fn_m2
            self.loop_count += 1
        return fn_m2


    def fibonacci_recursion(self,n):
        """
        Calculate value of Fibonacci sequence at given index
        using recursion (250 style)
            Raise a IndexError if n < 0
        :param n: index
        :return: value at index
        """

        if n < 0:
            raise IndexError("must be greater then 0")
        self.recursion_count += 1
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonacci_recursion(n-1) + self.fibonacci_recursion(n-2)


if __name__ == '__main__':

    print("  index     loop (count)   recursion (count)")
    for i in range(16):
    # i = 5;
        fib=Fibonacci()
        print(" fib[{:2d}] = {:15d}({:3}) {:15d} ({:3d})".format(i,
                                               fib.fibonacci_loop(i),fib.loop_count,
                                               fib.fibonacci_recursion(i), fib.recursion_count))

