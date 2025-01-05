def travel_solve(dZ, UA_Xi, UA_Zi, UF_X, UF_Z, LA_Xi, LA_Zi, LF_X, LF_Z, upperLength, lowerLength, sepAxle, sepFrame):
    # Find axle points for given lower axle Z change
    #
    # dZ is the movement of lower control arm at axle
    # UA_*i is the intial axle X,Z
    # UF_* is the frame X,Z
    # LA_*i is the intial axle X,Z
    # LF_* is the frame X,Z
    # upperLength is the lenght of the upper link in 2D
    # lowerLength is the lenght of the lower link in 2D
    # sepAxle is the distance from the upper link to the lower link at the axle in 2D
    # sepFrame is the distance from the upper link to the lower link at the frame in 2D
    #
    # Outputs: Upper Axle X, Upper Axle Z, Lower Axle X, Lower Axle Z

    from math import cos, sin, asin, acos, pi
    from Functions.distance_2d import dis2D


    LA_Zf = LA_Zi + dZ  # Determine Lower Axle Z
   
    if LA_Xi < LF_X: # Determine if frame is in front of axle
        LA_Xf = LF_X - ((lowerLength ** 2 - (LA_Zf - LF_Z) ** 2) ** 0.5) # calculate X distance between axle and frame on lower link, subtract from frame
    else:
        LA_Xf = LF_X + ((lowerLength ** 2 - (LA_Zf - LF_Z) ** 2) ** 0.5) # calculate X distance between axle and frame on lower link, add to frame

    Angle_LL_Horiz = asin((LF_Z - LA_Zf) / lowerLength) # find the angle between lower link and horizontal
    Length_UF_LAF = dis2D(UF_X, UF_Z, LA_Xf, LA_Zf) # find distance between upper frame and final lower axle
    Angle_LA_Opp_F = acos((lowerLength ** 2 + Length_UF_LAF ** 2 - sepFrame ** 2) / (2 * lowerLength * Length_UF_LAF)) # find angle between lower link and line from lower axle to upper frame
    Angle_LA_Opp_U = acos((sepAxle ** 2 + Length_UF_LAF ** 2 - upperLength ** 2) / (2 * sepAxle * Length_UF_LAF)) # find angle between axle points line and line between from lower axle to upper frame
    Angle_LL_Axle_Mounts = Angle_LA_Opp_F + Angle_LA_Opp_U # find angle between lower link and axle points line
    Angle_Pinion_Line = Angle_LL_Horiz + Angle_LL_Axle_Mounts # find angle between horizontal and axle points line
    Angle_Axle = pi - Angle_Pinion_Line # Find angle axle line is at

    # Upper Axle Z
    UA_Zf = LA_Zf + (sepAxle * sin(Angle_Axle)) # find upper axle Z
    # Upper Axle X
    if UA_Xi < UF_X: # Determine if frame is in front of axle
        UA_Xf = LA_Xf - (sepAxle * cos(Angle_Axle)) # calculate upper axle X
    else:
        UA_Xf = LA_Xf + (sepAxle * cos(Angle_Axle)) # calculate upper axle X

    return(UA_Xf,UA_Zf,LA_Xf,LA_Zf)