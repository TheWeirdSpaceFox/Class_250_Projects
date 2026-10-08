from fitparse import FitFile
import os
import numpy as np
from matplotlib import pyplot as plt
import math
from datetime import timedelta
from datetime import datetime

class FitFiles:
    def __init__(self, file_name):
        self.file_name = file_name
        relevant_fields = ['timestamp', 'speed', 'altitude', 'power', 'cadence', 'heart_rate']

        age_heartrate = self.file_name.split("_")
        age = age_heartrate[1]
        age = int(age)
        heart = age_heartrate[2]
        heart = int(heart)
        timestamp = []
        speed = []
        altitude = []
        power = []
        cadence = []
        heart_rate = []
        # print(display_fit(file_name))
        fitfile = FitFile(self.file_name)
        for record in fitfile.get_messages("record"):
            rec_dict = record.get_values()
            i = 0
            for field in relevant_fields:
                value = rec_dict[field]
                if i == 0:
                    timestamp.append(value)
                elif i == 1:
                    speed.append(value)
                elif i == 2:
                    altitude.append(value)
                elif i == 3:
                    power.append(value)
                elif i == 4:
                    cadence.append(value)
                elif i == 5:
                    heart_rate.append(value)
                i += 1
                # print("    ", field, value)
        speed_array = np.array(speed)

        distance = [0]
        # formula = (b - a) * (1/2) * (f(a) + f(b))
        for i in range(1, len(speed)):
            answer = (timestamp[i] - timestamp[i - 1]).total_seconds() * (1 / 2) * (
                        speed[i] + speed[i - 1])  # This seems wrong
            distance.append(answer)
        distance_array = np.array(distance)
        speed_array = (speed_array * 18) / 5
        distance_array = distance_array / 1000
        self.distance_array = np.cumsum(distance_array)
        Hrmax = 205.8 - (0.685 * age)
        Hrreserve = Hrmax - heart
        time_list = [0]
        for time in range(1, len(timestamp)):
            new_time = (timestamp[time] - timestamp[time - 1]).total_seconds()
            time_list.append(new_time)

        exertion = []
        endurence = heart + (0.2 * Hrreserve)  # maybe
        tempo = heart + (0.4 * Hrreserve)  # says this to threshold
        threshold = heart + (0.58 * Hrreserve)
        VO2_max = heart + (0.72 * Hrreserve)  # says this to anaerobic
        anaerobic = heart + (0.90 * Hrreserve)

        i = 0
        for rate in heart_rate:
            if rate > endurence and rate < tempo:
                point = (1 / 900) * time_list[i]
                exertion.append(point)
                i += 1
            elif rate > tempo and rate < threshold:
                point = (1 / 360) * time_list[i]
                exertion.append(point)
                i += 1
            elif rate > threshold and rate < VO2_max:
                point = (1 / 180) * time_list[i]
                exertion.append(point)
                i += 1
            elif rate > VO2_max and rate < anaerobic:
                point = (1 / 45) * time_list[i]
                exertion.append(point)
                i += 1
            elif rate >= anaerobic:
                point = (1 / 10) * time_list[i]
                exertion.append(point)
                i += 1
            else:
                exertion.append(0)
                i += 1
        exertion_array = np.array(exertion)
        exertion_array = np.cumsum(exertion_array)
        power_array = np.array(power)
        altitude_array = np.array(altitude)
        cadence_array = np.array(cadence)
        heart_rate_array = np.array(heart_rate)
        self.time_array = np.cumsum(time_list)

        self.exertion_title = exertion_array[-1]

        self.heart_rate_array = heart_rate_array / ((math.ceil(max(heart_rate_array) / 10)) * 10)
        self.cadence_array = cadence_array / ((math.ceil(max(cadence_array) / 10)) * 10)
        self.altitude_array = altitude_array / ((math.ceil(max(altitude_array) / 10)) * 10)
        self.power_array = power_array / ((math.ceil(max(power_array) / 10)) * 10)
        self.speed_array = speed_array / ((math.ceil(max(speed_array) / 10)) * 10)
        self.exertion_array = exertion_array / ((math.ceil(max(exertion_array) / 10)) * 10)


    def plot_from_file(self):
        plt.title("{} exertion={:.2f} (amanda.sanders.20)".format(self.file_name, self.exertion_title))
        # exertion_array, speed_array, power_array, altitude_array, cadence_array, heart_rate_array
        plt.plot(self.time_array, self.heart_rate_array)
        plt.plot(self.time_array, self.cadence_array)
        plt.plot(self.time_array, self.altitude_array)
        plt.plot(self.time_array, self.power_array)
        plt.plot(self.time_array, self.speed_array)
        plt.plot(self.time_array, self.exertion_array)
        plt.ylabel("Scaled Data")
        plt.xlabel("Time")
        #plt.show()

        plt.title("{} exertion={:.2f} (amanda.sanders.20)".format(self.file_name, self.exertion_title))
        plt.plot(self.distance_array, self.heart_rate_array)
        plt.plot(self.distance_array, self.cadence_array)
        plt.plot(self.distance_array, self.altitude_array)
        plt.plot(self.distance_array, self.power_array)
        plt.plot(self.distance_array, self.speed_array)
        plt.plot(self.distance_array, self.exertion_array)
        plt.ylabel("Scaled Data")
        plt.xlabel("Distance")
        #plt.show()

        return self.file_name, self.exertion_title, self.time_array, self.heart_rate_array, self.cadence_array, self.altitude_array, self.power_array, self.speed_array, self.exertion_array, self.distance_array

