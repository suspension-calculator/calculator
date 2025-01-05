def run_vehicle_pitch():
    from math import sqrt, cos, atan2, sin
    import numpy as np

    from VariableIO.variables import constant, travel, S, x,y,z
    from VariableIO.IO_Conversion.vehicle_pitch_IO import input_processing_vehicle_pitch, output_processing_vehicle_pitch

    from Functions.distance_2d import dis2D
    from Functions.distance_3d import dis3D
    #from Functions.unit_conversion import in2mm, mm2in, kg2lb, lb2kg, kmh2mph, mph2kmh, npmm2lbpin, lbpin2npmm
    #from Functions.floor_2_zero import floor2zero
    from Functions.rotation import rotate
    #from Functions.segment_seperation import SegSep
    from Functions.line_intersection import LineIntersect
    from Functions.link_travel import travel_solve
    from Functions.rotation import rotate
    from Functions.travel_wheel_2_lca import wheel_2_lca
    from Functions.axle_point_movement import on_axle_movement
    from Functions.Y_equals_0 import ZeroY
    from Functions.pinion_rotation import pinion_angle_change

    input_processing_vehicle_pitch()

    #------------------------------ Constant variable setup -------------------------------------
    x=0 # set value of x for easy array referencing
    y=1 # set value of y for easy array referencing
    z=2 # set value of z for easy array referencing

    F_hub = [constant.V.wheelbase,0,constant.F.tire_radius] # [x,y,z] of front hub center
    R_hub = [0,0,constant.R.tire_radius] # [x,y,z] of rear hub center 

    F_U_parallel = constant.F.UF[y] == constant.F.UA[y] and constant.F.U_count == 2 # If front 2 upper links and the are parallel, set flag
    F_L_parallel = constant.F.LF[y] == constant.F.LA[y] # If front lower links are parallel, set flag
    R_U_parallel = constant.R.UF[y] == constant.R.UA[y] and constant.R.U_count == 2 # If front 2 upper links and the are parallel, set flag
    R_L_parallel = constant.R.LF[y] == constant.R.LA[y] # If rear lower links are parallel, set flag

    upper_point = np.zeros(3) # Define upper point for first pass
    lower_point = np.zeros(3) # Define lower point for first pass

    F_tire_rate = (constant.F.tire_diameter*.5-constant.F.tire_radius)/(-1*constant.F.droop) # Find front tire spring rate [compression/travel]
    R_tire_rate = (constant.R.tire_diameter*.5-constant.R.tire_radius)/(-1*constant.R.droop) # Find rear tire spring rate [compression/travel]


    #------------------------------ Preallocation and setup math -------------------------------------

    F_travel_points = [constant.F.pitch_travel,constant.F.bump,constant.F.bump*.5,constant.F.droop*.5,constant.F.droop,constant.F.bump,constant.F.droop] # Hub travel array for front [user input, 100% rear pitch_rad, 50% rear pitch_rad, 50% front pitch_rad, 100% front pitch_rad, 100% bump, 100% droop]
    R_travel_points = [constant.R.pitch_travel,constant.R.droop,constant.R.droop*.5,constant.R.bump*.5,constant.R.bump,constant.R.bump,constant.R.droop] # Hub travel array for rear  [user input, 100% rear pitch_rad, 50% rear pitch_rad, 50% front pitch_rad, 100% front pitch_rad, 100% bump, 100% droop]

    constant.pitch.F.travel = F_travel_points
    constant.pitch.R.travel = R_travel_points

    point_count = len(F_travel_points)

    PR_B_CG = [0,0,0]
    AR_B_CG = [0,0,0]

    F_LCA_travel = [0]*point_count # Preallocate front lower axle movement array
    R_LCA_travel = [0]*point_count # Preallocate rear lower axle movement array

    PR_F_UA_travel = [[0] * 3 for _ in range(point_count)] # Preallocate front upper travel matrix
    PR_F_LA_travel = [[0] * 3 for _ in range(point_count)] # Preallocate front lower travel matrix
    PR_R_UA_travel = [[0] * 3 for _ in range(point_count)] # Preallocate rear upper travel matrix
    PR_R_LA_travel = [[0] * 3 for _ in range(point_count)] # Preallocate rear lower travel matrix

    PR_F_hub_travel = [[0] * 3 for _ in range(point_count)] # Preallocate front hub center travel matrix
    PR_R_hub_travel = [[0] * 3 for _ in range(point_count)] # Preallocate rear hub center travel matrix
    if constant.F.panhard: PR_F_PA_travel = [[0] * 3 for _ in range(point_count)] # Preallocate front panhard travel matrix
    if constant.R.panhard: PR_R_PA_travel = [[0] * 3 for _ in range(point_count)] # Preallocate rear panhard travel matrix

    F_pinion_travel_rad = [0]*point_count # Preallocate front pinion angle change array
    R_pinion_travel_rad = [0]*point_count # Preallocate rear pinion angle change array

    pitch_rad = [0]*point_count # Preallocate vehicle pitch_rad angle array

    constant.pitch.F.UA[y] = constant.F.UA[y]
    constant.pitch.F.LA[y] = constant.F.LA[y]
    constant.pitch.R.UA[y] = constant.R.UA[y]
    constant.pitch.R.LA[y] = constant.R.LA[y]

    constant.pitch.F.UF[y] = constant.F.UF[y]
    constant.pitch.F.LF[y] = constant.F.LF[y]
    constant.pitch.R.UF[y] = constant.R.UF[y]
    constant.pitch.R.LF[y] = constant.R.LF[y]

    if constant.F.panhard:
        constant.pitch.F.PF[y] = constant.F.PF[y]
    if constant.R.panhard:
        constant.pitch.R.PF[y] = constant.R.PF[y]

    F_U_parallel = constant.F.UF[y] == constant.F.UA[y] and constant.F.U_count == 2 # If front 2 upper links and the are parallel, set flag
    F_L_parallel = constant.F.LF[y] == constant.F.LA[y] # If front lower links are parallel, set flag
    R_U_parallel = constant.R.UF[y] == constant.R.UA[y] and constant.R.U_count == 2 # If front 2 upper links and the are parallel, set flag
    R_L_parallel = constant.R.LF[y] == constant.R.LA[y] # If rear lower links are parallel, set flag

    upper_point = [0,0,0] # Define upper point for first pass
    lower_point = [0,0,0] # Define lower point for first pass

    F_roll_center_travel = [0]*point_count # Preallocate front roll center array
    R_roll_center_travel = [0]*point_count # Preallocate rear roll center array

    F_IC_travel = [[0] * 3 for _ in range(point_count)] # Preallocate front panhard travel matrix
    R_IC_travel = [[0] * 3 for _ in range(point_count)] # Preallocate rear panhard travel matrix



    #accel = [0]*6
    #half_weight_transfer = [0]*6
    #rear_force = [0]*6
    #front_force = [0]*6
    #rear_force_closest = [0]*6
    #rear_travel_est = [0]*6
    #front_force_closest = [0]*6
    #front_travel_est = [0]*6
    #drive_bias = [0]*6
    #brake_bias = [0]*6
    #front_load_bias = [0]*6

    front_spring_force = [[0] for _ in range(S.sample_points*2+1+1)]
    rear_spring_force = [[0] for _ in range(S.sample_points*2+1+1)]


    #------------------------------ Maths -------------------------------------
    F_unsprung_CG_height = F_hub[z]+.5*constant.F.portal_height # Calculate CG of front axle
    R_unsprung_CG_height = R_hub[z]+.5*constant.R.portal_height # Calculate CG of rear axle

    V_sprung_mass = constant.V.mass - constant.R.unsprung_mass -constant.F.unsprung_mass

    PR_B_CG[x] = (constant.V.wheelbase*constant.V.weight_distribution*constant.V.mass-constant.V.wheelbase*constant.F.unsprung_mass)/(V_sprung_mass) # X CG of sprung mass
    PR_B_CG[y] = 0 # Y CG of sprung mass
    PR_B_CG[z] = (constant.V.CG_height*constant.V.mass-F_unsprung_CG_height*constant.F.unsprung_mass-R_unsprung_CG_height*constant.R.unsprung_mass)/(V_sprung_mass) # Z CG of sprung mass

    for i in range(0,len(F_travel_points)):
        F_LCA_travel = wheel_2_lca(F_travel_points[i],constant.F.UA[x],constant.F.UA[z],constant.F.UF[x],constant.F.UF[z],constant.F.LA[x],constant.F.LA[z],constant.F.LF[x],constant.F.LF[z],constant.F.U_length_2D,constant.F.L_length_2D,constant.F.A_sep_2D,constant.F.F_sep_2D,F_hub[x],F_hub[z]) # Calculate front lower axle z movement for given wheel travel
        R_LCA_travel = wheel_2_lca(R_travel_points[i],constant.R.UA[x],constant.R.UA[z],constant.R.UF[x],constant.R.UF[z],constant.R.LA[x],constant.R.LA[z],constant.R.LF[x],constant.R.LF[z],constant.R.U_length_2D,constant.R.L_length_2D,constant.R.A_sep_2D,constant.R.F_sep_2D,R_hub[x],R_hub[z]) # Calculate rear lower axle z movement for given wheel travel

        PR_F_UA_travel[x],PR_F_UA_travel[z],PR_F_LA_travel[x],PR_F_LA_travel[z] = travel_solve(F_LCA_travel,constant.F.UA[x],constant.F.UA[z],constant.F.UF[x],constant.F.UF[z],constant.F.LA[x],constant.F.LA[z],constant.F.LF[x],constant.F.LF[z],constant.F.U_length_2D,constant.F.L_length_2D,constant.F.A_sep_2D,constant.F.F_sep_2D) # Calculate front arm arcs
        PR_R_UA_travel[x],PR_R_UA_travel[z],PR_R_LA_travel[x],PR_R_LA_travel[z] = travel_solve(R_LCA_travel,constant.R.UA[x],constant.R.UA[z],constant.R.UF[x],constant.R.UF[z],constant.R.LA[x],constant.R.LA[z],constant.R.LF[x],constant.R.LF[z],constant.R.U_length_2D,constant.R.L_length_2D,constant.R.A_sep_2D,constant.R.F_sep_2D) # Calculate rear arm arcs

        F_pinion_travel_rad = pinion_angle_change(constant.F.UA[x], constant.F.UA[z], PR_F_UA_travel[x], PR_F_UA_travel[z], constant.F.LA[x], constant.F.LA[z], PR_F_LA_travel[x], PR_F_LA_travel[z]) # Calculate front pinion angle change
        R_pinion_travel_rad = pinion_angle_change(constant.R.UA[x], constant.R.UA[z], PR_R_UA_travel[x], PR_R_UA_travel[z], constant.R.LA[x], constant.R.LA[z], PR_R_LA_travel[x], PR_R_LA_travel[z]) # Calculate rear pinion angle change

        PR_F_hub_travel[x],PR_F_hub_travel[z] = on_axle_movement(F_hub[x],F_hub[z],constant.F.LA[x],constant.F.LA[z],PR_F_LA_travel[x],PR_F_LA_travel[z],F_pinion_travel_rad) # Calculate front hub center movement
        PR_R_hub_travel[x],PR_R_hub_travel[z] = on_axle_movement(R_hub[x],R_hub[z],constant.R.LA[x],constant.R.LA[z],PR_R_LA_travel[x],PR_R_LA_travel[z],R_pinion_travel_rad) # Calculate rear hub center movement

        if constant.F.panhard: # If front panhard is used
            PR_F_PA_travel[x],PR_F_PA_travel[z] = on_axle_movement(constant.F.PA[x],constant.F.PA[z],constant.F.LA[x],constant.F.LA[z],PR_F_LA_travel[x],PR_F_LA_travel[z],F_pinion_travel_rad) # Calculate front panhard X and Z movement
            constant.pitch.F.PA[y] = constant.F.PF[y]-sqrt(constant.F.P_length_3D**2-(constant.F.PF[x]-PR_F_PA_travel[x])**2-(constant.F.PF[z]-PR_F_PA_travel[z])**2) # Calculate front panhard Y movement
        if constant.R.panhard: # If rear panhard is used
            PR_R_PA_travel[x],PR_R_PA_travel[z] = on_axle_movement(constant.R.PA[x],constant.R.PA[z],constant.R.LA[x],constant.R.LA[z],PR_R_LA_travel[x],PR_R_LA_travel[z],R_pinion_travel_rad) # Calculate rear panhard X and Z movement
            constant.pitch.R.PA[y] = constant.R.PF[y]-sqrt(constant.R.P_length_3D**2-(constant.R.PF[x]-PR_R_PA_travel[x])**2-(constant.R.PF[z]-PR_R_PA_travel[z])**2) # Calculate rear panhard Y movement

        if S.simulate_tire_loading: # If tire loading is being simulated
            F_loaded_tire_radius =constant.F.tire_diameter*.5-F_tire_rate*(F_LCA_travel[i]-constant.F.droop)
            PR_F_wheel_contact = PR_F_hub_travel[z]-F_loaded_tire_radius # Calculate front contanct point
            R_loaded_tire_radius = constant.R.tire_diameter*.5-R_tire_rate*(R_LCA_travel[i]-constant.R.droop)
            PR_R_wheel_contact = PR_R_hub_travel[z]-R_loaded_tire_radius # Calculate rear contanct point
        else:
            PR_F_wheel_contact = PR_F_hub_travel[z]-constant.F.tire_radius # Calculate front contanct point
            PR_R_wheel_contact = PR_R_hub_travel[z]-constant.R.tire_radius # Calculate rear contanct point
            F_loaded_tire_radius = constant.F.tire_radius
            R_loaded_tire_radius = constant.R.tire_radius

        pitch_rad[i] = -1*atan2(PR_F_wheel_contact-PR_R_wheel_contact,PR_F_hub_travel[x]-PR_R_hub_travel[x])
        pitch_F_caster_change = pitch_rad[i] + F_pinion_travel_rad
        pitch_R_caster_change = pitch_rad[i] + R_pinion_travel_rad

        AR_F_pinion_rotation_rad = pinion_angle_change(constant.F.UA[x], constant.F.UA[z], PR_F_UA_travel[x], PR_F_UA_travel[z], constant.F.LA[x], constant.F.LA[z], PR_F_LA_travel[x], PR_F_LA_travel[z]) # Calculate front pinion angle change
        AR_R_pinion_rotation_rad = pinion_angle_change(constant.R.UA[x], constant.R.UA[z], PR_R_UA_travel[x], PR_R_UA_travel[z], constant.R.LA[x], constant.R.LA[z], PR_R_LA_travel[x], PR_R_LA_travel[z]) # Calculate rear pinion angle change

        constant.pitch.F.UA[i][x] = rotate(PR_R_hub_travel[x],PR_R_hub_travel[z],PR_F_UA_travel[x],PR_F_hub_travel[z],pitch_rad[i])[0] - PR_R_hub_travel[x]
        constant.pitch.F.UF[i][x] = rotate(PR_R_hub_travel[x],PR_R_hub_travel[z],constant.F.UF[x],constant.F.UF[z],pitch_rad[i])[0] - PR_R_hub_travel[x]
        constant.pitch.F.LA[i][x] = rotate(PR_R_hub_travel[x],PR_R_hub_travel[z],PR_F_LA_travel[x],PR_F_LA_travel[z],pitch_rad[i])[0] - PR_R_hub_travel[x]
        constant.pitch.F.LF[i][x] = rotate(PR_R_hub_travel[x],PR_R_hub_travel[z],constant.F.LF[x],constant.F.LF[z],pitch_rad[i])[0] - PR_R_hub_travel[x]
        constant.pitch.R.UA[i][x] = rotate(PR_R_hub_travel[x],PR_R_hub_travel[z],PR_R_UA_travel[x],PR_R_UA_travel[z],pitch_rad[i])[0] - PR_R_hub_travel[x]
        constant.pitch.R.UF[i][x] = rotate(PR_R_hub_travel[x],PR_R_hub_travel[z],constant.R.UF[x],constant.R.UF[z],pitch_rad[i])[0] - PR_R_hub_travel[x]
        constant.pitch.R.LA[i][x] = rotate(PR_R_hub_travel[x],PR_R_hub_travel[z],PR_R_LA_travel[x],PR_R_LA_travel[z],pitch_rad[i])[0] - PR_R_hub_travel[x]
        constant.pitch.R.LF[i][x] = rotate(PR_R_hub_travel[x],PR_R_hub_travel[z],constant.R.LF[x],constant.R.LF[z],pitch_rad[i])[0] - PR_R_hub_travel[x]
        constant.pitch.F.hub[i][x] = rotate(PR_R_hub_travel[x],PR_R_hub_travel[z],PR_F_hub_travel[x],PR_F_hub_travel[z],pitch_rad[i])[0] - PR_R_hub_travel[x]

        constant.pitch.F.UA[i][z] = rotate(PR_R_hub_travel[x],PR_R_hub_travel[z],PR_F_UA_travel[x],PR_F_hub_travel[z],pitch_rad[i])[1] - PR_R_hub_travel[z]-R_loaded_tire_radius
        constant.pitch.F.UF[i][z] = rotate(PR_R_hub_travel[x],PR_R_hub_travel[z],constant.F.UF[x],constant.F.UF[z],pitch_rad[i])[1] - PR_R_hub_travel[z]-R_loaded_tire_radius
        constant.pitch.F.LA[i][z] = rotate(PR_R_hub_travel[x],PR_R_hub_travel[z],PR_F_LA_travel[x],PR_F_LA_travel[z],pitch_rad[i])[1] - PR_R_hub_travel[z]-R_loaded_tire_radius
        constant.pitch.F.LF[i][z] = rotate(PR_R_hub_travel[x],PR_R_hub_travel[z],constant.F.LF[x],constant.F.LF[z],pitch_rad[i])[1] - PR_R_hub_travel[z]-R_loaded_tire_radius
        constant.pitch.R.UA[i][z] = rotate(PR_R_hub_travel[x],PR_R_hub_travel[z],PR_R_UA_travel[x],PR_R_UA_travel[z],pitch_rad[i])[1] - PR_R_hub_travel[z]-R_loaded_tire_radius
        constant.pitch.R.UF[i][z] = rotate(PR_R_hub_travel[x],PR_R_hub_travel[z],constant.R.UF[x],constant.R.UF[z],pitch_rad[i])[1] - PR_R_hub_travel[z]-R_loaded_tire_radius
        constant.pitch.R.LA[i][z] = rotate(PR_R_hub_travel[x],PR_R_hub_travel[z],PR_R_LA_travel[x],PR_R_LA_travel[z],pitch_rad[i])[1] - PR_R_hub_travel[z]-R_loaded_tire_radius
        constant.pitch.R.LF[i][z] = rotate(PR_R_hub_travel[x],PR_R_hub_travel[z],constant.R.LF[x],constant.R.LF[z],pitch_rad[i])[1] - PR_R_hub_travel[z]-R_loaded_tire_radius
        constant.pitch.F.hub[i][z] = rotate(PR_R_hub_travel[x],PR_R_hub_travel[z],PR_F_hub_travel[x],PR_F_hub_travel[z],pitch_rad[i])[1] - (PR_R_hub_travel[z]-R_loaded_tire_radius)

        constant.pitch.R.hub[i][z] = R_loaded_tire_radius

        if constant.F.panhard: # If front panhard is used
            temp1,temp2 = rotate(PR_R_hub_travel[x],PR_R_hub_travel[z],PR_F_PA_travel[x],PR_F_PA_travel[z],pitch_rad[i])
            constant.pitch.F.PA[i][x] = temp1 -PR_R_hub_travel[x]
            constant.pitch.F.PA[i][z] =  temp2 - (PR_R_hub_travel[z]-R_loaded_tire_radius)
            temp1,temp2 = rotate(PR_R_hub_travel[x],PR_R_hub_travel[z],constant.F.PF[x],constant.F.PF[z],pitch_rad[i])
            constant.pitch.F.PF[i][x] = temp1 - PR_R_hub_travel[x]
            constant.pitch.F.PF[i][z] =  temp2 - (PR_R_hub_travel[z]-R_loaded_tire_radius)
        if constant.R.panhard: # If rear panhard is used
            temp1,temp2 = rotate(PR_R_hub_travel[x],PR_R_hub_travel[z],PR_R_PA_travel[x],PR_R_PA_travel[z],pitch_rad[i])
            constant.pitch.R.PA[i][x] = temp1 - PR_R_hub_travel[x]
            constant.pitch.R.PA[i][z] = temp2 - (PR_R_hub_travel[z]-R_loaded_tire_radius)
            temp1,temp2 = rotate(PR_R_hub_travel[x],PR_R_hub_travel[z],constant.R.PF[x],constant.R.PF[z],pitch_rad[i])
            constant.pitch.R.PF[i][x] = temp1 - PR_R_hub_travel[x]
            constant.pitch.R.PF[i][z] = temp2 - (PR_R_hub_travel[z]-R_loaded_tire_radius)

        AR_B_CG[x] = rotate(PR_R_hub_travel[x],PR_R_hub_travel[z],PR_B_CG[x],PR_B_CG[z],pitch_rad[i])[0] - PR_R_hub_travel[x]
        AR_B_CG[z] = rotate(PR_R_hub_travel[x],PR_R_hub_travel[z],PR_B_CG[x],PR_B_CG[z],pitch_rad[i])[1] - (PR_R_hub_travel[z]-R_loaded_tire_radius)

        #---------------------------------------------------------------------------------Roll Calculations---------------------------------------------------------------------------------

        if constant.F.panhard: # If front panhard exists, calculate roll stuff based on it
            upper_point[x],upper_point[z] = ZeroY(constant.pitch.F.PF[i][x],constant.pitch.F.PF[i][y],constant.pitch.F.PF[i][z],constant.pitch.F.PA[i][x],constant.pitch.F.PA[i][y],constant.pitch.F.PA[i][x]) # Upper point is where panhard crosses centerline, y=0
            if F_L_parallel: # If front lowers are parallel, find lower point such that roll slope will be parallel to lower links
                lower_point[x] = upper_point[x]+constant.pitch.F.LF[i][x]-constant.pitch.F.LA[i][x] # Add lower link x component to upper point
                lower_point[z] = upper_point[z]+constant.pitch.F.LF[i][z]-constant.pitch.F.LA[i][z] # Add lower link z component to upper point
            else: # Solve for lower point
                lower_point[x],lower_point[z] = ZeroY(constant.pitch.F.LF[i][x],constant.pitch.F.LF[i][y],constant.pitch.F.LF[i][z],constant.pitch.F.LA[i][x],constant.pitch.F.LA[i][y],constant.pitch.F.LA[i][z]) # Find where lower links intersect in top view, y=0
        else:
            if F_U_parallel: # If front uppers are parallel, find upper point such that roll slope will be parallel to upper links
                lower_point[x],lower_point[z] = ZeroY(constant.pitch.F.LF[i][x],constant.pitch.F.LF[i][y],constant.pitch.F.LF[i][z],constant.pitch.F.LA[i][x],constant.pitch.F.LA[i][y],constant.pitch.F.LA[i][z]) # Find where lower links intersect in top view, y=0
                upper_point[x] = lower_point[x]+constant.pitch.F.LF[i][x]-constant.pitch.F.UA[i][x] # Add upper link x component to lower point
                upper_point[z] = lower_point[z]+constant.pitch.F.LF[i][z]-constant.pitch.F.UA[i][z] # Add upper link z component to lower point
            elif F_L_parallel: # If front lowers are parallel, find lower point such that roll slope will be parallel to lower links
                upper_point[x],upper_point[z] = ZeroY(constant.pitch.F.UF[i][x],constant.pitch.F.UF[i][y],constant.pitch.F.UF[i][z],constant.pitch.F.UA[i][x],constant.pitch.F.UA[i][y],constant.pitch.F.UA[i][z]) # Find where upper links intersect in top view, y=0
                lower_point[x] = upper_point[x]+constant.pitch.F.LF[i][x]-constant.pitch.F.LA[i][x] # Add lower link x component to upper point
                lower_point[z] = upper_point[z]+constant.pitch.F.LF[i][z]-constant.pitch.F.LA[i][z] # Add lower link z component to upper point
            elif F_U_parallel and F_L_parallel: # If front lowers are parallel and front uppers are parallel, create flat roll slope at ground level
                upper_point[x] = 0
                upper_point[z] = 0
                lower_point[x] = 1
                lower_point[z] = 0
            else:
                upper_point[x],upper_point[z] = ZeroY(constant.pitch.F.UF[i][x],constant.pitch.F.UF[i][y],constant.pitch.F.UF[i][z],constant.pitch.F.UA[i][x],constant.pitch.F.UA[i][y],constant.pitch.F.UA[i][z]) # Find where upper links intersect in top view, y=0
                lower_point[x],lower_point[z] = ZeroY(constant.pitch.F.LF[i][x],constant.pitch.F.LF[i][y],constant.pitch.F.LF[i][z],constant.pitch.F.LA[i][x],constant.pitch.F.LA[i][y],constant.pitch.F.LA[i][z]) # Find where lower links intersect in top view, y=0
        constant.pitch.F.roll_slope_dpd[i] = (upper_point[z]-lower_point[z])/(upper_point[x]-lower_point[x]) # Calculate front roll slope [distance rise/distance run]
        constant.pitch.F.roll_center[i] = LineIntersect(upper_point[x],upper_point[z],lower_point[x],lower_point[z],constant.pitch.F.hub[i][x],0,constant.pitch.F.hub[i][x],1)[1] # Find front roll center by using intersect between roll slope and vertical line at the wheel hubs

        if constant.R.panhard: # If rear panhard exists, calculate roll stuff based on it
            upper_point[x],upper_point[z] = ZeroY(constant.pitch.R.PF[i][x],constant.pitch.R.PF[i][y],constant.pitch.R.PF[i][z],constant.pitch.R.PA[i][x],constant.pitch.R.PA[i][y],constant.pitch.R.PA[i][x]) # Upper point is where panhard crosses centerline, y=0
            if R_L_parallel: # If rear lowers are parallel, find lower point such that roll slope will be parallel to lower links
                lower_point[x] = upper_point[x]+constant.pitch.R.LF[i][x]-constant.pitch.R.LA[i][x] # Add lower link x component to upper point
                lower_point[z] = upper_point[z]+constant.pitch.R.LF[i][z]-constant.pitch.R.LA[i][z] # Add lower link z component to upper point
            else: # Solve for lower point
                lower_point[x],lower_point[z] = ZeroY(constant.pitch.R.LF[i][x],constant.pitch.R.LF[i][y],constant.pitch.R.LF[i][z],constant.pitch.R.LA[i][x],constant.pitch.R.LA[i][y],constant.pitch.R.LA[i][z]) # Find where lower links intersect in top view, y=0
        else:
            if R_U_parallel: # If rear uppers are parallel, find upper point such that roll slope will be parallel to upper links
                lower_point[x],lower_point[z] = ZeroY(constant.pitch.R.LF[i][x],constant.pitch.R.LF[i][y],constant.pitch.R.LF[i][z],constant.pitch.R.LA[i][x],constant.pitch.R.LA[i][y],constant.pitch.R.LA[i][z]) # Find where lower links intersect in top view, y=0
                upper_point[x] = lower_point[x]+constant.pitch.R.LF[i][x]-constant.pitch.R.UA[i][x] # Add upper link x component to lower point
                upper_point[z] = lower_point[z]+constant.pitch.R.LF[i][z]-constant.pitch.R.UA[i][z] # Add upper link z component to lower point
            elif R_L_parallel: # If rear lowers are parallel, find lower point such that roll slope will be parallel to lower links
                upper_point[x],upper_point[z] = ZeroY(constant.pitch.R.UF[i][x],constant.pitch.R.UF[i][y],constant.pitch.R.UF[i][z],constant.pitch.R.UA[i][x],constant.pitch.R.UA[i][y],constant.pitch.R.UA[i][z]) # Find where upper links intersect in top view, y=0
                lower_point[x] = upper_point[x]+constant.pitch.R.LF[i][x]-constant.pitch.R.LA[i][x] # Add lower link x component to upper point
                lower_point[z] = upper_point[z]+constant.pitch.R.LF[i][z]-constant.pitch.R.LA[i][z] # Add lower link z component to upper point
            elif R_U_parallel and R_L_parallel: # If rear lowers are parallel and rear uppers are parallel, create flat roll slope at ground level
                upper_point[x] = 0
                upper_point[z] = 0
                lower_point[x] = 1
                lower_point[z] = 0
            else:
                upper_point[x],upper_point[z] = ZeroY(constant.pitch.R.UF[i][x],constant.pitch.R.UF[i][y],constant.pitch.R.UF[i][z],constant.pitch.R.UA[i][x],constant.pitch.R.UA[i][y],constant.pitch.R.UA[i][z]) # Find where upper links intersect in top view, y=0
                lower_point[x],lower_point[z] = ZeroY(constant.pitch.R.LF[i][x],constant.pitch.R.LF[i][y],constant.pitch.R.LF[i][z],constant.pitch.R.LA[i][x],constant.pitch.R.LA[i][y],constant.pitch.R.LA[i][z]) # Find where lower links intersect in top view, y=0
        constant.pitch.R.roll_slope_dpd[i] = (upper_point[z]-lower_point[z])/(upper_point[x]-lower_point[x]) # Calculate front roll slope [distance rise/distance run]
        constant.pitch.R.roll_center[i] = LineIntersect(upper_point[x],upper_point[z],lower_point[x],lower_point[z],constant.pitch.R.hub[i][x],0,constant.pitch.R.hub[i][x],1)[1] # Find rear roll center by using intersect between roll slope and vertical line at the wheel hubs

        #---------------------------------------------------------------------------------Anti Calculations---------------------------------------------------------------------------------

        if (constant.pitch.F.LF[i][z]-constant.pitch.F.LA[i][z])/(constant.pitch.F.LF[i][x]-constant.pitch.F.LA[i][x]) == (constant.pitch.F.UF[i][z]-constant.pitch.F.UA[i][z])/(constant.pitch.F.UF[i][x]-constant.pitch.F.UA[i][x]): # If slope of the front lower links is the same as the slope of the front upper links
            F_IC_travel[i][x] = constant.pitch.F.hub[i][x] + (constant.pitch.F.LF[i][x]-constant.pitch.F.LA[i][x]) # Define point on wheel contact to infinite IC line
            F_IC_travel[i][z] = constant.pitch.F.LF[i][z]-constant.pitch.F.LA[i][z] # Define point on wheel contact to infinite IC line
        else:
            F_IC_travel[i][x],F_IC_travel[i][z] = LineIntersect(constant.pitch.F.LF[i][x],constant.pitch.F.LF[i][z],constant.pitch.F.LA[i][x],constant.pitch.F.LA[i][z],constant.pitch.F.UF[i][x],constant.pitch.F.UF[i][z],constant.pitch.F.UA[i][x],constant.pitch.F.UA[i][z]) # Find intersection of upper and lower links in side view
        if (constant.pitch.R.LF[i][z]-constant.pitch.R.LA[i][z])/(constant.pitch.R.LF[i][x]-constant.pitch.R.LA[i][x]) == (constant.pitch.R.UF[i][z]-constant.pitch.R.UA[i][z])/(constant.pitch.R.UF[i][x]-constant.pitch.R.UA[i][x]): # If slope of the rear lower links is the same as the slope of the rear upper links
            R_IC_travel[i][x] = constant.pitch.R.hub[i][x] + (constant.pitch.R.LF[i][x]-constant.pitch.R.LA[i][x]) # Define point on wheel contact to infinite IC line
            R_IC_travel[i][z] = constant.pitch.R.LF[i][z]-constant.pitch.R.LA[i][z] # Define point on wheel contact to infinite IC line
        else:
            R_IC_travel[i][x],R_IC_travel[i][z] = LineIntersect(constant.pitch.R.LF[i][x],constant.pitch.R.LF[i][z],constant.pitch.R.LA[i][x],constant.pitch.R.LA[i][z],constant.pitch.R.UF[i][x],constant.pitch.R.UF[i][z],constant.pitch.R.UA[i][x],constant.pitch.R.UA[i][z]) # Find intersection of upper and lower links in side view

        drive_x = constant.pitch.F.hub[i][x]*constant.pitch.drive_bias # Find driving x measument point, accounting for change in constant.V.wheelbase
        brake_x = constant.pitch.F.hub[i][x]*constant.pitch.brake_bias # Find braking x measument point, accounting for change in constant.V.wheelbase

        F_drive_intersect_z = LineIntersect(0,constant.pitch.F.hub[i][x],F_IC_travel[i][x],F_IC_travel[i][z],drive_x,0,drive_x,1)[1] # Find where anti line crosses under/over measurement point
        F_brake_intersect_z = LineIntersect(0,constant.pitch.F.hub[i][x],F_IC_travel[i][x],F_IC_travel[i][z],brake_x,0,brake_x,1)[1] # Find where anti line crosses under/over measurement point
        R_drive_intersect_z = LineIntersect(0,constant.pitch.R.hub[i][x],R_IC_travel[i][x],R_IC_travel[i][z],drive_x,0,drive_x,1)[1] # Find where anti line crosses under/over measurement point
        R_brake_intersect_z = LineIntersect(0,constant.pitch.R.hub[i][x],R_IC_travel[i][x],R_IC_travel[i][z],brake_x,0,brake_x,1)[1] # Find where anti line crosses under/over measurement point

        AR_F_unsprung_CG_height = F_hub[z]+.5*constant.F.portal_height*cos(pitch_rad[i]+AR_F_pinion_rotation_rad) # Calculate CG of front axle
        AR_R_unsprung_CG_height = R_hub[z]+.5*constant.R.portal_height*cos(pitch_rad[i]+AR_R_pinion_rotation_rad) # Calculate CG of rear axle

        AR_F_unsprung_CG = (AR_B_CG[z]*V_sprung_mass+AR_R_unsprung_CG_height*constant.R.unsprung_mass)/(V_sprung_mass+constant.R.unsprung_mass)
        AR_R_unsprung_CG = (AR_B_CG[z]*V_sprung_mass+AR_F_unsprung_CG_height*constant.F.unsprung_mass)/(V_sprung_mass+constant.F.unsprung_mass)

        F_anti_CG = ((V_sprung_mass*AR_B_CG[z]-constant.F.unsprung_mass*AR_F_unsprung_CG)/(constant.V.mass-constant.F.unsprung_mass))
        R_anti_CG = ((V_sprung_mass*AR_B_CG[z]-constant.R.unsprung_mass*AR_R_unsprung_CG)/(constant.V.mass-constant.R.unsprung_mass))

        constant.pitch.F.anti_lift[i] = F_drive_intersect_z/F_anti_CG # Calculate front anti lift
        constant.pitch.F.anti_dive[i] = F_brake_intersect_z/F_anti_CG # Calculate front anti dive
        constant.pitch.R.anti_squat[i] = R_drive_intersect_z/R_anti_CG # Calculate rear anti squat
        constant.pitch.R.anti_lift[i] = R_brake_intersect_z/R_anti_CG # Calculate rear anti lift

        constant.pitch.body_roll_slope_dpd[i] = (F_roll_center_travel[i]-R_roll_center_travel[i])/constant.pitch.F.hub[i][x] # Calculate vehicle roll slope [distance rise/distance run]


    # Dynamics
    accel = [0,0,0,0,0]
    accel[0] = sin(constant.pitch.slope) # slope
    accel[1] = 1 # 1 G acceleration
    accel[2] = -1 # 1 G deceleration
    accel[3] = constant.pitch.acceleration # User inputed acceleration
    accel[4] = accel[0]+accel[3]# Combined

    for i in range(0,4):
        half_weight_transfer = .5*constant.V.CG_height*accel[i]*constant.V.mass/constant.V.wheelbase
        front_force = half_weight_transfer+constant.F.corner_sprung_weight
        rear_force = half_weight_transfer+constant.R.corner_sprung_weight
        if i == 0 | i == 4:
            front_force += constant.F.corner_sprung_weight*(cos(constant.V.pitch_slope)-1)
            rear_force += constant.R.corner_sprung_weight*(cos(constant.V.pitch_slope)-1)
        if accel[i] > 0:
            F_anti = travel.F.anti_lift.tolist()
            R_anti = travel.R.anti_squat.tolist()
            F_anti.insert(constant.F.slider_anti_lift[1],constant.F.slider_anti_lift[0])
            R_anti.insert(constant.R.slider_anti_squat[1],constant.R.slider_anti_squat[0])
        else:
            F_anti = travel.F.anti_dive.tolist()
            R_anti = travel.R.anti_lift.tolist()
            F_anti.insert(constant.F.slider_anti_dive[1],constant.F.slider_anti_dive[0])
            R_anti.insert(constant.R.slider_anti_lift[1],constant.R.slider_anti_lift[0])
        for j in range(0,S.sample_points*2+1+1):
            front_spring_force[j] = travel.F.wheel_force_chosen[j]+half_weight_transfer*(1-F_anti[j])-front_force
            rear_spring_force[j] = travel.R.wheel_force_chosen[j]+half_weight_transfer*(1-R_anti[j])-rear_force
        front_force_closest = front_spring_force[min(range(len(front_spring_force)), key = lambda i: abs(front_spring_force[i]))]
        rear_force_closest = rear_spring_force[min(range(len(rear_spring_force)), key = lambda i: abs(rear_spring_force[i]))]
        temp_list = travel.F.travel_dist.tolist()
        constant.pitch.front_travel_est[i] = max(min(temp_list[front_spring_force.index(front_force_closest)-1],constant.F.droop),constant.F.bump)
        temp_list = travel.R.travel_dist.tolist()
        constant.pitch.rear_travel_est[i] = max(min(temp_list[rear_spring_force.index(rear_force_closest)-1],constant.R.droop),constant.R.bump)
        constant.pitch.load_bias[i] = max(min(rear_force/(rear_force+front_force),0),1)

    output_processing_vehicle_pitch()