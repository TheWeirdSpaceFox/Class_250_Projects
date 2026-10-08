"""
Practice with lists and tuples


@author Amanda Sanders
@version 9/1/21

"""
# pylint: disable-msg=C0103


def motion(start, motions):
    """
    Calculate the final position given a starting point (x,y), and a list
    of incremental motions as a list of tuples (dx, dy)

    Calculate the final position by adding the incremental motions to the
    appropriate term.
    For example, starting at (1,2), with
    motions=[(2,0), (0, 2), (1, 3)]
    The intermediate positions would be
    (1+2, 2),  (3, 2+2), (3+1, 4+3) with final position (4, 7)

    Hint: You may need to convert from tuple-to-list and list-to-tuple

    :param start:  tuple of starting position (x,y)
    :param motions:  list of tuples of [(dx1, dy1), ...(dxn, dyn)]
                       that define incremental "motions" on a grid
    :return: tuple with final (x,y) position
    """
    xposition = start[0]
    yposition = start[1]
    i = 0
    while i <= len(motions)-1:
        motion1 = motions[i]
        motion1x = motion1[0]
        motion1y = motion1[1]

        xposition += motion1x
        yposition += motion1y

        i += 1


    # motion1 = motions[0]
    # motion1x = motion1[0]
    # motion1y = motion1[1]
    #
    # motion2 = motions[1]
    # motion2x = motion2[0]
    # motion2y = motion2[1]
    #
    # motion3 = motions[2]
    # motion3x = motion3[0]
    # motion3y = motion3[1]
    #
    # xposition += motion1x
    # xposition += motion2x
    # xposition += motion3x
    #
    # yposition += motion1y
    # yposition += motion2y
    # yposition += motion3y

    tuple = (xposition, yposition)
    return tuple


if __name__ == '__main__':
    # Here is simple test - no need to modify below
    start = (1, 2)
    motions = [(2, 0), (0, 2), (1, 3)]
    print("Final position", motion(start, motions))
