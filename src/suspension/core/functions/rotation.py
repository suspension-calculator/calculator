# src/suspension/core/functions/rotation.py

def rotate(xo,yo,xi,yi,theta):
    # Rotation of point i about o by angle theta (radians) in 2D space
    # xo, yo are the X, Y coordinates of the point being rotated about
    # xi, yi are the X, Y coordinates of the point being rotated
    # Theta is the angle being rotated

    # Points are translated to origin, rotated, then translated back

    from math import cos, sin

    X = (xi - xo) * cos(theta) - (yi - yo) * sin(theta) + xo # find new X coordinate
    Y = (yi - yo) * cos(theta) + (xi - xo) * sin(theta) + yo # find new Y coordinate
    return(X,Y)