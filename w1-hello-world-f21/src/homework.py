

"""
Define a method called cnu_captains that takes no arguments.

Create a string that has one line per integer from 1 to 100 inclusive
(Remember, range starts at 0, be careful)

if the number is divisible by 2 the line should be "CNU"
if the number is divisible by 5 the line should be "CAPTAINS"
if the number is divisible by 2 and 5 the line should be "CNUCAPTAINS"
Otherwise, you should should have the integer on the line.

Each line should be separated by a new-line "\n".

First few lines should look like this:
1
CNU
3
CNU
CAPTAINS
CNU
7
CNU
9
CNUCAPTAINS
11

:return: String that is described above
"""

# Fix this with defined method
# def cnu_captains():
#     i = 1
#     while i <= 100 and i >= 0:
#         if i %2 ==0 and i %5 ==0:
#             i += 1
#             print("CNUCAPTAINS")
#         elif i %2==0:
#             i += 1
#             print("CNU")
#         elif i %5==0:
#             i += 1
#             print("CAPTAINS")
#         else:
#             print(i)
#             i += 1

def cnu_captains():
    i = 1
    string =''
    while i <= 100 and i >= 0:
        if i %2 ==0 and i %5 ==0:
            i += 1
            string += "CNUCAPTAINS\n"
        elif i %2==0:
            i += 1
            string += "CNU\n"
        elif i %5==0:
            i += 1
            string += "CAPTAINS\n"
        else:
            string += str(i)
            string += '\n'
            i += 1
    return string



if __name__ == '__main__':
    print(cnu_captains())
