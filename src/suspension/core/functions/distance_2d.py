# Functions/distance_2d.py

def dis2D(x1,y1,x2,y2):
    # Distance between 2 points in 2D space
    # x1 is X value of point 1
    # y1 is Y value of point 1
    # x2 is X value of point 2
    # y2 is Y value of point 2

    from math import sqrt

    return(sqrt((x1-x2)**2+(y1-y2)**2))