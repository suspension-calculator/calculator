def on_axle_movement(hub_Xi, hub_Zi, LA_Xi, LA_Zi, LA_Xf, LA_Zf, angle):
    # Find new wheel center at travel
    #
    # hub_*i is the wheel center at ride
    # UA_*i is the upper axle link point at ride
    # LA_*i is the lower axle link point at ride
    # UA_*f is the upper axle link point at travel
    # LA_*f is the lower axle link point at travel
    #
    # Outputs: hub_*f is the traveled wheel center

    from .rotation import rotate

    LA_Xt = LA_Xf-LA_Xi # Difference in X between LA ride and travel
    LA_Zt = LA_Zf-LA_Zi # Difference in Z between LA ride and travel
    [hub_Xr,hub_Zr] = rotate(LA_Xi,LA_Zi,hub_Xi,hub_Zi,angle) # rotate wheel hub about LA at ride
    hub_Xf = hub_Xr+LA_Xt # move from ride LA to travel LA
    hub_Zf = hub_Zr+LA_Zt # move from ride LA to travel LA

    return hub_Xf,hub_Zf