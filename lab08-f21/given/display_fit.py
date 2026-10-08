"""
Demonstration of parsing fit file for CPSC 250 Lab
"""

import os

from fitparse import FitFile


def display_fit(file_name):
    """
    Load a fit file and display some of the relevant data
    @param file_name : name of fit file (including relative path)
    """
    # Load the FIT file
    fitfile = FitFile(file_name)

    relevant_fields = ['timestamp', 'speed', 'altitude', 'power', 'cadence', 'heart_rate']

    initial_flag = True
    prior_time = None
    # Iterate over all messages of type "record"
    # (other types include "device_info", "file_creator", "event", etc)
    for record in fitfile.get_messages("record"):

        # Records can contain multiple pieces of data (ex: timestamp, latitude, longitude, etc)
        rec_dict = record.get_values()

        if initial_flag:
            initial_flag = False  # only display all record names once

            # Show information stored in Fit file
            print(" record: ", type(record))
            for key in rec_dict:
                print("  ->", key, rec_dict[key])

            for msg in record:
                print("  =>", msg)

            fields = record.as_dict()['fields']
            for fld in fields:
                print("  *>", fld)

            # Initialize prior time only the first time
            prior_time = rec_dict['timestamp']

        # For each record show field data that are relevant to us
        elapsed = rec_dict['timestamp']-prior_time
        print("  elapsed = ", type(elapsed), elapsed.total_seconds())
        prior_time = rec_dict['timestamp']
        for field in relevant_fields:
            value = rec_dict[field]
            print("    ", field, value)



if __name__ == '__main__':
    file_name = os.path.join('data', 'male_23_65_1.fit')
    print("Using fit file: ", file_name)

    display_fit(file_name)
