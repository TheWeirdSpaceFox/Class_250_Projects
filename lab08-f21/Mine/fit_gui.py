from tkinter import *
from tkinter import filedialog
from Mine.calling_file import FitFiles
import os
from os.path import exists
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
from matplotlib import pyplot as plt
class Fit:

    def __init__(self):

        print("  initializing the Fit Gui ...")
        self.root = Tk()

        self.root.title("Amanda.Sanders.20")
        self.win = Frame(self.root)


        menubar = Menu(self.root)
        filemenu = Menu(menubar, tearoff=0)

        filemenu.add_command(label="Open", command=self.open)

        filemenu.add_separator()

        filemenu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        self.root.config(menu=menubar)
        # self.root.mainloop()


        # Create the Enter Cmd label
        self.cmd_label = Label(self.win, text="Enter age:")
        self.cmd_label.grid(row=2, column=1)

        # Create the command entry box
        self.cmd_entry = Entry(self.win, width=20, bg="white")
        self.cmd_entry.grid(row=2,column=2)

        # Create the Enter Cmd label
        self.cmd_label2 = Label(self.win, text="Enter Resting Heart Rate:")
        self.cmd_label2.grid(row=4, column=1)

        # Create the command entry box
        self.cmd_entry2 = Entry(self.win, width=20, bg="white")
        self.cmd_entry2.grid(row=4, column=2)

        self.cmd_label3 = Label(self.win, text="File Number:")
        self.cmd_label3.grid(row=5, column=1)

        # Create the command entry box
        self.cmd_entry3 = Entry(self.win, width=20, bg="white")
        self.cmd_entry3.grid(row=5, column=2)

        # Create the Do It Button
        # self.btn = Button(self.win, text="File Number", command=self.do_it)
        # self.btn.grid(row=3, column=3)

        self.btn = Button(self.win, text="Time Plot", command=self.time_plot)
        self.btn.grid(row=6, column=2)

        self.btn = Button(self.win, text="Distance Plot", command=self.distance_plot)
        self.btn.grid(row=7, column=2)

        # Create the Output Label
        self.output_label = Label(self.win, text="Messages:")
        self.output_label.grid(row=7, column=1)

        # Create the Output text box
        self.output = Text(self.win, width=80, height=5, wrap=WORD,bg='black',fg='white')
        self.output.grid(row=8,column=2, columnspan=1)

        # Create the Quit Button
        self.quit = Button(self.win, text="Quit", command=self.root.quit)
        self.quit.grid(row=9, column=4)

        # Pack the frame
        self.win.pack()
        print("Ending")

    def check_file_number(self):
        cmd1 = self.cmd_entry.get()
        cmd2 = self.cmd_entry2.get()
        file_numbers =[]
        file_path = os.path.join('data', 'male_{}_{}_{}.fit'.format(cmd1, cmd2, 1))
        if os.path.exists(file_path):
            # self.output.insert(END, "male_{}_{}_{}.fit".format(cmd1, cmd2, 1))
            file_numbers.append(1)
        file_path = os.path.join('data', 'male_{}_{}_{}.fit'.format(cmd1, cmd2, 2), "rt")
        if os.path.exists(file_path):
            # self.output.insert(END, "male_{}_{}_{}.fit".format(cmd1, cmd2, 2))
            file_numbers.append(2)
        file_path = os.path.join('data', 'male_{}_{}_{}.fit'.format(cmd1, cmd2, 3))
        if os.path.exists(file_path):
            # self.output.insert(END, "male_{}_{}_{}.fit".format(cmd1, cmd2, 3))
            file_numbers.append(3)
        file_path = os.path.join('data', 'male_{}_{}_{}.fit'.format(cmd1, cmd2, 4))
        if os.path.exists(file_path):
            # self.output.insert(END, "male_{}_{}_{}.fit".format(cmd1, cmd2, 4))
            file_numbers.append(4)
        file_path = os.path.join('data', 'male_{}_{}_{}.fit'.format(cmd1, cmd2, 5))
        if os.path.exists(file_path):
            # self.output.insert(END, "male_{}_{}_{}.fit".format(cmd1, cmd2, 5))
            file_numbers.append(5)
        file_path = os.path.join('data', 'male_{}_{}_{}.fit'.format(cmd1, cmd2, 6))
        if os.path.exists(file_path):
            # self.output.insert(END, "male_{}_{}_{}.fit".format(cmd1, cmd2, 6))
            file_numbers.append(6)
        return file_numbers


    def do_it(self, *args):

        self.output.delete(0.0, END)

        cmd1 = self.cmd_entry.get()
        cmd2 = self.cmd_entry2.get()
        cmd3 = self.cmd_entry3.get()
        number_list = self.check_file_number()

        if cmd1.isdigit() == False or cmd2.isdigit() == False or cmd3.isdigit == False or cmd1 == "" or cmd2 == "" or cmd3 == "" or int(cmd3) not in number_list:
            if cmd1 == "":
                cmd1 = "Must Enter Number For Age"
            elif cmd1.isdigit() == False:
                cmd1 = "Invalid Age Must Be Number"
            else:
                if int(cmd1) < 0 or int(cmd1) > 122:
                    cmd1 = "Invalid Age"
            if cmd2 == "":
                cmd2 = "Must Enter Number For Resting Heart Rate"
            elif cmd2.isdigit() == False:
                cmd2 = "Invalid Resting Heart Rate Must Be Number"
            else:
                if int(cmd2) < 27 or int(cmd2) > 100:
                    cmd2 = "Invalid Resting Heart Rate (or you should probably see a doctor)"
            if cmd3 == "":
                cmd3 = "Must Enter Number For File Number"
            elif cmd3.isdigit() == False:
                cmd3 = "Invalid Must be Number"
            else:
                number = ""
                for num in number_list:
                    number += str(num) + " "
                cmd3 = "Invalid File Number Choose Number Or Change Age Or Heart Rate: " + number
            self.output.insert(END, cmd1 + "\n" + cmd2 + "\n" + cmd3)
        else:
            return True

    def time_plot(self):
        yes_no = self.do_it()
        if yes_no == True:
            cmd1 = self.cmd_entry.get()
            cmd2 = self.cmd_entry2.get()
            cmd3 = self.cmd_entry3.get()
            file = FitFiles(os.path.join('data', 'male_{}_{}_{}.fit'.format(cmd1, cmd2, cmd3)))
            time_array = file.time_array
            heart_rate_array = file.heart_rate_array
            cadence_array = file.cadence_array
            altitude_array = file.altitude_array
            power_array = file.power_array
            speed_array = file.speed_array
            exertion_title = file.exertion_title
            distance_array = file.distance_array
            file_name = file.file_name
            exertion_array = file.exertion_array

            plt.plot(time_array, heart_rate_array, color="red")
            plt.plot(time_array, cadence_array, color="yellow")
            plt.plot(time_array, altitude_array, color="blue")
            plt.plot(time_array, power_array, color="purple")
            plt.plot(time_array, speed_array, color="orange")
            plt.plot(time_array, exertion_array, color="black")
            plt.gca().invert_yaxis()

            plt.suptitle("{} exertion={:.2f} (amanda.sanders.20)".format(file_name, exertion_title), fontsize=12)
            plt.ylabel("Scaled Data", fontsize=10)
            plt.xlabel("Time", fontsize=10)

            name = "{}_{}_{}_time".format(cmd1, cmd2, cmd3)
            plt.savefig(os.path.join('graphs', name))
            fig = os.path.join('graphs', name)
            photo = PhotoImage(file=fig + ".png")
            w = Label(self.win, image=photo)
            w.grid(row=1, column=2)
            mainloop()

    def distance_plot(self):
        yes_no = self.do_it()
        if yes_no == True:
            cmd1 = self.cmd_entry.get()
            cmd2 = self.cmd_entry2.get()
            cmd3 = self.cmd_entry3.get()
            file = FitFiles(os.path.join('data', 'male_{}_{}_{}.fit'.format(cmd1,cmd2,cmd3)))
            time_array = file.time_array
            heart_rate_array = file.heart_rate_array
            cadence_array = file.cadence_array
            altitude_array = file.altitude_array
            power_array = file.power_array
            speed_array = file.speed_array
            exertion_title = file.exertion_title
            distance_array = file.distance_array
            file_name = file.file_name
            exertion_array = file.exertion_array

            plt.plot(distance_array, heart_rate_array, color="red")
            plt.plot(distance_array, cadence_array, color="yellow")
            plt.plot(distance_array, altitude_array, color="blue")
            plt.plot(distance_array, power_array, color="purple")
            plt.plot(distance_array, speed_array, color="orange")
            plt.plot(distance_array, exertion_array, color="black")
            plt.gca().invert_yaxis()


            plt.suptitle("{} exertion={:.2f} (amanda.sanders.20)".format(file_name, exertion_title), fontsize=12)
            plt.ylabel("Scaled Data", fontsize=10)
            plt.xlabel("Distance", fontsize=10)

            name = "{}_{}_{}_distance".format(cmd1, cmd2,cmd3)
            plt.savefig(os.path.join('graphs', name))
            fig = os.path.join('graphs', name)
            photo = PhotoImage(file=fig + ".png")
            w = Label(self.win, image=photo)
            w.grid(row=1, column=2)
            mainloop()


    def open(self):
        data = filedialog.askopenfilename()
        data = data.split("/")
        data = data[-1]
        data = data.split(".")
        data = data[0]
        data = data.split("_")
        cmd1 = data[1]
        cmd2 = data[2]
        cmd3 = data[3]
        self.cmd_entry.insert(END, cmd1)
        self.cmd_entry2.insert(END, cmd2)
        self.cmd_entry3.insert(END, cmd3)


    def run(self):
        print("    Entering the Tk main event loop")
        self.root.mainloop()
        print("    Leaving the Tk main event loop")


if __name__ == '__main__':

    print("Inside main...")
    fit = Fit()
    fit.run()
    print("done!")