# VariablesIO/IO_Conversion/link_calc_IO.py

def input_processing_link_calc():
    from VariableIO.initialize_IO import inputs
    from VariableIO.variables import constant,S,x,y,z
    from Functions.unit_conversion import in2mm, mm2in, kg2lb, lb2kg, kmh2mph, mph2kmh, npmm2lbpin, lbpin2npmm
    from math import pi

    #degree to rad conversion
    constant.F.panhard = inputs.F.panhard == True
    constant.F.U_count = inputs.F.U_count*1

    constant.R.panhard = inputs.R.panhard == True
    constant.R.U_count = inputs.R.U_count*1

    constant.V.drive_bias = inputs.V.drive_bias*1
    constant.V.brake_bias = inputs.V.brake_bias*1
    constant.V.weight_distribution = inputs.V.weight_distribution*1
    constant.V.acceleration = inputs.V.acceleration*1
    constant.V.transverse_acceleration = inputs.V.transverse_acceleration*1

    if S.units == 'metric':
        # if metric convert all inputs to sae and set variables
        
        constant.F.LA = mm2in(inputs.F.LA)
        constant.F.LF = mm2in(inputs.F.LF)
        constant.F.UA = mm2in(inputs.F.UA)
        constant.F.UF = mm2in(inputs.F.UF)
        if constant.F.panhard: constant.F.PA = mm2in(inputs.F.PA)
        if constant.F.panhard: constant.F.PF = mm2in(inputs.F.PF)
        constant.F.bump = mm2in(inputs.F.bump)
        constant.F.droop = mm2in(inputs.F.droop)
        constant.F.tire_radius = mm2in(inputs.F.tire_radius)
        constant.F.tire_diameter = mm2in(inputs.F.tire_diameter)
        constant.F.tire_width = mm2in(inputs.F.tire_width)
        constant.F.portal_height = mm2in(inputs.F.portal_height)
        constant.F.track_width = mm2in(inputs.F.track_width)
        constant.F.unsprung_mass = kg2lb(inputs.F.unsprung_mass)

        constant.R.LA = mm2in(inputs.R.LA)
        constant.R.LF = mm2in(inputs.R.LF)
        constant.R.UA = mm2in(inputs.R.UA)
        constant.R.UF = mm2in(inputs.R.UF)
        if constant.R.panhard: constant.R.PA = mm2in(inputs.R.PA)
        if constant.R.panhard: constant.R.PR = mm2in(inputs.R.PF)
        constant.R.bump = mm2in(inputs.R.bump)
        constant.R.droop = mm2in(inputs.R.droop)
        constant.R.tire_radius = mm2in(inputs.R.tire_radius)
        constant.R.tire_diameter = mm2in(inputs.R.tire_diameter)
        constant.R.tire_width = mm2in(inputs.F.tire_width)
        constant.R.portal_height = mm2in(inputs.R.portal_height)
        constant.R.track_width = mm2in(inputs.R.track_width)
        constant.R.unsprung_mass = kg2lb(inputs.R.unsprung_mass)

        constant.V.wheelbase = mm2in(inputs.V.wheelbase)
        constant.V.CG_height = mm2in(inputs.V.CG_height)
        constant.V.mass = kg2lb(inputs.V.mass)

    else:
        # set variables
        constant.F.LA = inputs.F.LA*1
        constant.F.LF = inputs.F.LF*1
        constant.F.UA = inputs.F.UA*1
        constant.F.UF = inputs.F.UF*1
        if constant.F.panhard: constant.F.PA = inputs.F.PA*1
        if constant.F.panhard: constant.F.PF = inputs.F.PF*1
        constant.F.bump = inputs.F.bump*1
        constant.F.droop = inputs.F.droop*1
        constant.F.tire_radius = inputs.F.tire_radius*1
        constant.F.tire_diameter = inputs.F.tire_diameter*1
        constant.F.tire_width = inputs.F.tire_width*1
        constant.F.portal_height = inputs.F.portal_height*1
        constant.F.track_width = inputs.F.track_width*1
        constant.F.unsprung_mass = inputs.F.unsprung_mass*1

        constant.R.LA = inputs.R.LA*1
        constant.R.LF = inputs.R.LF*1
        constant.R.UA = inputs.R.UA*1
        constant.R.UF = inputs.R.UF*1
        if constant.R.panhard: constant.R.PA = inputs.R.PA*1
        if constant.R.panhard: constant.R.PF = inputs.R.PF*1
        constant.R.bump = inputs.R.bump*1
        constant.R.droop = inputs.R.droop*1
        constant.R.tire_radius = inputs.R.tire_radius*1
        constant.R.tire_diameter = inputs.R.tire_diameter*1
        constant.R.tire_width = inputs.R.tire_width*1
        constant.R.portal_height = inputs.R.portal_height*1
        constant.R.track_width = inputs.R.track_width*1
        constant.R.unsprung_mass = inputs.R.unsprung_mass*1

        constant.V.wheelbase = inputs.V.wheelbase*1
        constant.V.CG_height = inputs.V.CG_height*1
        constant.V.mass = inputs.V.mass*1
        constant.V.desired_speed = inputs.V.desired_speed*1

    if S.reversed_front_x:
        constant.F.UA[x] = constant.V.wheelbase - constant.F.UA[x]
        constant.F.UF[x] = constant.V.wheelbase - constant.F.UF[x]
        constant.F.LA[x] = constant.V.wheelbase - constant.F.LA[x]
        constant.F.LF[x] = constant.V.wheelbase - constant.F.LF[x]
        constant.F.PA[x] = constant.V.wheelbase - constant.F.PA[x]
        constant.F.PF[x] = constant.V.wheelbase - constant.F.PF[x]
    else:
        constant.F.UA[x] = constant.V.wheelbase + constant.F.UA[x]
        constant.F.UF[x] = constant.V.wheelbase + constant.F.UF[x]
        constant.F.LA[x] = constant.V.wheelbase + constant.F.LA[x]
        constant.F.LF[x] = constant.V.wheelbase + constant.F.LF[x]
        constant.F.PA[x] = constant.V.wheelbase + constant.F.PA[x]
        constant.F.PF[x] = constant.V.wheelbase + constant.F.PF[x]


