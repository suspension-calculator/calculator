# src/suspension/core/functions/points_angle.py

from math import acos


def point_angle(p1x, p1y, p2x, p2y, p3x, p3y):
    # angle bewteen 3 points, returns positive value
    # p1 is the start point
    # p2 is the vertex point
    # p3 is the end point

    from .distance_2d import dis2D

    l12 = dis2D(p1x, p1y, p2x, p2y)  # distance between points 1 and 2
    l13 = dis2D(p1x, p1y, p3x, p3y)  # distance between points 1 and 3
    l23 = dis2D(p2x, p2y, p3x, p3y)  # distance between points 2 and 3

    return abs(
        acos((l12**2 + l23**2 - l13**2) / (2 * l23 * l12))
    )  # Law of cosines to get angle, absolute value to keep positive.
