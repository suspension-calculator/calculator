# src/suspension/core/functions/line_seperation.py


def LineSeperation(x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4):
    # Smallest distance between two infinite length lines in 3D space that are defined by 2 points per line
    # x1, y1, z1 are the X,Y,Z values of point 1 defining line 1
    # x2, y2, z2 are the X,Y,Z values of point 2 defining line 1
    # x3, y3, z3 are the X,Y,Z values of point 3 defining line 2
    # x4, y4, z4 are the X,Y,Z values of point 4 defining line 2

    # Forumla
    # Line 1: (x-x1)/a1 = (y-y1)/b1 = (z-z1)/c1
    # Line 2: (x-x2)/a2 = (y-y2)/b2 = (z-z2)/c2
    #
    #            |x2-x1   y2-y1   z2-z1|
    #            |a1      b1      c1   |
    #            |a2      b2      c2   |
    # Distance = ----------------------------------------------------
    #            sqrt((b1c2-b2c1)^2 + (a1c2-a2c1)^2 + (a1b2-a2b1)^2)

    from math import sqrt

    x21 = x2 - x1  # Find a1
    y21 = y2 - y1  # Find b1
    z21 = z2 - z1  # Find c1
    x43 = x4 - x3  # Find a2
    y43 = y4 - y3  # Find b2
    z43 = z4 - z3  # Find c2

    x31 = x3 - x1  # Find x2-x1
    y31 = y3 - y1  # Find y2-y1
    z31 = z3 - z1  # Find z2-z1

    x21X43 = y21 * z43 - z21 * y43  # (b1c2-b2c1)
    y21X43 = z21 * x43 - x21 * z43  # (a1c2-a2c1)
    z21X43 = x21 * y43 - y21 * x43  # (a1b2-a2b1)

    mag21X43 = sqrt(x21X43**2 + y21X43**2 + z21X43**2)  # Find denominator

    return (
        x31 * x21X43 + y31 * y21X43 + z31 * z21X43
    ) / mag21X43  # Find Numerator and divide
