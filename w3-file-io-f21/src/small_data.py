"""
Demo some reading of files

Modify your Run-Edit Configuration to point to the project folder, not src!
"""
import os

def read_data(fpath):
    """
    Read data from file into 3 columns  c0|c1|c2
    :param fpath:
    :return: c0,c1,c2
    """

    c0, c1, c2 = [], [], []
    with open(fpath, 'rt') as file:
        lines = file.readlines()
        for line in lines:
            values = line.strip().split('|')
            c0.append(int(values[0]))
            c1.append(int(values[1]))
            c2.append(int(values[2]))

    return c0,c1,c2


def append_data(file_path, max_val=32):
    """
    Add up to i=max_val for i|i^2|i^3
    :param file_path:
    :return: Number of lines written to the file
    """
    c0,_,_ = read_data(file_path)
    start_val = c0[-1]
    with open(file_path, 'at') as file:
        for i in range(start_val+1, max_val+1):
            fmt_string = f"{i}|{i*i}|{i*i*i}\n"
            file.write(fmt_string)


if __name__ == '__main__':
    file_path = os.path.join("data", "small_data.txt")
    print("path:", file_path)

    file = open(file_path, 'rt')
    lines = file.readlines()
    print(lines)
    file.close()

    # # Get me 3 lists of integers
    c1, c2, c3 = read_data(file_path)
    print(c1)
    print(c2)
    print(c3)
    #
    #
    # append_data(file_path)
    #
    # c1, c2, c3 = read_data(file_path)
    #
    # print(c1)
    # print(c2)
    # print(c3)


