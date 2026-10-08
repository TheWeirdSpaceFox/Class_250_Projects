import os
import matplotlib.pyplot as plt
from src.signal_io import folder_name, write_csv_as_binary, read_binary, convert_data


if __name__ == '__main__':
    ws,ns,sd = write_csv_as_binary("signal_data")
    wsb,nsb,sdb = read_binary("signal_data")
    tv, sdv = convert_data(wsb, nsb, sdb)

    print(" ws data:",ws==wsb)
    print(" ns data:",ns==nsb)
    print(" sd data:",sd==sdb)

    fig = plt.figure(1)
    plt.plot(tv,sdv,'b-',label="signal",linewidth=2)
    plt.legend()
    plt.xlabel('time (s)')
    plt.ylabel('signal')
    plt.title('Signal Data (amanda.sanders.20)')
    fig.savefig(os.path.join(folder_name,"signal_data.png"))

    plt.show()
