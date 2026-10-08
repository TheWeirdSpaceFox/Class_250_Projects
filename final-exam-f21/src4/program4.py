"""
Program 4

You should write the 3 methods defined below.

NOTE: The plot_method depends on the other two.

@author Amanda Sanders
 vvvvvvvvvvv you code below here vvvvvvvvvvvvvv
"""
# pylint: disable=C0103
import numpy as np
import matplotlib.pyplot as plt

def gen_linearly_spaced_values(min, max, n):
    """
    Given a min and max value generate linearly spaced data with n points.
        e.g given min = 0, max=7, and n=8
        return numpy array with [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]

    :return: numpy array
    """

    list = []
    for i in range(n):
        if min < max+1:
            list.append(float(min))
            min += 1
    return list


def get_y_data(t, amplitude, frequency, decay):
    """
    Given one numpy array t (time), and 3 constants use numpy array math to calculate the following function.
        amplitude x sin( frequency * time) x e^(-decay*time)

        Note, the resulting numpy array should contain exactly the same number of elements as the input numpy array, t.
        You are calculating the value of the function for each point in time.

    :param t : input numpy array
    :param amplitude:
    :param decay:
    :param frequency:
    :return: numpy array

    """
    t = np.array(t)
    numpy_array = amplitude * np.sin(frequency*t) * np.exp(-decay * t)
    return numpy_array


def generate_plot(file_name, amplitude, frequency, decay,
                  min_val=0.0, max_val=6.0, samples=50):
    """
        Given parameters, generate the x and y data by calling methods above,
         and plot

        Label axes
            x-axis = "Time [s]"
            y-axis  = "Angle [degs]"

        Title "Pendulum with Friction (first.last.year)"
            With your personal information

        Plot the signal with a red line
        Add a legend for the "Pendulum 1"

        For full credit:
            Plot a second pendulum as a green line.
            Use the original y values, but offset the original x values by .1 to make a "cool" pattern.
            Legend label should be "Pendulum 2"
            Hint: Numpy makes this .1 sec offset easier.


        Save plot to given file name.
        :return: Nothing
    """

    t = gen_linearly_spaced_values(max_val, min_val, samples)
    x = np.array(t)
    x = x + 0.1
    y = get_y_data(t, amplitude, frequency, decay)
    fig = plt.figure()
    plt.plot(x, "-r", label="Pendulum 2")
    plt.plot(y, "b", label="Pendulum 1")
    plt.legend(fontsize=12)
    plt.xlabel("Time [s]")
    plt.ylabel("Angle [degs]")
    plt.title("Pendulum with Friction (amanda.sanders.20)")
    plt.show()
    fig.savefig(file_name)


"""
^^^^^^^^^^^^^^^^^^ your code up here ^^^^^^^^^^^^^^^^^^^^ 
I'm giving you the below code as simple test.  Just leave as is
"""
if __name__ == '__main__':
    """
    Make sure you run this script from the project workspace, not the src4 folder
    """
    import math
    import os
    full_path_file_name = os.path.join("data", "program4_plot.png")

    print("Get the linearly spaced values:")
    x = gen_linearly_spaced_values(0.0, 5.0, 6)
    print("    x data  =", x)
    print("   Should be: [0. 1. 2. 3. 4. 5.]")

    print("Get the y-data:")
    amp, freq, k = 1.0, 10, .5
    y = get_y_data(x, amp, freq, k)
    print("    y data = ", y)
    print("   Should be: [ .         -0.32996548  0.33585379 -0.22045965  0.1008401  -0.02153704]")

    print("Generate plot ")
    generate_plot(full_path_file_name, amp, freq, k, 0.0, 6.3, 200)
    print("Done!")
