def pinion_angle_change(UA_Xi, UA_Zi, UA_Xf, UA_Zf, LA_Xi, LA_Zi, LA_Xf, LA_Zf):
    # Find pinion angle change
    #
    # hub_*i is the wheel center at ride
    # UA_*i is the upper axle link point at ride
    # LA_*i is the lower axle link point at ride
    # UA_*f is the upper axle link point at travel
    # LA_*f is the lower axle link point at travel
    #
    # Outputs: hub_*f is the traveled wheel center

    from math import atan2

    ride_angle = atan2((UA_Zi-LA_Zi),(UA_Xi-LA_Xi)) # Angle of line between upper and lower axle points and horizontal at ride
    travel_angle = atan2((UA_Zf-LA_Zf),(UA_Xf-LA_Xf)) # Angle of line between upper and lower axle points and horizontal at travel
    return(travel_angle - ride_angle) # diffenece in angle mount point lines slopes