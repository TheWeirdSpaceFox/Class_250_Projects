import os


def text_attributes(file_path):
    """
    Given a file_path of a valid text file return the number of characters and number of lines in a file.

    Note: Ignore newlines for the character count!

    :param file_path: File path with filename
    :return: tuple with number of characters and number of lines in that order
    """
    #file_path = os.path.join("data", "")

    with open(file_path) as file:
        lines = file.readlines()
        number_of_character = len(lines)
        # without spaces
        # lines = file.readlines().replace(" ","")
        # number_of_character = len(lines)
        for i in lines:
            lines = lines.split()

        number_of_lines = 0
    return (number_of_character, number_of_lines)


def write_file(file_path, n):
    """
    Write a pattern that looks like this into a file with n number of lines

    Below is the result of make_pattern(file_path, 5)
    *
    ##
    ***
    ####
    *****

    :param file_path:
    :param n: Number of lines to follow this pattern
    :return:
    """
    pass


def append_file(file_path, n):
    """
    Open a file and continue the pattern as seen above in the file. The pattern will be the same as in write_file().

        Note: Do not write a new file or you will not receive credit for the function.

        Note #2: You should be able to continue the pattern based on the last line only.
                 Meaning you should be able to continue the patter of a file that only has "*****\n" in it.

    :param file_path:
    :param n: Max number of lines
    :return: n_lines: number of lines written
    """
    pass


def fourier_analysis(file_path):
    """
    Read in a text file where the path and filename is given by the input parameter file_path
    There are 4 columns in the text file that are separated by colons ":".  col1:col2:col3:col4
    Code in the main block specifies which file to open.

    Plot all 3 datasets in one figure. (x axis vs y axis)
    col1 vs col2 (Label "n=1"), col1 vs col3 (Label "n=3"), col1 vs col4 (Label "n=5")

    Make sure you have proper x and y labels and a title. The x label should be "t", y should be "Function Sum"
    And the title be Fourier Analysis. Remember, you should have your first.last.yy in parentheses in the title.

        Note: For full credit you must also include a legend with the dataset labels as shown above.

    Upload the resulting plot (.png) to scholar for credit. No unit tests here.
    :param file_path:
    :return:
    """
    c1 = []
    c2 = []
    c3 = []
    c4 = []
    with open(file_path) as file:
        lines = file.readlines()
        # print(lines)
        for line in lines:
            line = line.strip()
            line = line.split(':')
            # print(line)
            c1.append(line[0])
            c2.append(line[1])
            c3.append(line[2])
            c4.append(line[3])
    # print('c1 =', c1)
    # print('c2 =', c2)
    # print('c3 =', c3)
    # print('c4 =', c4)


    import matplotlib.pyplot as plt
    fig = plt.figure()
    plt.plot(c1[:14], c2[:14], 'r-', label='n=1')
    plt.plot(c1[:10], c3[:10], 'g.', label='n=3')
    plt.plot(c1[:7], c4[:7], 'b:', label='n=5')
    plt.legend(fontsize=12)
    plt.xlabel('t', fontsize=24)
    plt.ylabel('Function Sum', fontsize=24)
    plt.grid()
    plt.title("Fourier Analysis (amanda.sanders.21)")
    fig.savefig("data/plot_data.png")
    plt.show()
    pass


if __name__ == '__main__':
    write_file(os.path.join("data", "cpsc150.txt"), 5)
    append_file(os.path.join("data", "cpsc150.txt"), 15)
    file_path = os.path.join("data", "fourier_dataset.txt")
    fourier_analysis(file_path)
