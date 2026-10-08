"""
Program 3




@author Amanda Sanders
 vvvvvvvvvvv you code below here vvvvvvvvvvvvvv
"""
# pylint: disable=C0103


class Program3:

    def __init__(self):
        self.counter1 = 0
        self.counter2 = 0

    def remove_vowels(self, a_string):
        """
        Given a string, return a string with the vowels removed. You should do this one character at a time, recursively.

        Note: Do not use unnecessary/extra base cases as they will interfere with unit tests.
            vowels include a,e,i,o,u

        Examples:
         Given "abcde" return "bcd"
         Given "ae" return ""

        :param a_string:
        :return: number of vowels
        """
        # Do not modify this incrementing of the counter.
        self.counter1 += 1
        if a_string == "":
            return "empty string"
        elif "a" in a_string:
            return self.remove_vowels([a_string[1:]])
        elif "e" in a_string:
            return self.remove_vowels([a_string[1:]])
        elif "i" in a_string:
            return self.remove_vowels([a_string[1:]])
        elif "o" in a_string:
            return self.remove_vowels([a_string[1:]])
        elif "u" in a_string:
            return self.remove_vowels([a_string[1:]])
        else:
            return a_string






    def pattern(self, n):
        """
        Write a method to calculate values in a sequence.
            An element in the sequence is defined as 2 times the previous value in the sequence plus the second value prior in the sequence minus the third value in the sequence.

        For values less than 0 raise a ValueError

        n    0   1   2   3   4  ...
        f(n) 6   7   8  17  35

        Hints:
            -Do not use unnecessary or extra base cases as they will interfere with unit tests.

        :param n:
        :return: sequence value
        """

        # Do not modify this incrementing of the counter.
        self.counter2 += 1
        if n < 0:
            raise ValueError("n must be greater then 0")
        elif n == 0:
            return 6
        elif n == 1:
            return 7
        elif n == 2:
            return 8
        else:
            return (2 * self.pattern(n-1)) + self.pattern(n-2) - self.pattern(n-3)


if __name__ == '__main__':
    print("\n"+"*"*25)
    program1 = Program3()
    actual = program1.remove_vowels("Hello World!")
    print("Expected:", "Hll Wrld!")
    print("Actual:  ", actual)

    print("\n"+"*"*25)
    print("n    expected  actual")
    expected = [6, 7, 8, 17, 35]
    for i in range(20):
        print(program1.pattern(i), ",", end ="")
    print()
    for i in range(20):
        program1 = Program3()
        program1.pattern(i)
        print(program1.counter2, ",", end ="")
    print()
    for i, val in enumerate(expected):
        print(f"{i}     {val:4d}     {program1.pattern(i):4d}")
