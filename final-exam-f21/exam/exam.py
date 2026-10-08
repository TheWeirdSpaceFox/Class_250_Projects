"""
These methods can be called inside WebCAT to determine which tests are loaded
for a given section/exam pair.  This allows a common WebCAT submission site to
support different project tests
"""

## STUDENTS - DO NOT CHANGE!
def section():
    # Instructor section (instructor to change before distribution)
    return 8042 # Phelps


def exam():
    # A or B exam (instructor to change to match specific project distribution
    return "A"
    #return "B"
