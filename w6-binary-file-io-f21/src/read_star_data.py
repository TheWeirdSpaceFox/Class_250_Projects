import matplotlib.pyplot as plt
import struct
import os


def plot_star_data(filepath):
    """
    Given a valid filepath, you will read a binary file that consists of two "columns" of double precision floating point numbers.
    The format is little endian. Once you have read the data plot the first column vs the second column (x axis is the first column).

    You should always properly label your plot!
        - In this case since there are no units you can title the x and y axes "x" and "y".
        - The title should be "Star Plot - (first.last.yy)"
        - Turn in this figure to scholar

    Hint: You will know that you are plotting the data correctly if the name of this function makes sense.

    :param filepath:
    :return:
    """
    new_list1 = []
    new_list2 = []
    with open(filepath, encoding="utf-8") as file:
        ba = bytearray(file.read())

        chunk_size = struct.calcsize("<d")
        n_chunk = len(ba) // chunk_size


        for i in range(n_chunk):
            start = i * chunk_size
            stop = start + chunk_size
            my_bytes = ba[start:stop]

    pass


if __name__ == "__main__":
    file = os.path.join("data", "star.dat")
    plot_star_data(file)
