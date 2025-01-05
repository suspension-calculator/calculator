def SegSep(x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4):
    # Find distance minimum distance between two line segments in 3D space
    # Credit goes to https://math.stackexchange.com/questions/846054/closest-points-on-two-line-segments
    # x1, y1, z1 are the X,Y,Z values of point 1 defining line 1
    # x2, y2, z2 are the X,Y,Z values of point 2 defining line 1
    # x3, y3, z3 are the X,Y,Z values of point 3 defining line 2
    # x4, y4, z4 are the X,Y,Z values of point 4 defining line 2

    from .distance_3d import dis3D

    R1 = (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2 # Find R1^2
    R2 = (x4 - x3) ** 2 + (y4 - y3) ** 2 + (z4 - z3) ** 2 # Find R2^2
    D4321 = (x4 - x3) * (x2 - x1) + (y4 - y3) * (y2 - y1) + (z4 - z3) * (z2 - z1)
    D3121 = (x3 - x1) * (x2 - x1) + (y3 - y1) * (y2 - y1) + (z3 - z1) * (z2 - z1)
    D4331 = (x4 - x3) * (x3 - x1) + (y4 - y3) * (y3 - y1) + (z4 - z3) * (z3 - z1)

    s = (D4321 * D4331 - D3121 * R2) / (D4321 ** 2-R1 * R2);
    t = (D4331 * R1 - D4321 * D3121) / (D4321 ** 2-R1 * R2);

    if 0 <= s <= 1 or 0 <= t <= 1: # Closest distance is on both line segments
        # Find closest points
        x5 = x1 + s * (x2 - x1)
        y5 = y1 + s * (y2 - y1)
        z5 = z1 + s * (z2 - z1)
        x6 = x3 + t * (x4 - x3)
        y6 = y3 + t * (y4 - y3)
        z6 = z3 + t * (z4 - z3)
        # Calculate Distance
        out = dis3D(x5,y5,z5,x6,y6,z6)

    else: # Closeest distance is not on one of the line segments

        D4121 = (x4 - x1) * (x2 - x1) + (y4 - y1) * (y2 - y1) + (z4 - z1) * (z2 - z1)
        D4332 = (x4 - x3) * (x3 - x1) + (y4 - y3) * (y3 - y1) + (z4 - z3) * (z3 - z1)

        # Find S and T values of the 4 point combinations
        s3 = D3121 / R1
        s4 = D4121 / R1
        t1 = -D4331 / R2
        t2 = -D4332 / R2

        if 0 > s3:
            s3 = 0
        elif s3 > 1:
            s3 = 1

        if 0 > s4:
            s4 = 0
        elif s4 > 1:
            s4 = 1

        if 0 > t1:
            t1 = 0
        elif t1 > 1:
            t1 = 1

        if 0 > t2:
            t2 = 0
        elif t2 > 1:
            t2 = 1

        # Find closest point along lines to each of the 4 line segment end points
        x16 = x3 + t1 * (x4 - x3)
        y16 = y3 + t1 * (y4 - y3)
        z16 = z3 + t1 * (z4 - z3)

        x26 = x3 + t2 * (x4 - x3)
        y26 = y3 + t2 * (y4 - y3)
        z26 = z3 + t2 * (z4 - z3)

        x35 = x1 + s3 * (x2 - x1)
        y35 = y1 + s3 * (y2 - y1)
        z35 = z1 + s3 * (z2 - z1)

        x45 = x1 + s4 * (x2 - x1)
        y45 = y1 + s4 * (y2 - y1)
        z45 = z1 + s4 * (z2 - z1)

        # Calculate distances from endpoints to closest point on line
        D1 = dis3D(x16,y16,z16,x1,y1,z1)
        D2 = dis3D(x26,y26,z26,x2,y2,z2)
        D3 = dis3D(x3,y3,z3,x35,y35,z35)
        D4 = dis3D(x4,y4,z4,x45,y45,z45)

        # Find closest of the 4 combinations
        out = min(D1, D2, D3, D4)

    return(out)
