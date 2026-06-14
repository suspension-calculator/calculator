# src/suspension/core/functions/Y_equals_0.py


def ZeroY(x1, y1, z1, x2, y2, z2):
    # Find X and Z cordinates of Y=0
    # x1, y1, z1 are the X,Y,Z values of point 1 defining the line
    # x2, y2, z2 are the X,Y,Z values of point 2 defining the line

    # Find direction vector
    t = -y1 / (y2 - y1)

    X = x1 + (x2 - x1) * t
    Z = z1 + (z2 - z1) * t

    return (X, Z)
