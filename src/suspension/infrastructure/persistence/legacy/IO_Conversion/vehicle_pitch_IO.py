# src/suspension/io/IO_Conversion/vehicle_pitch_IO.py


def input_processing_vehicle_pitch():
    from suspension.io import inputs
    from suspension.io.variables import constant, S
    from suspension.core.functions.unit_conversion import (
        mm2in,
    )
    from math import radians

    # degree to rad conversion

    constant.pitch.slope = radians(inputs.V.pitch_slope)
    constant.pitch.acceleration = inputs.V.pitch_acceleration * 1
    constant.pitch.drive_bias = inputs.V.pitch_drive_bias * 1
    constant.pitch.brake_bias = inputs.V.pitch_brake_bias * 1

    if S.units == "metric":
        # if metric convert all inputs to sae and set variables
        constant.F.pitch_travel = mm2in(inputs.F.pitch_travel)
        constant.R.pitch_travel = mm2in(inputs.R.pitch_travel)

    else:
        # set variables
        constant.F.pitch_travel = inputs.F.pitch_travel * 1
        constant.R.pitch_travel = inputs.R.pitch_travel * 1


def output_processing_vehicle_pitch():
    from suspension.io import outputs
    from suspension.io.variables import constant, S
    from suspension.core.functions.unit_conversion import (
        in2mm,
    )
    from math import degrees, atan

    outputs.Pitch.load_bias = constant.pitch.load_bias * 1

    temp = 0  # User inputted
    outputs.Pitch.User_Input.Angle = constant.pitch.angle[temp] * 1
    outputs.Pitch.User_Input.Body_Roll_Axis = degrees(
        atan(constant.pitch.body_roll_slope_dpd[temp])
    )
    outputs.Pitch.User_Input.F.Anti_Dive = constant.pitch.F.anti_dive[temp] * 1
    outputs.Pitch.User_Input.F.Anti_Lift = constant.pitch.F.anti_lift[temp] * 1
    outputs.Pitch.User_Input.F.Roll_Slope = degrees(
        atan(constant.pitch.F.roll_slope_dpd[temp])
    )
    outputs.Pitch.User_Input.R.Anti_Squat = constant.pitch.R.anti_squat[temp] * 1
    outputs.Pitch.User_Input.R.Anti_Lift = constant.pitch.R.anti_lift[temp] * 1
    outputs.Pitch.User_Input.R.Roll_Slope = degrees(
        atan(constant.pitch.R.roll_slope_dpd[temp])
    )

    temp = 1  # full front
    outputs.Pitch.Full_Front.Angle = constant.pitch.angle[temp] * 1
    outputs.Pitch.Full_Front.Body_Roll_Axis = degrees(
        atan(constant.pitch.body_roll_slope_dpd[temp])
    )
    outputs.Pitch.Full_Front.F.Anti_Dive = constant.pitch.F.anti_dive[temp] * 1
    outputs.Pitch.Full_Front.F.Anti_Lift = constant.pitch.F.anti_lift[temp] * 1
    outputs.Pitch.Full_Front.F.Roll_Slope = degrees(
        atan(constant.pitch.F.roll_slope_dpd[temp])
    )
    outputs.Pitch.Full_Front.R.Anti_Squat = constant.pitch.R.anti_squat[temp] * 1
    outputs.Pitch.Full_Front.R.Anti_Lift = constant.pitch.R.anti_lift[temp] * 1
    outputs.Pitch.Full_Front.R.Roll_Slope = degrees(
        atan(constant.pitch.R.roll_slope_dpd[temp])
    )

    temp = 2  # half front
    outputs.Pitch.Half_Front.Angle = constant.pitch.angle[temp] * 1
    outputs.Pitch.Half_Front.Body_Roll_Axis = degrees(
        atan(constant.pitch.body_roll_slope_dpd[temp])
    )
    outputs.Pitch.Half_Front.F.Anti_Dive = constant.pitch.F.anti_dive[temp] * 1
    outputs.Pitch.Half_Front.F.Anti_Lift = constant.pitch.F.anti_lift[temp] * 1
    outputs.Pitch.Half_Front.F.Roll_Slope = degrees(
        atan(constant.pitch.F.roll_slope_dpd[temp])
    )
    outputs.Pitch.Half_Front.R.Anti_Squat = constant.pitch.R.anti_squat[temp]
    outputs.Pitch.Half_Front.R.Anti_Lift = constant.pitch.R.anti_lift[temp]
    outputs.Pitch.Half_Front.R.Roll_Slope = degrees(
        atan(constant.pitch.R.roll_slope_dpd[temp])
    )

    temp = 3  # half rear
    outputs.Pitch.Half_Rear.Angle = constant.pitch.angle[temp] * 1
    outputs.Pitch.Half_Rear.Body_Roll_Axis = degrees(
        atan(constant.pitch.body_roll_slope_dpd[temp])
    )
    outputs.Pitch.Half_Rear.F.Anti_Dive = constant.pitch.F.anti_dive[temp] * 1
    outputs.Pitch.Half_Rear.F.Anti_Lift = constant.pitch.F.anti_lift[temp] * 1
    outputs.Pitch.Half_Rear.F.Roll_Slope = degrees(
        atan(constant.pitch.F.roll_slope_dpd[temp])
    )
    outputs.Pitch.Half_Rear.R.Anti_Squat = constant.pitch.R.anti_squat[temp] * 1
    outputs.Pitch.Half_Rear.R.Anti_Lift = constant.pitch.R.anti_lift[temp] * 1
    outputs.Pitch.Half_Rear.R.Roll_Slope = degrees(
        atan(constant.pitch.R.roll_slope_dpd[temp])
    )

    temp = 4  # full rear
    outputs.Pitch.Full_Rear.Angle = constant.pitch.angle[temp] * 1
    outputs.Pitch.Full_Rear.Body_Roll_Axis = degrees(
        atan(constant.pitch.body_roll_slope_dpd[temp])
    )
    outputs.Pitch.Full_Rear.F.Anti_Dive = constant.pitch.F.anti_dive[temp] * 1
    outputs.Pitch.Full_Rear.F.Anti_Lift = constant.pitch.F.anti_lift[temp] * 1
    outputs.Pitch.Full_Rear.F.Roll_Slope = degrees(
        atan(constant.pitch.F.roll_slope_dpd[temp])
    )
    outputs.Pitch.Full_Rear.R.Anti_Squat = constant.pitch.R.anti_squat[temp] * 1
    outputs.Pitch.Full_Rear.R.Anti_Lift = constant.pitch.R.anti_lift[temp] * 1
    outputs.Pitch.Full_Rear.R.Roll_Slope = degrees(
        atan(constant.pitch.R.roll_slope_dpd[temp])
    )

    temp = 5  # full up
    outputs.Pitch.Full_Up.Angle = constant.pitch.angle[temp] * 1
    outputs.Pitch.Full_Up.Body_Roll_Axis = degrees(
        atan(constant.pitch.body_roll_slope_dpd[temp])
    )
    outputs.Pitch.Full_Up.F.Anti_Dive = constant.pitch.F.anti_dive[temp] * 1
    outputs.Pitch.Full_Up.F.Anti_Lift = constant.pitch.F.anti_lift[temp] * 1
    outputs.Pitch.Full_Up.F.Roll_Slope = degrees(
        atan(constant.pitch.F.roll_slope_dpd[temp])
    )
    outputs.Pitch.Full_Up.R.Anti_Squat = constant.pitch.R.anti_squat[temp] * 1
    outputs.Pitch.Full_Up.R.Anti_Lift = constant.pitch.R.anti_lift[temp] * 1
    outputs.Pitch.Full_Up.R.Roll_Slope = degrees(
        atan(constant.pitch.R.roll_slope_dpd[temp])
    )

    temp = 6  # full down
    outputs.Pitch.Full_Down.Angle = constant.pitch.angle[temp] * 1
    outputs.Pitch.Full_Down.Body_Roll_Axis = degrees(
        atan(constant.pitch.body_roll_slope_dpd[temp])
    )
    outputs.Pitch.Full_Down.F.Anti_Dive = constant.pitch.F.anti_dive[temp] * 1
    outputs.Pitch.Full_Down.F.Anti_Lift = constant.pitch.F.anti_lift[temp] * 1
    outputs.Pitch.Full_Down.F.Roll_Slope = degrees(
        atan(constant.pitch.F.roll_slope_dpd[temp])
    )
    outputs.Pitch.Full_Down.R.Anti_Squat = constant.pitch.R.anti_squat[temp] * 1
    outputs.Pitch.Full_Down.R.Anti_Lift = constant.pitch.R.anti_lift[temp] * 1
    outputs.Pitch.Full_Down.R.Roll_Slope = degrees(
        atan(constant.pitch.R.roll_slope_dpd[temp])
    )

    if S.units == "metric":
        # if metric convert all outputs to metric
        outputs.Pitch.front_travel_est = in2mm(constant.pitch.front_travel_est)
        outputs.Pitch.rear_travel_est = in2mm(constant.pitch.rear_travel_est)

        temp = 0  # user inputted travel
        outputs.Pitch.User_Input.Front_Travel = in2mm(constant.pitch.F.travel[temp])
        outputs.Pitch.User_Input.Rear_Travel = in2mm(constant.pitch.R.travel[temp])
        outputs.Pitch.User_Input.Sprung_Mass_CG = in2mm(
            constant.pitch.sprung_mass_CG[temp]
        )

        outputs.Pitch.User_Input.F.Roll_Center = in2mm(
            constant.pitch.F.roll_center[temp]
        )
        outputs.Pitch.User_Input.F.UA = in2mm(constant.pitch.F.UA[temp])
        outputs.Pitch.User_Input.F.LA = in2mm(constant.pitch.F.LA[temp])
        outputs.Pitch.User_Input.F.UF = in2mm(constant.pitch.F.UF[temp])
        outputs.Pitch.User_Input.F.LF = in2mm(constant.pitch.F.LF[temp])
        outputs.Pitch.User_Input.F.PA = in2mm(constant.pitch.F.PA[temp])
        outputs.Pitch.User_Input.F.PF = in2mm(constant.pitch.F.PF[temp])
        outputs.Pitch.User_Input.F.Hub = in2mm(constant.pitch.F.hub[temp])

        outputs.Pitch.User_Input.R.Roll_Center = in2mm(
            constant.pitch.R.roll_center[temp]
        )
        outputs.Pitch.User_Input.R.UA = in2mm(constant.pitch.R.UA[temp])
        outputs.Pitch.User_Input.R.LA = in2mm(constant.pitch.R.LA[temp])
        outputs.Pitch.User_Input.R.UF = in2mm(constant.pitch.R.UF[temp])
        outputs.Pitch.User_Input.R.LF = in2mm(constant.pitch.R.LF[temp])
        outputs.Pitch.User_Input.R.PA = in2mm(constant.pitch.R.PA[temp])
        outputs.Pitch.User_Input.R.PF = in2mm(constant.pitch.R.PF[temp])
        outputs.Pitch.User_Input.R.Hub = in2mm(constant.pitch.R.hub[temp])

        temp = 1  # full front
        outputs.Pitch.Full_Front.Front_Travel = in2mm(constant.pitch.F.travel[temp])
        outputs.Pitch.Full_Front.Rear_Travel = in2mm(constant.pitch.R.travel[temp])
        outputs.Pitch.Full_Front.Sprung_Mass_CG = in2mm(
            constant.pitch.sprung_mass_CG[temp]
        )

        outputs.Pitch.Full_Front.F.Roll_Center = in2mm(
            constant.pitch.F.roll_center[temp]
        )
        outputs.Pitch.Full_Front.F.UA = in2mm(constant.pitch.F.UA[temp])
        outputs.Pitch.Full_Front.F.LA = in2mm(constant.pitch.F.LA[temp])
        outputs.Pitch.Full_Front.F.UF = in2mm(constant.pitch.F.UF[temp])
        outputs.Pitch.Full_Front.F.LF = in2mm(constant.pitch.F.LF[temp])
        outputs.Pitch.Full_Front.F.PA = in2mm(constant.pitch.F.PA[temp])
        outputs.Pitch.Full_Front.F.PF = in2mm(constant.pitch.F.PF[temp])
        outputs.Pitch.Full_Front.F.Hub = in2mm(constant.pitch.F.hub[temp])

        outputs.Pitch.Full_Front.R.Roll_Center = in2mm(
            constant.pitch.R.roll_center[temp]
        )
        outputs.Pitch.Full_Front.R.UA = in2mm(constant.pitch.R.UA[temp])
        outputs.Pitch.Full_Front.R.LA = in2mm(constant.pitch.R.LA[temp])
        outputs.Pitch.Full_Front.R.UF = in2mm(constant.pitch.R.UF[temp])
        outputs.Pitch.Full_Front.R.LF = in2mm(constant.pitch.R.LF[temp])
        outputs.Pitch.Full_Front.R.PA = in2mm(constant.pitch.R.PA[temp])
        outputs.Pitch.Full_Front.R.PF = in2mm(constant.pitch.R.PF[temp])
        outputs.Pitch.Full_Front.R.Hub = in2mm(constant.pitch.R.hub[temp])

        temp = 2  # half front
        outputs.Pitch.Half_Front.Front_Travel = in2mm(constant.pitch.F.travel[temp])
        outputs.Pitch.Half_Front.Rear_Travel = in2mm(constant.pitch.R.travel[temp])
        outputs.Pitch.Half_Front.Sprung_Mass_CG = in2mm(
            constant.pitch.sprung_mass_CG[temp]
        )

        outputs.Pitch.Half_Front.F.Roll_Center = in2mm(
            constant.pitch.F.roll_center[temp]
        )
        outputs.Pitch.Half_Front.F.UA = in2mm(constant.pitch.F.UA[temp])
        outputs.Pitch.Half_Front.F.LA = in2mm(constant.pitch.F.LA[temp])
        outputs.Pitch.Half_Front.F.UF = in2mm(constant.pitch.F.UF[temp])
        outputs.Pitch.Half_Front.F.LF = in2mm(constant.pitch.F.LF[temp])
        outputs.Pitch.Half_Front.F.PA = in2mm(constant.pitch.F.PA[temp])
        outputs.Pitch.Half_Front.F.PF = in2mm(constant.pitch.F.PF[temp])
        outputs.Pitch.Half_Front.F.Hub = in2mm(constant.pitch.F.hub[temp])

        outputs.Pitch.Half_Front.R.Roll_Center = in2mm(
            constant.pitch.R.roll_center[temp]
        )
        outputs.Pitch.Half_Front.R.UA = in2mm(constant.pitch.R.UA[temp])
        outputs.Pitch.Half_Front.R.LA = in2mm(constant.pitch.R.LA[temp])
        outputs.Pitch.Half_Front.R.UF = in2mm(constant.pitch.R.UF[temp])
        outputs.Pitch.Half_Front.R.LF = in2mm(constant.pitch.R.LF[temp])
        outputs.Pitch.Half_Front.R.PA = in2mm(constant.pitch.R.PA[temp])
        outputs.Pitch.Half_Front.R.PF = in2mm(constant.pitch.R.PF[temp])
        outputs.Pitch.Half_Front.R.Hub = in2mm(constant.pitch.R.hub[temp])

        temp = 3  # half rear
        outputs.Pitch.Half_Rear.Front_Travel = in2mm(constant.pitch.F.travel[temp])
        outputs.Pitch.Half_Rear.Rear_Travel = in2mm(constant.pitch.R.travel[temp])
        outputs.Pitch.Half_Rear.Sprung_Mass_CG = in2mm(
            constant.pitch.sprung_mass_CG[temp]
        )

        outputs.Pitch.Half_Rear.F.Roll_Center = in2mm(
            constant.pitch.F.roll_center[temp]
        )
        outputs.Pitch.Half_Rear.F.UA = in2mm(constant.pitch.F.UA[temp])
        outputs.Pitch.Half_Rear.F.LA = in2mm(constant.pitch.F.LA[temp])
        outputs.Pitch.Half_Rear.F.UF = in2mm(constant.pitch.F.UF[temp])
        outputs.Pitch.Half_Rear.F.LF = in2mm(constant.pitch.F.LF[temp])
        outputs.Pitch.Half_Rear.F.PA = in2mm(constant.pitch.F.PA[temp])
        outputs.Pitch.Half_Rear.F.PF = in2mm(constant.pitch.F.PF[temp])
        outputs.Pitch.Half_Rear.F.Hub = in2mm(constant.pitch.F.hub[temp])

        outputs.Pitch.Half_Rear.R.Roll_Center = in2mm(
            constant.pitch.R.roll_center[temp]
        )
        outputs.Pitch.Half_Rear.R.UA = in2mm(constant.pitch.R.UA[temp])
        outputs.Pitch.Half_Rear.R.LA = in2mm(constant.pitch.R.LA[temp])
        outputs.Pitch.Half_Rear.R.UF = in2mm(constant.pitch.R.UF[temp])
        outputs.Pitch.Half_Rear.R.LF = in2mm(constant.pitch.R.LF[temp])
        outputs.Pitch.Half_Rear.R.PA = in2mm(constant.pitch.R.PA[temp])
        outputs.Pitch.Half_Rear.R.PF = in2mm(constant.pitch.R.PF[temp])
        outputs.Pitch.Half_Rear.R.Hub = in2mm(constant.pitch.R.hub[temp])

        temp = 4  # full front
        outputs.Pitch.Full_Rear.Front_Travel = in2mm(constant.pitch.F.travel[temp])
        outputs.Pitch.Full_Rear.Rear_Travel = in2mm(constant.pitch.R.travel[temp])
        outputs.Pitch.Full_Rear.Sprung_Mass_CG = in2mm(
            constant.pitch.sprung_mass_CG[temp]
        )

        outputs.Pitch.Full_Rear.F.Roll_Center = in2mm(
            constant.pitch.F.roll_center[temp]
        )
        outputs.Pitch.Full_Rear.F.UA = in2mm(constant.pitch.F.UA[temp])
        outputs.Pitch.Full_Rear.F.LA = in2mm(constant.pitch.F.LA[temp])
        outputs.Pitch.Full_Rear.F.UF = in2mm(constant.pitch.F.UF[temp])
        outputs.Pitch.Full_Rear.F.LF = in2mm(constant.pitch.F.LF[temp])
        outputs.Pitch.Full_Rear.F.PA = in2mm(constant.pitch.F.PA[temp])
        outputs.Pitch.Full_Rear.F.PF = in2mm(constant.pitch.F.PF[temp])
        outputs.Pitch.Full_Rear.F.Hub = in2mm(constant.pitch.F.hub[temp])

        outputs.Pitch.Full_Rear.R.Roll_Center = in2mm(
            constant.pitch.R.roll_center[temp]
        )
        outputs.Pitch.Full_Rear.R.UA = in2mm(constant.pitch.R.UA[temp])
        outputs.Pitch.Full_Rear.R.LA = in2mm(constant.pitch.R.LA[temp])
        outputs.Pitch.Full_Rear.R.UF = in2mm(constant.pitch.R.UF[temp])
        outputs.Pitch.Full_Rear.R.LF = in2mm(constant.pitch.R.LF[temp])
        outputs.Pitch.Full_Rear.R.PA = in2mm(constant.pitch.R.PA[temp])
        outputs.Pitch.Full_Rear.R.PF = in2mm(constant.pitch.R.PF[temp])
        outputs.Pitch.Full_Rear.R.Hub = in2mm(constant.pitch.R.hub[temp])

        temp = 5  # full up
        outputs.Pitch.Full_Up.Front_Travel = in2mm(constant.pitch.F.travel[temp])
        outputs.Pitch.Full_Up.Rear_Travel = in2mm(constant.pitch.R.travel[temp])
        outputs.Pitch.Full_Up.Sprung_Mass_CG = in2mm(
            constant.pitch.sprung_mass_CG[temp]
        )

        outputs.Pitch.Full_Up.F.Roll_Center = in2mm(constant.pitch.F.roll_center[temp])
        outputs.Pitch.Full_Up.F.UA = in2mm(constant.pitch.F.UA[temp])
        outputs.Pitch.Full_Up.F.LA = in2mm(constant.pitch.F.LA[temp])
        outputs.Pitch.Full_Up.F.UF = in2mm(constant.pitch.F.UF[temp])
        outputs.Pitch.Full_Up.F.LF = in2mm(constant.pitch.F.LF[temp])
        outputs.Pitch.Full_Up.F.PA = in2mm(constant.pitch.F.PA[temp])
        outputs.Pitch.Full_Up.F.PF = in2mm(constant.pitch.F.PF[temp])
        outputs.Pitch.Full_Up.F.Hub = in2mm(constant.pitch.F.hub[temp])

        outputs.Pitch.Full_Up.R.Roll_Center = in2mm(constant.pitch.R.roll_center[temp])
        outputs.Pitch.Full_Up.R.UA = in2mm(constant.pitch.R.UA[temp])
        outputs.Pitch.Full_Up.R.LA = in2mm(constant.pitch.R.LA[temp])
        outputs.Pitch.Full_Up.R.UF = in2mm(constant.pitch.R.UF[temp])
        outputs.Pitch.Full_Up.R.LF = in2mm(constant.pitch.R.LF[temp])
        outputs.Pitch.Full_Up.R.PA = in2mm(constant.pitch.R.PA[temp])
        outputs.Pitch.Full_Up.R.PF = in2mm(constant.pitch.R.PF[temp])
        outputs.Pitch.Full_Up.R.Hub = in2mm(constant.pitch.R.hub[temp])

        temp = 6  # full down
        outputs.Pitch.Full_Down.Front_Travel = in2mm(constant.pitch.F.travel[temp])
        outputs.Pitch.Full_Down.Rear_Travel = in2mm(constant.pitch.R.travel[temp])
        outputs.Pitch.Full_Down.Sprung_Mass_CG = in2mm(
            constant.pitch.sprung_mass_CG[temp]
        )

        outputs.Pitch.Full_Down.F.Roll_Center = in2mm(
            constant.pitch.F.roll_center[temp]
        )
        outputs.Pitch.Full_Down.F.UA = in2mm(constant.pitch.F.UA[temp])
        outputs.Pitch.Full_Down.F.LA = in2mm(constant.pitch.F.LA[temp])
        outputs.Pitch.Full_Down.F.UF = in2mm(constant.pitch.F.UF[temp])
        outputs.Pitch.Full_Down.F.LF = in2mm(constant.pitch.F.LF[temp])
        outputs.Pitch.Full_Down.F.PA = in2mm(constant.pitch.F.PA[temp])
        outputs.Pitch.Full_Down.F.PF = in2mm(constant.pitch.F.PF[temp])
        outputs.Pitch.Full_Down.F.Hub = in2mm(constant.pitch.F.hub[temp])

        outputs.Pitch.Full_Down.R.Roll_Center = in2mm(
            constant.pitch.R.roll_center[temp]
        )
        outputs.Pitch.Full_Down.R.UA = in2mm(constant.pitch.R.UA[temp])
        outputs.Pitch.Full_Down.R.LA = in2mm(constant.pitch.R.LA[temp])
        outputs.Pitch.Full_Down.R.UF = in2mm(constant.pitch.R.UF[temp])
        outputs.Pitch.Full_Down.R.LF = in2mm(constant.pitch.R.LF[temp])
        outputs.Pitch.Full_Down.R.PA = in2mm(constant.pitch.R.PA[temp])
        outputs.Pitch.Full_Down.R.PF = in2mm(constant.pitch.R.PF[temp])
        outputs.Pitch.Full_Down.R.Hub = in2mm(constant.pitch.R.hub[temp])

    else:
        outputs.Pitch.front_travel_est = constant.pitch.front_travel_est
        outputs.Pitch.rear_travel_est = constant.pitch.rear_travel_est

        temp = 0  # user inputted travel
        outputs.Pitch.User_Input.Front_Travel = constant.pitch.F.travel[temp] * 1
        outputs.Pitch.User_Input.Rear_Travel = constant.pitch.R.travel[temp] * 1
        outputs.Pitch.User_Input.Sprung_Mass_CG = (
            constant.pitch.sprung_mass_CG[temp] * 1
        )
        outputs.Pitch.User_Input.F.Roll_Center = constant.pitch.F.roll_center[temp] * 1
        outputs.Pitch.User_Input.F.UA = constant.pitch.F.UA[temp] * 1
        outputs.Pitch.User_Input.F.LA = constant.pitch.F.LA[temp] * 1
        outputs.Pitch.User_Input.F.UF = constant.pitch.F.UF[temp] * 1
        outputs.Pitch.User_Input.F.LF = constant.pitch.F.LF[temp] * 1
        outputs.Pitch.User_Input.F.PA = constant.pitch.F.PA[temp] * 1
        outputs.Pitch.User_Input.F.PF = constant.pitch.F.PF[temp] * 1
        outputs.Pitch.User_Input.F.Hub = constant.pitch.F.hub[temp] * 1
        outputs.Pitch.User_Input.R.Roll_Center = constant.pitch.R.roll_center[temp] * 1
        outputs.Pitch.User_Input.R.UA = constant.pitch.R.UA[temp] * 1
        outputs.Pitch.User_Input.R.LA = constant.pitch.R.LA[temp] * 1
        outputs.Pitch.User_Input.R.UF = constant.pitch.R.UF[temp] * 1
        outputs.Pitch.User_Input.R.LF = constant.pitch.R.LF[temp] * 1
        outputs.Pitch.User_Input.R.PA = constant.pitch.R.PA[temp] * 1
        outputs.Pitch.User_Input.R.PF = constant.pitch.R.PF[temp] * 1
        outputs.Pitch.User_Input.R.Hub = constant.pitch.R.hub[temp] * 1

        temp = 1  # full front
        outputs.Pitch.Full_Front.Front_Travel = constant.pitch.F.travel[temp] * 1
        outputs.Pitch.Full_Front.Rear_Travel = constant.pitch.R.travel[temp] * 1
        outputs.Pitch.Full_Front.Sprung_Mass_CG = (
            constant.pitch.sprung_mass_CG[temp] * 1
        )
        outputs.Pitch.Full_Front.F.Roll_Center = constant.pitch.F.roll_center[temp] * 1
        outputs.Pitch.Full_Front.F.UA = constant.pitch.F.UA[temp] * 1
        outputs.Pitch.Full_Front.F.LA = constant.pitch.F.LA[temp] * 1
        outputs.Pitch.Full_Front.F.UF = constant.pitch.F.UF[temp] * 1
        outputs.Pitch.Full_Front.F.LF = constant.pitch.F.LF[temp] * 1
        outputs.Pitch.Full_Front.F.PA = constant.pitch.F.PA[temp] * 1
        outputs.Pitch.Full_Front.F.PF = constant.pitch.F.PF[temp] * 1
        outputs.Pitch.Full_Front.F.Hub = constant.pitch.F.hub[temp] * 1
        outputs.Pitch.Full_Front.R.Roll_Center = constant.pitch.R.roll_center[temp] * 1
        outputs.Pitch.Full_Front.R.UA = constant.pitch.R.UA[temp] * 1
        outputs.Pitch.Full_Front.R.LA = constant.pitch.R.LA[temp] * 1
        outputs.Pitch.Full_Front.R.UF = constant.pitch.R.UF[temp] * 1
        outputs.Pitch.Full_Front.R.LF = constant.pitch.R.LF[temp] * 1
        outputs.Pitch.Full_Front.R.PA = constant.pitch.R.PA[temp] * 1
        outputs.Pitch.Full_Front.R.PF = constant.pitch.R.PF[temp] * 1
        outputs.Pitch.Full_Front.R.Hub = constant.pitch.R.hub[temp] * 1

        temp = 2  # half front
        outputs.Pitch.Half_Front.Front_Travel = constant.pitch.F.travel[temp] * 1
        outputs.Pitch.Half_Front.Rear_Travel = constant.pitch.R.travel[temp] * 1
        outputs.Pitch.Half_Front.Sprung_Mass_CG = (
            constant.pitch.sprung_mass_CG[temp] * 1
        )
        outputs.Pitch.Half_Front.F.Roll_Center = constant.pitch.F.roll_center[temp] * 1
        outputs.Pitch.Half_Front.F.UA = constant.pitch.F.UA[temp] * 1
        outputs.Pitch.Half_Front.F.LA = constant.pitch.F.LA[temp] * 1
        outputs.Pitch.Half_Front.F.UF = constant.pitch.F.UF[temp] * 1
        outputs.Pitch.Half_Front.F.LF = constant.pitch.F.LF[temp] * 1
        outputs.Pitch.Half_Front.F.PA = constant.pitch.F.PA[temp] * 1
        outputs.Pitch.Half_Front.F.PF = constant.pitch.F.PF[temp] * 1
        outputs.Pitch.Half_Front.F.Hub = constant.pitch.F.hub[temp] * 1
        outputs.Pitch.Half_Front.R.Roll_Center = constant.pitch.R.roll_center[temp] * 1
        outputs.Pitch.Half_Front.R.UA = constant.pitch.R.UA[temp] * 1
        outputs.Pitch.Half_Front.R.LA = constant.pitch.R.LA[temp] * 1
        outputs.Pitch.Half_Front.R.UF = constant.pitch.R.UF[temp] * 1
        outputs.Pitch.Half_Front.R.LF = constant.pitch.R.LF[temp] * 1
        outputs.Pitch.Half_Front.R.PA = constant.pitch.R.PA[temp] * 1
        outputs.Pitch.Half_Front.R.PF = constant.pitch.R.PF[temp] * 1
        outputs.Pitch.Half_Front.R.Hub = constant.pitch.R.hub[temp] * 1

        temp = 3  # half rear
        outputs.Pitch.Half_Rear.Front_Travel = constant.pitch.F.travel[temp] * 1
        outputs.Pitch.Half_Rear.Rear_Travel = constant.pitch.R.travel[temp] * 1
        outputs.Pitch.Half_Rear.Sprung_Mass_CG = constant.pitch.sprung_mass_CG[temp] * 1
        outputs.Pitch.Half_Rear.F.Roll_Center = constant.pitch.F.roll_center[temp] * 1
        outputs.Pitch.Half_Rear.F.UA = constant.pitch.F.UA[temp] * 1
        outputs.Pitch.Half_Rear.F.LA = constant.pitch.F.LA[temp] * 1
        outputs.Pitch.Half_Rear.F.UF = constant.pitch.F.UF[temp] * 1
        outputs.Pitch.Half_Rear.F.LF = constant.pitch.F.LF[temp] * 1
        outputs.Pitch.Half_Rear.F.PA = constant.pitch.F.PA[temp] * 1
        outputs.Pitch.Half_Rear.F.PF = constant.pitch.F.PF[temp] * 1
        outputs.Pitch.Half_Rear.F.Hub = constant.pitch.F.hub[temp] * 1
        outputs.Pitch.Half_Rear.R.Roll_Center = constant.pitch.R.roll_center[temp] * 1
        outputs.Pitch.Half_Rear.R.UA = constant.pitch.R.UA[temp] * 1
        outputs.Pitch.Half_Rear.R.LA = constant.pitch.R.LA[temp] * 1
        outputs.Pitch.Half_Rear.R.UF = constant.pitch.R.UF[temp] * 1
        outputs.Pitch.Half_Rear.R.LF = constant.pitch.R.LF[temp] * 1
        outputs.Pitch.Half_Rear.R.PA = constant.pitch.R.PA[temp] * 1
        outputs.Pitch.Half_Rear.R.PF = constant.pitch.R.PF[temp] * 1
        outputs.Pitch.Half_Rear.R.Hub = constant.pitch.R.hub[temp] * 1

        temp = 4  # full rear
        outputs.Pitch.Full_Rear.Front_Travel = constant.pitch.F.travel[temp] * 1
        outputs.Pitch.Full_Rear.Rear_Travel = constant.pitch.R.travel[temp] * 1
        outputs.Pitch.Full_Rear.Sprung_Mass_CG = constant.pitch.sprung_mass_CG[temp] * 1
        outputs.Pitch.Full_Rear.F.Roll_Center = constant.pitch.F.roll_center[temp] * 1
        outputs.Pitch.Full_Rear.F.UA = constant.pitch.F.UA[temp] * 1
        outputs.Pitch.Full_Rear.F.LA = constant.pitch.F.LA[temp] * 1
        outputs.Pitch.Full_Rear.F.UF = constant.pitch.F.UF[temp] * 1
        outputs.Pitch.Full_Rear.F.LF = constant.pitch.F.LF[temp] * 1
        outputs.Pitch.Full_Rear.F.PA = constant.pitch.F.PA[temp] * 1
        outputs.Pitch.Full_Rear.F.PF = constant.pitch.F.PF[temp] * 1
        outputs.Pitch.Full_Rear.F.Hub = constant.pitch.F.hub[temp] * 1
        outputs.Pitch.Full_Rear.R.Roll_Center = constant.pitch.R.roll_center[temp] * 1
        outputs.Pitch.Full_Rear.R.UA = constant.pitch.R.UA[temp] * 1
        outputs.Pitch.Full_Rear.R.LA = constant.pitch.R.LA[temp] * 1
        outputs.Pitch.Full_Rear.R.UF = constant.pitch.R.UF[temp] * 1
        outputs.Pitch.Full_Rear.R.LF = constant.pitch.R.LF[temp] * 1
        outputs.Pitch.Full_Rear.R.PA = constant.pitch.R.PA[temp] * 1
        outputs.Pitch.Full_Rear.R.PF = constant.pitch.R.PF[temp] * 1
        outputs.Pitch.Full_Rear.R.Hub = constant.pitch.R.hub[temp] * 1

        temp = 5  # Full up
        outputs.Pitch.Full_Up.Front_Travel = constant.pitch.F.travel[temp] * 1
        outputs.Pitch.Full_Up.Rear_Travel = constant.pitch.R.travel[temp] * 1
        outputs.Pitch.Full_Up.Sprung_Mass_CG = constant.pitch.sprung_mass_CG[temp] * 1
        outputs.Pitch.Full_Up.F.Roll_Center = constant.pitch.F.roll_center[temp] * 1
        outputs.Pitch.Full_Up.F.UA = constant.pitch.F.UA[temp] * 1
        outputs.Pitch.Full_Up.F.LA = constant.pitch.F.LA[temp] * 1
        outputs.Pitch.Full_Up.F.UF = constant.pitch.F.UF[temp] * 1
        outputs.Pitch.Full_Up.F.LF = constant.pitch.F.LF[temp] * 1
        outputs.Pitch.Full_Up.F.PA = constant.pitch.F.PA[temp] * 1
        outputs.Pitch.Full_Up.F.PF = constant.pitch.F.PF[temp] * 1
        outputs.Pitch.Full_Up.F.Hub = constant.pitch.F.hub[temp] * 1
        outputs.Pitch.Full_Up.R.Roll_Center = constant.pitch.R.roll_center[temp] * 1
        outputs.Pitch.Full_Up.R.UA = constant.pitch.R.UA[temp] * 1
        outputs.Pitch.Full_Up.R.LA = constant.pitch.R.LA[temp] * 1
        outputs.Pitch.Full_Up.R.UF = constant.pitch.R.UF[temp] * 1
        outputs.Pitch.Full_Up.R.LF = constant.pitch.R.LF[temp] * 1
        outputs.Pitch.Full_Up.R.PA = constant.pitch.R.PA[temp] * 1
        outputs.Pitch.Full_Up.R.PF = constant.pitch.R.PF[temp] * 1
        outputs.Pitch.Full_Up.R.Hub = constant.pitch.R.hub[temp] * 1

        temp = 6  # full down
        outputs.Pitch.Full_Down.Front_Travel = constant.pitch.F.travel[temp] * 1
        outputs.Pitch.Full_Down.Rear_Travel = constant.pitch.R.travel[temp] * 1
        outputs.Pitch.Full_Down.Sprung_Mass_CG = constant.pitch.sprung_mass_CG[temp] * 1
        outputs.Pitch.Full_Down.F.Roll_Center = constant.pitch.F.roll_center[temp] * 1
        outputs.Pitch.Full_Down.F.UA = constant.pitch.F.UA[temp] * 1
        outputs.Pitch.Full_Down.F.LA = constant.pitch.F.LA[temp] * 1
        outputs.Pitch.Full_Down.F.UF = constant.pitch.F.UF[temp] * 1
        outputs.Pitch.Full_Down.F.LF = constant.pitch.F.LF[temp] * 1
        outputs.Pitch.Full_Down.F.PA = constant.pitch.F.PA[temp] * 1
        outputs.Pitch.Full_Down.F.PF = constant.pitch.F.PF[temp] * 1
        outputs.Pitch.Full_Down.F.Hub = constant.pitch.F.hub[temp] * 1
        outputs.Pitch.Full_Down.R.Roll_Center = constant.pitch.R.roll_center[temp] * 1
        outputs.Pitch.Full_Down.R.UA = constant.pitch.R.UA[temp] * 1
        outputs.Pitch.Full_Down.R.LA = constant.pitch.R.LA[temp] * 1
        outputs.Pitch.Full_Down.R.UF = constant.pitch.R.UF[temp] * 1
        outputs.Pitch.Full_Down.R.LF = constant.pitch.R.LF[temp] * 1
        outputs.Pitch.Full_Down.R.PA = constant.pitch.R.PA[temp] * 1
        outputs.Pitch.Full_Down.R.PF = constant.pitch.R.PF[temp] * 1
        outputs.Pitch.Full_Down.R.Hub = constant.pitch.R.hub[temp] * 1
