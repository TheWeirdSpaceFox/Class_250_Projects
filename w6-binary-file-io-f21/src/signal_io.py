import os
import struct
import csv
import numpy as np

folder_name ="data"

def write_csv_as_binary(file_name):
    """
    Read in data from csv file, and resave as binary
    :param file_name:
    :return: ws, ns, sd data from csv file as lists
    """

    ws = []
    ns = []
    sd = []
    with open(os.path.join(folder_name, file_name + ".csv"), "r") as csv_file:
        line_reader = csv.reader(csv_file, delimiter=',', lineterminator='\n')
        for line in line_reader:
            # print(line)
            if (len(line) > 0):
                ws.append(int(line[0]))
                ns.append(int(line[1]))
                sd.append(float(line[2]))

    print("First:", ws[0], ns[0], sd[0])
    print("Last :", ws[-1], ns[-1], sd[-1])

    # Now pack the data into a byte array
    # https://docs.python.org/3/library/stdtypes.html#bytearray
    # Using struct
    # https://docs.python.org/3/library/struct.html

    # @fixme
    ba = bytearray()
    for i in range(len(ws)):
        my_bytes = struct.pack(">iid", ws[i], ns[i], sd[i])
        ba.extend(my_bytes)

    file_path = os.path.join("data", file_name+".dat")
    with open(file_path, "wb") as file:
        file.write(ba)

    ## Now open a file for writing binary data ("wb") and write the byte array
    # @fixme

    # Return the data we read in from csv
    return ws, ns, sd


def read_binary(file_name):
    """
    Read binary file data
    :param file_name: filename
    :return: ws, ns, sd data from csv file as lists
    """
    file_path = os.path.join(folder_name, file_name+'.dat')
    with open(file_path, 'rb') as file:
        ba = bytearray(file.read())

        chunk_size = struct.calcsize(">iid")
        #print("chunksize", chunk_size, 'bytes')
        #print('filesize', len(ba), 'bytes')
        n_chunk = len(ba)//chunk_size
        #print("# chunks", n_chunk)

        first_chunk = ba[:16]
        #print(struct.unpack(".iid", first_chunk))

        second_chunk = ba[16:32]
        #print(struct.unpack(".iid", second_chunk))
        ws,ns,sd = [],[],[]
        for i in range(n_chunk):
            start = i * chunk_size
            stop = start + chunk_size
            my_bytes = ba[start:stop]
            ws_temp, ns_temp, sd_temp = struct.unpack('>iid', my_bytes)
            ws.append(ws_temp)
            ns.append(ns_temp)
            sd.append(sd_temp)
    return ws, ns, sd

def convert_data(ws,ns,sd):
    """
    Convert epoch timestamp into zero referenced float
    :param ws: whole seconds since Jan 1, 1970
    :param ns: nanoseconds since whole second
    :return: time and signal data as two float numpy arrays
    """
    ws = np.array(ws)
    ns = np.array(ns)
    sd = np.array(sd)
    #zero referencing
    ws = ws - ws[0]
    t = ws + ns*1e-9
    return t, sd



if __name__ == '__main__':
    #write_csv_as_binary("signal_data")
    print(read_binary("signal_data"))