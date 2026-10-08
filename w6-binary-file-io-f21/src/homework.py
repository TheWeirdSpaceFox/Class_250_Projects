import struct
import os


def read_attributes(file_path, format):
    """
    Given a binary file written using struct.pack() with the given format, return the number of bytes in the file and the number of bytes in each chunk.

    :param file_path:
    :param format: a string with the format of the data in the struct
    :return: tuple with the number of bytes in file and the number of bytes written in each chunk
    """
    with open(file_path) as file:
        ba = file.read()

        chunk_size = struct.calcsize(format)
        # print("chunksize", chunk_size, 'bytes')
        # print('filesize', len(ba), 'bytes')
        n_chunk = len(ba)//chunk_size
        # print("# chunks", n_chunk)
        #use n_chunks to get things

    return (len(ba), chunk_size)


def read_binary_file(file_path):
    """

    Read a binary file that is formatted using little endian format and that has one integer and 3 doubles in that order.
    Return 4 lists (In the same order that you read the columns).

    :param file_path:
    :return:
    """

    new_list1 = []
    new_list2 = []
    new_list3 = []
    new_list4 = []
    with open(file_path, 'rb') as file:
        ba = bytearray(file.read())

        chunk_size = struct.calcsize("<iddd")
        # print("chunksize", chunk_size, 'bytes')
        # print('filesize', len(ba), 'bytes')
        n_chunk = len(ba) // chunk_size
        # print("# chunks", n_chunk)



        for i in range(n_chunk):
            start = i * chunk_size
            stop = start + chunk_size
            my_bytes = ba[start:stop]
            list1, list2, list3, list4 = struct.unpack('<iddd', my_bytes)
            new_list1.append(list1)
            new_list2.append(list2)
            new_list3.append(list3)
            new_list4.append(list4)

        # for line in file:
        #     print(line)
        #     if (len(line) > 0):
        #         list1.append(int(line[0]))
        #         list2.append(int(line[1]))
        #         list3.append(int(line[2]))
        #         list4.append(int(line[3]))
        # print('list1', list1)
        #
        # unpack = struct.unpack('<iddd', bytearray(list1))
        # new_list1.append(unpack)
        # unpack = struct.unpack('<iddd', list2)
        # new_list2.append(unpack)
        # unpack = struct.unpack('<iddd', list3)
        # new_list3.append(unpack)
        # unpack = struct.unpack('<iddd', list4)
        # new_list4.append(unpack)


    return new_list1, new_list2, new_list3, new_list4


if __name__ == '__main__':
    print(read_attributes(os.path.join("data", "binary.dat"), ">iid"))
    # print(read_binary_file("data/binary.dat"))
    print((read_binary_file(os.path.join("data", "binary.dat"))))
