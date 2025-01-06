# src/suspension/core/functions/line_intersection.py

def LineIntersect(x1,y1,x2,y2,x3,y3,x4,y4):
    # Find intersection of 2 lines in 2D
    # x1, y1, z1 are the X,Y,Z values of point 1 defining line 1
    # x2, y2, z2 are the X,Y,Z values of point 2 defining line 1
    # x3, y3, z3 are the X,Y,Z values of point 3 defining line 2
    # x4, y4, z4 are the X,Y,Z values of point 4 defining line 2

    denom = ((x1 - x2) * (y3 - y4))- ((y1 - y2) * (x3 - x4)) # Calculate divisor
    multi1 = (x1 * y2) - (y1 * x2) # Calculate part of numerator
    multi2 = (x3 * y4) - (y3 * x4) # Calculate part of numerator
    X = (multi1 * (x3 - x4) - (x1 - x2) * multi2) / denom # Calculate X compontent
    Y = (multi1 * (y3 - y4) - (y1 - y2) * multi2) / denom # Calculate Y component
    return(X,Y)