# def everything(file_name):
#     relevant_fields = ['timestamp', 'speed', 'altitude', 'power', 'cadence', 'heart_rate']
#
#     age_heartrate = file_name.split("_")
#     age = age_heartrate[1]
#     age = int(age)
#     heart = age_heartrate[2]
#     heart = int(heart)
#     timestamp = []
#     speed = []
#     altitude = []
#     power = []
#     cadence = []
#     heart_rate = []
#     #print(display_fit(file_name))
#     fitfile = FitFile(file_name)
#     for record in fitfile.get_messages("record"):
#         rec_dict = record.get_values()
#         i = 0
#         for field in relevant_fields:
#             value = rec_dict[field]
#             if i == 0:
#                 timestamp.append(value)
#             elif i == 1:
#                 speed.append(value)
#             elif i == 2:
#                 altitude.append(value)
#             elif i == 3:
#                 power.append(value)
#             elif i == 4:
#                 cadence.append(value)
#             elif i == 5:
#                 heart_rate.append(value)
#             i += 1
#             #print("    ", field, value)
#     speed_array = np.array(speed)
#
#     distance = [0]
#     #formula = (b - a) * (1/2) * (f(a) + f(b))
#     for i in range(1, len(speed)):
#         answer = (timestamp[i] - timestamp[i - 1]).total_seconds() * (1/2) * (speed[i] + speed[i-1]) #This seems wrong
#         distance.append(answer)
#     distance_array = np.array(distance)
#     speed_array = (speed_array* 18)/5
#     distance_array = distance_array/1000
#     distance_array = np.cumsum(distance_array)
#     Hrmax = 205.8 - (0.685 * age)
#     Hrreserve = Hrmax - heart
#     time_list = [0]
#     for time in range(1, len(timestamp)):
#         new_time = (timestamp[time] - timestamp[time-1]).total_seconds()
#         time_list.append(new_time)
#
#     exertion = []
#     endurence = heart + (0.2 * Hrreserve) #maybe
#     tempo = heart + (0.4 * Hrreserve) #says this to threshold
#     threshold = heart + (0.58 * Hrreserve)
#     VO2_max = heart + (0.72 * Hrreserve) #says this to anaerobic
#     anaerobic = heart + (0.90 * Hrreserve)
#
#     i = 0
#     for rate in heart_rate:
#         if rate > endurence and rate < tempo:
#             point = (1/900) * time_list[i]
#             exertion.append(point)
#             i += 1
#         elif rate > tempo and rate < threshold:
#             point = (1/360) * time_list[i]
#             exertion.append(point)
#             i += 1
#         elif rate > threshold and rate < VO2_max:
#             point = (1/180) * time_list[i]
#             exertion.append(point)
#             i += 1
#         elif rate > VO2_max and rate < anaerobic:
#             point = (1/45) * time_list[i]
#             exertion.append(point)
#             i += 1
#         elif rate >= anaerobic:
#             point = (1/10) * time_list[i]
#             exertion.append(point)
#             i += 1
#         else:
#             exertion.append(0)
#             i +=1
#     exertion_array = np.array(exertion)
#     exertion_array = np.cumsum(exertion_array)
#     power_array = np.array(power)
#     altitude_array = np.array(altitude)
#     cadence_array = np.array(cadence)
#     heart_rate_array = np.array(heart_rate)
#     time_array = np.cumsum(time_list)
#
#     exertion_title = exertion_array[-1]
#
#     heart_rate_array = heart_rate_array/((math.ceil(max(heart_rate_array)/10))*10)
#     cadence_array = cadence_array/((math.ceil(max(cadence_array)/10))*10)
#     altitude_array = altitude_array/((math.ceil(max(altitude_array)/10))*10)
#     power_array = power_array/((math.ceil(max(power_array)/10))*10)
#     speed_array = speed_array/((math.ceil(max(speed_array)/10))*10)
#     exertion_array = exertion_array/((math.ceil(max(exertion_array)/10))*10)
#
#     plt.title("{} exertion={:.2f} (amanda.sanders.20)".format(file_name, exertion_title))
#     # exertion_array, speed_array, power_array, altitude_array, cadence_array, heart_rate_array
#     plt.plot(time_array, heart_rate_array)
#     plt.plot(time_array, cadence_array)
#     plt.plot(time_array, altitude_array)
#     plt.plot(time_array, power_array)
#     plt.plot(time_array, speed_array)
#     plt.plot(time_array, exertion_array)
#     plt.ylabel("Scaled Data")
#     plt.xlabel("Time")
#     plt.show()
#
#     plt.title("{} exertion={:.2f} (amanda.sanders.20)".format(file_name, exertion_title))
#     plt.plot(distance_array, heart_rate_array)
#     plt.plot(distance_array, cadence_array)
#     plt.plot(distance_array, altitude_array)
#     plt.plot(distance_array, power_array)
#     plt.plot(distance_array, speed_array)
#     plt.plot(distance_array, exertion_array)
#     plt.ylabel("Scaled Data")
#     plt.xlabel("Distance")
#     plt.show()
#


if __name__ == '__main__':
    # file_name = os.path.join('data', 'male_23_65_1.fit')
    # everything(file_name)


    # file_name = os.path.join('data', 'male_54_66_3.fit')
    # file_name = os.path.join('data', 'male_54_66_4.fit')
    # file_name = os.path.join('data', 'male_54_66_5.fit')
    # file_name = os.path.join('data', 'male_54_66_6.fit')
    # file_name = os.path.join('data', 'male_54_67_2.fit')
    file_name = FitFiles(os.path.join('data', 'male_54_68_1.fit'))
    file_name.plot()