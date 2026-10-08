"""
Program 1

Write functions as defined by docstrings below

@author amanda sanders
"""
import os
import csv
import matplotlib.pyplot as plt
import numpy as np


def write_file(file_path):
    """
    Given a valid filepath write "Happy 60th Anniversary, CNU!\n" to the file.

    :param file_path:
    :return: number of characters written to the file
    """
    text = "Happy 60th Anniversary, CNU!\n"
    with open(file_path, 'wt') as file:
        file.write(text)
    return len(text)


def plancks_law_data(file_path):
    """
    Given a valid filepath read a text file.
    The text file contains 5 columns of data separated by a tilde "~" symbol:

    You should return 5 lists of these values as floating point numbers.
      Note: You are not allowed to use any library other than csv or os for this task.

    :param file_path:
    :return: a tuple containing a list for each column of data
    """
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    with open(file_path) as file:
        for line in file.readlines():
            line = line.strip().split('~')
            list1.append(float(line[0]))
            list2.append(float(line[1]))
            list3.append(float(line[2]))
            list4.append(float(line[3]))
            list5.append(float(line[4]))

    return list1, list2, list3, list4, list5


def plot_data(file_path):
    """
    Given a valid filepath to a data file.

    Read in the x and y values (they are in that order) into lists and plot them in matplotlib.

    The title should be "Happy 60th Anniversary CNU! (first.last.yy)"
    The x axis label should be "Logo x"
    The y axis label should be "Logo y"

    Save the image and upload to scholar (no screenshots).

    :param file_path:
    :return:
    """
    x, y = [], []

    with open(file_path) as file:
        #print("lion", lines)
        for line in file.readlines():
            x_temp, y_temp = line.strip().split(",")
            x.append(float(x_temp))
            y.append(float(y_temp))
            #print("line", line)

    fig = plt.figure()
    plt.plot(x,y)
    plt.xlabel("Logo x")
    plt.ylabel("Logo y")
    plt.title("Happy 60th Anniversary CNU! (amanda.sanders.20)")
    plt.show()
    fig.savefig(os.path.join("data", "Happy 60th Anniversary CNU!"))
    pass


def get_x_data(min_val, max_val, samples):
    """
    Return a Numpy array or list starting at min_val and going to max_val
    with defined number of samples
    e.g given min_val = 0, max_val=5, and samples=6
    return numpy array or list with [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]

    :return: instance of numpy array
    """
    return np.linspace(min_val, max_val, samples)

def numpy_polynomial(x, coefficients):
    """
    In this problem you will be asked to evaluate a function using numpy.
    You will be given a numpy array x and a list of coefficients that determine what order polynomial function you will calculate.

    If you are given a numpy array x and a list of coefficients [c1,c2,c3], for example the polynomial will follow this pattern:
        f(x) = c1*x^0 + c2*x^2 + c3*x^4
        Note: The list of coefficients can be of any length and would change the number of terms in the polynomial.
              (ex: if the length of the coefficients list is 4, then your polynomial would go up to the x^8 term)

    You should return two numpy arrays that have the same length as the input array x. Return them in a tuple.
        The two arrays should be a polynomial f(x) as one numpy array and the polynomial f(x) after normalization.
        Note: Normalization in this case is where you divide each element of the array by the mean of all elements


    :param x: Numpy array of x values
    :param coefficients: list of polynomial coefficients
    :return: tuple of two numpy arrays, the result, and normalized result
    """
    sum_array = np.zeros(len(x))

    for i in range(len(coefficients)):
        sum_array += coefficients[i] * x ** (i*2)

    normalized_array = sum_array/np.mean(sum_array)

    return sum_array, normalized_array


if __name__ == '__main__':
    # Write your own test code here or use what I have provided:

    # Write a file
    import os
    write_file(os.path.join("data", "test_file.txt"))

    # Planks_law_data
    file_path = os.path.join("data", "radiation.txt")
    x, y1, y2, y3, y4 = plancks_law_data(file_path)
    print(x[:5])
    print(y1[:5])
    print(y2[:5])
    print(y3[:5])
    print(y4[:5])

    print("Get the x-data:")
    x = get_x_data(0.0, 5.0, 6)
    print("    x data  =", x)

    print("This should create your plot")
    plot_data(os.path.join("data", "cnu_data.csv"))