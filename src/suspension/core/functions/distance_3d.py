# src/suspension/core/functions/distance_3d.py

def dis3D(x1,y1,z1,x2,y2,z2):
    # Distance betwwen 2 points in 3D space
    # x1 is X value of point 1
    # y1 is Y value of point 1
    # z1 is Z value of point 1
    # x2 is X value of point 2
    # y2 is Y value of point 2
    # z2 is Z value of point 2

    from math import sqrt
    
    return(sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2))