# src/suspension/core/functions/travel_wheel_2_lca.py


def wheel_2_lca(
    dZ,
    UA_Xi,
    UA_Zi,
    UF_X,
    UF_Z,
    LA_Xi,
    LA_Zi,
    LF_X,
    LF_Z,
    upperLength,
    lowerLength,
    sepAxle,
    sepFrame,
    wheel_Xi,
    wheel_Zi,
):
    # Find LCA Z travel that gives desired wheel Z travel
    #
    # dZ is the movement of the wheel center at travel
    # UA_*i is the intial axle X,Z
    # UF_* is the frame X,Z
    # LA_*i is the intial axle X,Z
    # LF_* is the frame X,Z
    # upperLength is the lenght of the upper link in 2D
    # lowerLength is the lenght of the lower link in 2D
    # sepAxle is the distance from the upper link to the lower link at the axle in 2D
    # sepFrame is the distance from the upper link to the lower link at the frame in 2D
    # wheel_*i is the ride wheel center
    #
    # Outputs: dZi is the control arm travel for a wheel center travel of dZ
    from .link_travel import travel_solve
    from .axle_point_movement import on_axle_movement
    from .pinion_rotation import pinion_angle_change

    dZi = dZ  # set initial LCA travel to desired travel

    while True:
        UA_Xf, UA_Zf, LA_Xf, LA_Zf = travel_solve(
            dZi,
            UA_Xi,
            UA_Zi,
            UF_X,
            UF_Z,
            LA_Xi,
            LA_Zi,
            LF_X,
            LF_Z,
            upperLength,
            lowerLength,
            sepAxle,
            sepFrame,
        )  # get travel points
        angle = pinion_angle_change(
            UA_Xi, UA_Zi, UA_Xf, UA_Zf, LA_Xi, LA_Zi, LA_Xf, LA_Zf
        )
        wheel_Zf = on_axle_movement(
            wheel_Xi, wheel_Zi, LA_Xi, LA_Zi, LA_Xf, LA_Zf, angle
        )[
            1
        ]  # get travel wheel center

        d_WC_z = wheel_Zf - wheel_Zi  # dZ of wheel center from ride
        error = (
            d_WC_z - dZ
        )  # difference between wheel center travel and desired wheel center travel
        if abs(error) < 0.0001:
            break  # once error is low 0.0001", exit loop, loop is exited here so that dZi is at the low error
        dZi = dZi - error  # LCA travel for next loop

    return dZi