def output_processing_link_calc():
    from VariableIO.initialize_IO import outputs
    from VariableIO.variables import constant,travel,S
    from Functions.unit_conversion import in2mm, mm2in, kg2lb, lb2kg, kmh2mph, mph2kmh, npmm2lbpin, lbpin2npmm, lb2N
    from math import pi, degrees
    import numpy as np

    outputs.F.Anti_Dive = travel.F.anti_dive*100
    outputs.F.Anti_Lift = travel.F.anti_lift*100
    outputs.F.Roll_Slope = np.arctan(travel.F.roll_slope_dpd)*180/pi
    outputs.F.Pinion_Change = travel.F.pinion_rad*180/pi
    outputs.F.Upper_Convergence = constant.F.U_converge*180/pi
    outputs.F.Lower_Convergence = constant.F.L_converge*180/pi
    outputs.F.Total_Convergence = constant.F.total_converge*180/pi

    outputs.R.Anti_Squat = travel.R.anti_squat*100
    outputs.R.Anti_Lift = travel.R.anti_lift*100
    outputs.R.Roll_Slope = np.arctan(travel.R.roll_slope_dpd)*180/pi
    outputs.R.Pinion_Change = travel.R.pinion_rad*180/pi
    outputs.R.Upper_Convergence = constant.R.U_converge*180/pi
    outputs.R.Lower_Convergence = constant.R.L_converge*180/pi
    outputs.R.Total_Convergence = constant.R.total_converge*180/pi

    outputs.V.Acceleration = constant.V.acceleration*1
    outputs.V.Transverse_Acceleration = constant.V.transverse_acceleration
    outputs.V.Roll_Axis = np.arctan(constant.V.roll_slope_dpd)*180/pi
    outputs.V.Climb_Angle = constant.V.climb_angle*180/pi
    outputs.V.Descent_Angle = constant.V.descent_angle*180/pi
    outputs.V.Side_Roll_Angle = constant.V.side_roll_angle*180/pi

    outputs.F.U_top_view_angle = degrees(constant.F.U_top_view_angle)
    outputs.F.UF_side_view_angle_range = [degrees(constant.F.UF_side_view_angle_range[0]),degrees(constant.F.UF_side_view_angle_range[1])]
    outputs.F.UA_side_view_angle_range = [degrees(constant.F.UA_side_view_angle_range[0]),degrees(constant.F.UA_side_view_angle_range[1])]
    outputs.F.L_top_view_angle = degrees(constant.F.L_top_view_angle)
    outputs.F.LF_side_view_angle_range = [degrees(constant.F.LF_side_view_angle_range[0]),degrees(constant.F.LF_side_view_angle_range[1])]
    outputs.F.LA_side_view_angle_range = [degrees(constant.F.LA_side_view_angle_range[0]),degrees(constant.F.LA_side_view_angle_range[1])]
    outputs.F.PA_top_view_angle_range = [degrees(constant.F.PA_top_view_angle_range[0]),degrees(constant.F.PA_top_view_angle_range[1])]
    outputs.F.PF_top_view_angle_range = [degrees(constant.F.PF_top_view_angle_range[0]),degrees(constant.F.PF_top_view_angle_range[1])]
    outputs.F.PA_front_view_angle_range = [degrees(constant.F.PA_front_view_angle_range[0]),degrees(constant.F.PA_front_view_angle_range[1])]
    outputs.F.PF_front_view_angle_range = [degrees(constant.F.PF_front_view_angle_range[0]),degrees(constant.F.PF_front_view_angle_range[1])]

    outputs.R.U_top_view_angle = degrees(constant.R.U_top_view_angle)
    outputs.R.UF_side_view_angle_range = [degrees(constant.R.UF_side_view_angle_range[0]),degrees(constant.R.UF_side_view_angle_range[1])]
    outputs.R.UA_side_view_angle_range = [degrees(constant.R.UA_side_view_angle_range[0]),degrees(constant.R.UA_side_view_angle_range[1])]
    outputs.R.L_top_view_angle = degrees(constant.R.L_top_view_angle)
    outputs.R.LF_side_view_angle_range = [degrees(constant.R.LF_side_view_angle_range[0]),degrees(constant.R.LF_side_view_angle_range[1])]
    outputs.R.LA_side_view_angle_range = [degrees(constant.R.LA_side_view_angle_range[0]),degrees(constant.R.LA_side_view_angle_range[1])]
    outputs.R.PA_top_view_angle_range = [degrees(constant.R.PA_top_view_angle_range[0]),degrees(constant.R.PA_top_view_angle_range[1])]
    outputs.R.PF_top_view_angle_range = [degrees(constant.R.PF_top_view_angle_range[0]),degrees(constant.R.PF_top_view_angle_range[1])]
    outputs.R.PA_rear_view_angle_range = [degrees(constant.R.PA_rear_view_angle_range[0]),degrees(constant.R.PA_rear_view_angle_range[1])]
    outputs.R.PF_rear_view_angle_range = [degrees(constant.R.PF_rear_view_angle_range[0]),degrees(constant.R.PF_rear_view_angle_range[1])]

    if S.units == 'metric': # if metric convert all outputs to metric
        outputs.F.UA = in2mm(travel.F.UA)
        outputs.F.LA = in2mm(travel.F.LA)
        outputs.F.UF = in2mm(constant.F.UF)
        outputs.F.LF = in2mm(constant.F.LF)
        outputs.F.PA = in2mm(travel.F.PA)
        outputs.F.PF = in2mm(constant.F.PF)
        outputs.F.U_Length_3D = in2mm(constant.F.U_length_3D)
        outputs.F.L_Length_3D = in2mm(constant.F.L_length_3D)
        outputs.F.P_Length_3D = in2mm(constant.F.P_length_3D)
        outputs.F.U_Length_2D = in2mm(constant.F.U_length_2D)
        outputs.F.L_Length_2D = in2mm(constant.F.L_length_2D)
        outputs.F.P_Length_2D = in2mm(constant.F.P_length_2D)
        outputs.F.U_Max_Force = in2mm(constant.F.U_force)
        outputs.F.L_Max_Force = in2mm(constant.F.L_force)
        outputs.F.P_Max_Force = in2mm(constant.F.P_force)
        outputs.F.Travel = in2mm(travel.F.hub[:,2]-travel.F.hub[S.sample_points,2])
        outputs.F.Roll_Center = in2mm(travel.F.roll_center)
        outputs.F.Panhard_Transverse_Movement = in2mm(travel.R.panhard_transverse_movement)
        outputs.F.IC = in2mm(travel.F.IC)
        outputs.F.Anti_CG = in2mm(constant.F.anti_CG)
        outputs.F.Hub = in2mm(travel.F.hub)
        outputs.F.Sprung_CG_height_Above_Roll_Center = in2mm(constant.F.sprung_CG_height_above_roll_center)
        outputs.F.Min_Sep = in2mm(constant.F.min_distance)
        outputs.F.U_converge_point = in2mm(constant.F.U_converge_point)
        outputs.F.L_converge_point = in2mm(constant.F.L_converge_point)

        outputs.R.UA = in2mm(travel.R.UA)
        outputs.R.LA = in2mm(travel.R.LA)
        outputs.R.UF = in2mm(constant.R.UF)
        outputs.R.LF = in2mm(constant.R.LF)
        outputs.R.PA = in2mm(travel.R.PA)
        outputs.R.PF = in2mm(constant.R.PF)
        outputs.R.U_Length_3D = in2mm(constant.R.U_length_3D)
        outputs.R.L_Length_3D = in2mm(constant.R.L_length_3D)
        outputs.R.P_Length_3D = in2mm(constant.R.P_length_3D)
        outputs.R.U_Length_2D = in2mm(constant.R.U_length_2D)
        outputs.R.L_Length_2D = in2mm(constant.R.L_length_2D)
        outputs.R.P_Length_2D = in2mm(constant.R.P_length_2D)
        outputs.R.U_Max_Force = in2mm(constant.R.U_force)
        outputs.R.L_Max_Force = in2mm(constant.R.L_force)
        outputs.R.P_Max_Force = in2mm(constant.R.P_force)
        outputs.R.Travel = in2mm(travel.R.hub[:,2]-travel.R.hub[S.sample_points,2])
        outputs.R.Roll_Center = in2mm(travel.R.roll_center)
        outputs.R.Panhard_Transverse_Movement = in2mm(travel.R.panhard_transverse_movement)
        outputs.R.IC = in2mm(travel.R.IC)
        outputs.R.Anti_CG = in2mm(constant.R.anti_CG)
        outputs.R.Hub = in2mm(travel.R.hub)
        outputs.R.Sprung_CG_height_Above_Roll_Center = in2mm(constant.R.sprung_CG_height_above_roll_center)
        outputs.R.Min_Sep = in2mm(constant.R.min_distance)
        outputs.R.U_converge_point = in2mm(constant.R.U_converge_point)
        outputs.R.L_converge_point = in2mm(constant.R.L_converge_point)

        outputs.V.Sprung_CG_height = in2mm(constant.V.sprung_cg)
        outputs.V.Sprung_CG_height_Above_Roll_Axis = in2mm(constant.V.sprung_CG_height_above_roll_axis)

    else:
        outputs.F.UA = travel.F.UA*1
        outputs.F.LA = travel.F.LA*1
        outputs.F.UF = constant.F.UF*1
        outputs.F.LF = constant.F.LF*1
        outputs.F.PA = travel.F.PA*1
        outputs.F.PF = constant.F.PF*1
        outputs.F.U_Length_3D = constant.F.U_length_3D*1
        outputs.F.L_Length_3D = constant.F.L_length_3D*1
        outputs.F.P_Length_3D = constant.F.P_length_3D*1
        outputs.F.U_Length_2D = constant.F.U_length_2D*1
        outputs.F.L_Length_2D = constant.F.L_length_2D*1
        outputs.F.P_Length_2D = constant.F.P_length_2D*1
        outputs.F.U_Max_Force = constant.F.U_force*1
        outputs.F.L_Max_Force = constant.F.L_force*1
        outputs.F.P_Max_Force = constant.F.P_force*1
        outputs.F.Travel = (travel.F.hub[:,2]-travel.F.hub[S.sample_points,2])*1
        outputs.F.Roll_Center = travel.F.roll_center*1
        outputs.F.Panhard_Transverse_Movement = travel.R.panhard_transverse_movement*1
        outputs.F.IC = travel.F.IC*1
        outputs.F.Anti_CG = constant.F.anti_CG*1
        outputs.F.Hub = travel.F.hub*1
        outputs.F.Sprung_CG_height_Above_Roll_Center = constant.F.sprung_CG_height_above_roll_center*1
        outputs.F.Min_Sep = constant.F.min_distance*1
        outputs.F.U_converge_point = constant.F.U_converge_point*1
        outputs.F.L_converge_point = constant.F.L_converge_point*1

        outputs.R.UA = travel.R.UA*1
        outputs.R.LA = travel.R.LA*1
        outputs.R.UF = constant.R.UF*1
        outputs.R.LF = constant.R.LF*1
        outputs.R.PA = travel.R.PA*1
        outputs.R.PF = constant.R.PF*1
        outputs.R.U_Length_3D = constant.R.U_length_3D*1
        outputs.R.L_Length_3D = constant.R.L_length_3D*1
        outputs.R.P_Length_3D = constant.R.P_length_3D*1
        outputs.R.U_Length_2D = constant.R.U_length_2D*1
        outputs.R.L_Length_2D = constant.R.L_length_2D*1
        outputs.R.P_Length_2D = constant.R.P_length_2D*1
        outputs.R.U_Max_Force = constant.R.U_force*1
        outputs.R.L_Max_Force = constant.R.L_force*1
        outputs.R.P_Max_Force = constant.R.P_force*1
        outputs.R.Travel = (travel.R.hub[:,2]-travel.R.hub[S.sample_points,2])*1
        outputs.R.Roll_Center = travel.R.roll_center*1
        outputs.R.Panhard_Transverse_Movement = travel.R.panhard_transverse_movement*1
        outputs.R.IC = travel.R.IC*1
        outputs.R.Anti_CG = constant.R.anti_CG*1
        outputs.R.Hub = travel.R.hub*1
        outputs.R.Sprung_CG_height_Above_Roll_Center = constant.R.sprung_CG_height_above_roll_center*1
        outputs.R.Min_Sep = constant.R.min_distance*1
        outputs.R.U_converge_point = constant.R.U_converge_point*1
        outputs.R.L_converge_point = constant.R.L_converge_point*1
        
        outputs.V.Sprung_CG_height = constant.V.sprung_cg*1
        outputs.V.Sprung_CG_height_Above_Roll_Axis = constant.V.sprung_CG_height_above_roll_axis*1