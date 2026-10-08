import csv
import matplotlib.pyplot as plt
import numpy as np
import os


def read_headers(filename):
    """
    Return a list of strings that are the column labels from headers.csv

    :param filename: string path and filename for the header file
    :return: list of strings
    """
    header_list = []
    with open(filename) as file:
        lines = file.readlines()
        for header in lines:
            header = header.split()
            for group_headers in header:
                group_headers = group_headers.split(',')
                # header_list.append(group_headers)

    return group_headers


def read_all_data_list(filename):
    """
    Read each column in as a list and return as a list of lists.
    The data type of the elements in the first column should be np.datetime64 for the datetime axis of matplotlib
    The rest of the columns should be floats

    :param filename:
    :return: list of lists with the same dimensions as the text file (6 columns N number of rows)
    """
    list_1 = []
    list_2 = []
    list_3 = []
    list_4 = []
    list_5 = []
    list_6 = []
    final_list = []
    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            # print(line)
            line = line.strip()
            line = line.split(',')
            final_list.append(line)
            list_1.append(np.datetime64(line[0]))
            list_2.append(line[1])
            list_3.append(line[2])
            list_4.append(line[3])
            list_5.append(line[4])
            list_6.append(line[5])


        final_list = [list_1, list_2, list_3, list_4, list_5, list_6]
    return final_list


def get_time_max_min(time, reading):
    """
    Take in two lists and returns the value and time at the minimum and maximum for the reading.
    The reading will be barometric pressure, heat index, temperature, etc.

    :param time: list of np.datetime64 objects
    :param reading: list of floats
    :return: tuple containing (min_value, time_at_min, max_value, time_at_max) where the time is np.datetime64 and values are floats
    """
    # for t, read in zip(time, reading):
    #     print(t, read)
    maxreading = max(reading)
    minreading = min(reading)

    for count, value in enumerate(reading):
        if value == maxreading:
            maxreadingtime =time[count]
        if value == minreading:
            minreadingtime =time[count]

    return minreading, minreadingtime, maxreadingtime, maxreadingtime


def plot_date(x, y, output_filename=os.path.join("fig","temp_09_06.png"), title="My Awesome Plot (Amanda.Sanders.20)", x_label="Date", y_label="y_label"):
    """
    This is a function that provides an interface to plot. Leave for students.

    :param x:
    :param y:
    :param output_filename:
    :param title:
    :param x_label:
    :param y_label:
    :return:
    """

    fig = plt.figure()
    plt.plot(x, y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.savefig(output_filename)
    fig.savefig(os.path.join("data", "weatherhw.png"))
    plt.show()


if __name__ == "__main__":
    # Check that you can read the header file which explains what each column contains in the data file.
    print(80*"-")
    header_data = os.path.join("data", "headers.csv")
    print(read_headers(header_data))

    # Test reading and plotting a small data file
    print(80*"-")
    file_data = os.path.join("data", "weather_09_06.csv")
    my_data = read_all_data_list(file_data)
    # print(my_data)
    plot_date(my_data[0], my_data[1], output_filename=os.path.join("fig","temp_09_06.png"), title="Temperature on 9.06.19 (Amanda.Sanders.20)",y_label="Temperature [deg F]")

    # Test that you can get the min and max of one of the readings
    print(80*"-")
    temp_maxmin = get_time_max_min(my_data[0], my_data[1])
    print(temp_maxmin)
    print("Temperature min {}F Time min {} Temperature max {}F Time max {}".format(temp_maxmin[0],temp_maxmin[1],temp_maxmin[2],temp_maxmin[3]))
