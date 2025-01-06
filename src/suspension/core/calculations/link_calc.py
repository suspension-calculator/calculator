# calculations/link_calc.py

def run_link_calc():

    from math import sqrt, acos, atan2, pi
    import numpy as np

    from suspension.io.variables import constant,travel,S,x,y,z
    from suspension.io.IO_Conversion.link_calc_IO import input_processing_link_calc, output_processing_link_calc

    from ..functions.distance_2d import dis2D
    from ..functions.distance_3d import dis3D
    #from ..functions.unit_conversion import in2mm, mm2in, kg2lb, lb2kg, kmh2mph, mph2kmh, npmm2lbpin, lbpin2npmm
    #from ..functions.floor_2_zero import floor2zero
    #from ..functions.rotation import rotate
    from ..functions.segment_seperation import SegSep
    from ..functions.line_intersection import LineIntersect
    from ..functions.link_travel import travel_solve
    from ..functions.travel_wheel_2_lca import wheel_2_lca
    from ..functions.axle_point_movement import on_axle_movement
    from ..functions.Y_equals_0 import ZeroY
    from ..functions.pinion_rotation import pinion_angle_change
    #from ..functions.input_conversion import convert2sae

    input_processing_link_calc()

    #------------------------------ Preallocation -------------------------------------
    class solver:
        lower_point = np.zeros(3)
        upper_point = np.zeros(3)
        CG_x = 0
        width_at_CG_x = 0
        class F:
            U_force = np.zeros(2*S.sample_points+1) # Preallocate front anti lift array
            L_force = np.zeros(2*S.sample_points+1) # Preallocate front anti lift array
            P_force = np.zeros(2*S.sample_points+1) # Preallocate front anti lift array
            bump_LA = 0
            droop_LA = 0
            wheel_contact = 0
            drive_x = 0
            brake_x = 0
            drive_intersect_z = 0
            brake_intersect_z = 0
            UF = np.zeros(3)
            LF = np.zeros(3)
            PF = np.zeros(3)

        class R:
            U_force = np.zeros(2*S.sample_points+1) # Preallocate front anti lift array
            L_force = np.zeros(2*S.sample_points+1) # Preallocate front anti lift array
            P_force = np.zeros(2*S.sample_points+1) # Preallocate front anti lift array
            bump_LA = 0
            droop_LA = 0
            wheel_contact = 0
            drive_x = 0
            brake_x = 0
            drive_intersect_z = 0
            brake_intersect_z = 0
            UF = np.zeros(3)
            LF = np.zeros(3)
            PF = np.zeros(3)

    travel.F.travel_dist = np.zeros(2*S.sample_points+1) # Preallocate front travel points array
    travel.R.travel_dist = np.zeros(2*S.sample_points+1) # Preallocate rear travel points array

    constant.F.percent_up_remaining = constant.F.bump/(abs(constant.F.bump)+abs(constant.F.droop))
    constant.R.percent_up_remaining = constant.R.bump/(abs(constant.R.bump)+abs(constant.R.droop))

    travel.F.UA = np.zeros((2*S.sample_points+1,3)) # Preallocate front upper travel matrix
    travel.F.LA = np.zeros((2*S.sample_points+1,3)) # Preallocate front lower travel matrix
    travel.R.UA = np.zeros((2*S.sample_points+1,3)) # Preallocate rear upper travel matrix
    travel.R.LA = np.zeros((2*S.sample_points+1,3)) # Preallocate rear lower travel matrix

    travel.F.hub = np.zeros((2*S.sample_points+1,3)) # Preallocate front hub center travel matrix
    travel.R.hub = np.zeros((2*S.sample_points+1,3)) # Preallocate rear hub center travel matrix
    if constant.F.panhard: travel.F.PA = np.zeros((2*S.sample_points+1,3)) # Preallocate front panhard travel matrix
    if constant.R.panhard: travel.R.PA = np.zeros((2*S.sample_points+1,3)) # Preallocate rear panhard travel matrix

    travel.F.pinion_rad = np.zeros(2*S.sample_points+1) # Preallocate front pinion angle change array
    travel.R.pinion_rad = np.zeros(2*S.sample_points+1) # Preallocate rear pinion angle change array

    travel.F.roll_slope_dpd = np.zeros(2*S.sample_points+1) # Preallocate front roll slope array
    travel.F.roll_center = np.zeros(2*S.sample_points+1) # Preallocate front roll center array
    travel.R.roll_slope_dpd = np.zeros(2*S.sample_points+1) # Preallocate rear roll slope array
    travel.R.roll_center = np.zeros(2*S.sample_points+1) # Preallocate rear roll center array

    travel.F.IC = np.zeros((2*S.sample_points+1,3)) # Preallocate front panhard travel matrix
    travel.R.IC = np.zeros((2*S.sample_points+1,3)) # Preallocate rear panhard travel matrix

    travel.F.anti_lift = np.zeros(2*S.sample_points+1) # Preallocate front anti lift array
    travel.F.anti_dive = np.zeros(2*S.sample_points+1) # Preallocate front anti dive array
    travel.R.anti_squat = np.zeros(2*S.sample_points+1) # Preallocate rear anti squat array
    travel.R.anti_lift = np.zeros(2*S.sample_points+1) # Preallocate rear anti lift array

    travel.F.panhard_transverse_movement = np.zeros(2*S.sample_points+1)
    travel.R.panhard_transverse_movement = np.zeros(2*S.sample_points+1)

    constant.F.LA_side_view_angle_range = [0,0]
    constant.F.LF_side_view_angle_range = [0,0]
    constant.F.UA_side_view_angle_range = [0,0]
    constant.F.UF_side_view_angle_range = [0,0]
    constant.R.LA_side_view_angle_range = [0,0]
    constant.R.LF_side_view_angle_range = [0,0]
    constant.R.UA_side_view_angle_range = [0,0]
    constant.R.UF_side_view_angle_range = [0,0]

    travel_F_force = np.zeros(2*S.sample_points+1) #aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

    #------------------------------ Constant variable setup -------------------------------------

    constant.F.hub = [constant.V.wheelbase,0,constant.F.tire_radius] # [x,y,z] of front hub center
    constant.R.hub = [0,0,constant.R.tire_radius] # [x,y,z] of rear hub center 

    constant.F.U_parallel = constant.F.UF[y] == constant.F.UA[y] and constant.F.U_count == 2 # If front 2 upper links and the are parallel, set flag
    constant.F.L_parallel = constant.F.LF[y] == constant.F.LA[y] # If front lower links are parallel, set flag
    constant.R.U_parallel = constant.R.UF[y] == constant.R.UA[y] and constant.R.U_count == 2 # If front 2 upper links and the are parallel, set flag
    constant.R.L_parallel = constant.R.LF[y] == constant.R.LA[y] # If rear lower links are parallel, set flag

    solver.upper_point = [0,0,0] # Define upper point for first pass
    solver.lower_point = [0,0,0] # Define lower point for first pass

    constant.F.tire_rate = (constant.F.tire_diameter*.5-constant.F.tire_radius)/(-1*constant.F.droop) # Find front tire spring rate [compression/travel]
    constant.R.tire_rate = (constant.R.tire_diameter*.5-constant.R.tire_radius)/(-1*constant.R.droop) # Find rear tire spring rate [compression/travel]

    constant.F.unsprung_CG_height = constant.F.hub[z]+.5*constant.F.portal_height # Calculate CG of front axle
    constant.R.unsprung_CG_height = constant.R.hub[z]+.5*constant.R.portal_height # Calculate CG of rear axle
    constant.V.sprung_mass = constant.V.mass - constant.F.unsprung_mass - constant.R.unsprung_mass

    constant.F.anti_CG = (constant.V.CG_height*constant.V.mass-constant.F.unsprung_mass*constant.F.unsprung_CG_height)/(constant.V.mass-constant.F.unsprung_mass) # Calculate Z value of CG not including front axle
    constant.R.anti_CG = (constant.V.CG_height*constant.V.mass-constant.R.unsprung_mass*constant.R.unsprung_CG_height)/(constant.V.mass-constant.R.unsprung_mass) # Calculate Z value of CG not including rear axle

    solver.CG_x = constant.V.weight_distribution*constant.V.wheelbase
    constant.V.sprung_cg[x] = (solver.CG_x*constant.V.mass-constant.V.wheelbase*constant.F.unsprung_mass)/(constant.V.mass-constant.R.unsprung_mass-constant.F.unsprung_mass)
    constant.V.sprung_cg[y] = 0
    constant.V.sprung_cg[z] = (constant.V.CG_height*constant.V.mass-constant.F.unsprung_mass*constant.F.unsprung_CG_height-constant.R.unsprung_mass*constant.R.unsprung_CG_height)/(constant.V.mass-constant.F.unsprung_mass-constant.R.unsprung_mass)

    #------------------------------ Maths -------------------------------------

    constant.F.U_length_2D = dis2D(constant.F.UF[x],constant.F.UF[z],constant.F.UA[x],constant.F.UA[z]) # Find front upper length in side view
    constant.F.L_length_2D = dis2D(constant.F.LF[x],constant.F.LF[z],constant.F.LA[x],constant.F.LA[z]) # Find front lower length in side view
    constant.F.F_sep_2D    = dis2D(constant.F.UF[x],constant.F.UF[z],constant.F.LF[x],constant.F.LF[z]) # Find front frame seperation distance in side view
    constant.F.A_sep_2D    = dis2D(constant.F.UA[x],constant.F.UA[z],constant.F.LA[x],constant.F.LA[z]) # Find front axle seperation distace in side view

    constant.F.U_length_3D = dis3D(constant.F.UF[x],constant.F.UF[y],constant.F.UF[z],constant.F.UA[x],constant.F.UA[y],constant.F.UA[z]) # Find 3D length of front upper axle links
    constant.F.L_length_3D = dis3D(constant.F.LF[x],constant.F.LF[y],constant.F.LF[z],constant.F.LA[x],constant.F.LA[y],constant.F.LA[z]) # Find 3D length of front lower axle links

    constant.R.U_length_2D = dis2D(constant.R.UF[x],constant.R.UF[z],constant.R.UA[x],constant.R.UA[z]) # Find rear upper length in side view
    constant.R.L_length_2D = dis2D(constant.R.LF[x],constant.R.LF[z],constant.R.LA[x],constant.R.LA[z]) # Find rear lower length in side view
    constant.R.F_sep_2D    = dis2D(constant.R.UF[x],constant.R.UF[z],constant.R.LF[x],constant.R.LF[z]) # Find rear frame seperation distance in side view
    constant.R.A_sep_2D    = dis2D(constant.R.UA[x],constant.R.UA[z],constant.R.LA[x],constant.R.LA[z]) # Find rear axle seperation distance in side view

    constant.R.U_length_3D = dis3D(constant.R.UF[x],constant.R.UF[y],constant.R.UF[z],constant.R.UA[x],constant.R.UA[y],constant.R.UA[z]) # Find 3D length of rear upper axle links
    constant.R.L_length_3D = dis3D(constant.R.LF[x],constant.R.LF[y],constant.R.LF[z],constant.R.LA[x],constant.R.LA[y],constant.R.LA[z]) # Find 3D length of rear lower axle links

    if constant.F.panhard:
        constant.F.P_length_3D = dis3D(constant.F.PF[x],constant.F.PF[y],constant.F.PF[z],constant.F.PA[x],constant.F.PA[y],constant.F.PA[z]) # Find 3D length of front panhard bar
        constant.F.P_length_2D = dis2D(constant.F.PF[y],constant.F.PF[z],constant.F.PA[y],constant.F.PA[z])
    if constant.R.panhard:
        constant.R.P_length_3D = dis3D(constant.R.PF[x],constant.R.PF[y],constant.R.PF[z],constant.R.PA[x],constant.R.PA[y],constant.R.PA[z]) # Find 3D length of rear panhard bar
        constant.F.P_length_2D = dis2D(constant.F.PF[y],constant.F.PF[z],constant.F.PA[y],constant.F.PA[z])

    solver.F.bump_LA = wheel_2_lca(constant.F.bump,constant.F.UA[x],constant.F.UA[z],constant.F.UF[x],constant.F.UF[z],constant.F.LA[x],constant.F.LA[z],constant.F.LF[x],constant.F.LF[z],constant.F.U_length_2D,constant.F.L_length_2D,constant.F.A_sep_2D,constant.F.F_sep_2D,constant.F.hub[x],constant.F.hub[z]) # Determine front bump LA travel for desired hub bump
    solver.F.droop_LA = wheel_2_lca(constant.F.droop,constant.F.UA[x],constant.F.UA[z],constant.F.UF[x],constant.F.UF[z],constant.F.LA[x],constant.F.LA[z],constant.F.LF[x],constant.F.LF[z],constant.F.U_length_2D,constant.F.L_length_2D,constant.F.A_sep_2D,constant.F.F_sep_2D,constant.F.hub[x],constant.F.hub[z]) # Determine front droop LA travel for desired hub droop
    solver.R.bump_LA = wheel_2_lca(constant.R.bump,constant.R.UA[x],constant.R.UA[z],constant.R.UF[x],constant.R.UF[z],constant.R.LA[x],constant.R.LA[z],constant.R.LF[x],constant.R.LF[z],constant.R.U_length_2D,constant.R.L_length_2D,constant.R.A_sep_2D,constant.R.F_sep_2D,constant.R.hub[x],constant.R.hub[z]) # Determine rear bump LA travel for desired hub bump
    solver.R.droop_LA = wheel_2_lca(constant.R.droop,constant.R.UA[x],constant.R.UA[z],constant.R.UF[x],constant.R.UF[z],constant.R.LA[x],constant.R.LA[z],constant.R.LF[x],constant.R.LF[z],constant.R.U_length_2D,constant.R.L_length_2D,constant.R.A_sep_2D,constant.R.F_sep_2D,constant.R.hub[x],constant.R.hub[z]) # Determine rear droop LA travel for desired hub droop

    h_F = -1*solver.F.droop_LA/S.sample_points # Sample point step distance for front droop
    h_R = -1*solver.R.droop_LA/S.sample_points # Sample point step distance for rear droop
    for i in range(0,S.sample_points):
       travel.F.travel_dist[i] = solver.F.droop_LA+i*h_F # Fill in droop portion of front travel points array
       travel.R.travel_dist[i] = solver.R.droop_LA+i*h_R # Fill in droop portion of rear travel point array

    h_F = solver.F.bump_LA/S.sample_points # Sample point step distance for front bump
    h_R = solver.R.bump_LA/S.sample_points # Sample point step distance for rear bump
    for i in range(S.sample_points+1,S.sample_points*2+1):
        travel.F.travel_dist[i] = (i-S.sample_points)*h_F # Fill in bump portion of front travel points array
        travel.R.travel_dist[i] = (i-S.sample_points)*h_R # Fill in bump portion of rear travel points array
        if i == 100:
            a=1

    for i in range(0,S.sample_points*2+1):
        #---------------------------------------------------------------------------------Movement Calculations---------------------------------------------------------------------------------
        travel.F.UA[i][x],travel.F.UA[i][z],travel.F.LA[i][x],travel.F.LA[i][z] = travel_solve(travel.F.travel_dist[i],constant.F.UA[x],constant.F.UA[z],constant.F.UF[x],constant.F.UF[z],constant.F.LA[x],constant.F.LA[z],constant.F.LF[x],constant.F.LF[z],constant.F.U_length_2D,constant.F.L_length_2D,constant.F.A_sep_2D,constant.F.F_sep_2D) # Calculate front arm arcs
        travel.R.UA[i][x],travel.R.UA[i][z],travel.R.LA[i][x],travel.R.LA[i][z] = travel_solve(travel.R.travel_dist[i],constant.R.UA[x],constant.R.UA[z],constant.R.UF[x],constant.R.UF[z],constant.R.LA[x],constant.R.LA[z],constant.R.LF[x],constant.R.LF[z],constant.R.U_length_2D,constant.R.L_length_2D,constant.R.A_sep_2D,constant.R.F_sep_2D) # Calculate rear arm arcs

        travel.F.UA[i][y] = constant.F.UA[y] # Y value does not change in side view travel
        travel.F.LA[i][y] = constant.F.LA[y] # Y value does not change in side view travel
        travel.R.UA[i][y] = constant.R.UA[y] # Y value does not change in side view travel
        travel.R.LA[i][y] = constant.R.LA[y] # Y value does not change in side view travel

        travel.F.pinion_rad[i] = pinion_angle_change(constant.F.UA[x], constant.F.UA[z], travel.F.UA[i][x], travel.F.UA[i][z], constant.F.LA[x], constant.F.LA[z], travel.F.LA[i][x], travel.F.LA[i][z]) # Calculate front pinion angle change
        travel.R.pinion_rad[i] = pinion_angle_change(constant.R.UA[x], constant.R.UA[z], travel.R.UA[i][x], travel.R.UA[i][z], constant.R.LA[x], constant.R.LA[z], travel.R.LA[i][x], travel.R.LA[i][z]) # Calculate rear pinion angle change

        travel.F.hub[i][x],travel.F.hub[i][z] = on_axle_movement(constant.F.hub[x],constant.F.hub[z],constant.F.LA[x],constant.F.LA[z],travel.F.LA[i][x],travel.F.LA[i][z],travel.F.pinion_rad[i]) # Calculate front hub center movement
        travel.R.hub[i][x],travel.R.hub[i][z] = on_axle_movement(constant.R.hub[x],constant.R.hub[z],constant.R.LA[x],constant.R.LA[z],travel.R.LA[i][x],travel.R.LA[i][z],travel.R.pinion_rad[i]) # Calculate rear hub center movement

        if constant.F.panhard: # If front panhard is used
            travel.F.PA[i][x],travel.F.PA[i][z] = on_axle_movement(constant.F.PA[x],constant.F.PA[z],constant.F.LA[x],constant.F.LA[z],travel.F.LA[i][x],travel.F.LA[i][z],travel.F.pinion_rad[i]) # Calculate front panhard X and Z movement
            travel.F.PA[i][y] = constant.F.PF[y]-sqrt(constant.F.P_length_3D**2-(constant.F.PF[x]-travel.F.PA[i][x])**2-(constant.F.PF[z]-travel.F.PA[i][z])**2) # Calculate front panhard Y movement
        if constant.R.panhard: # If rear panhard is used
            travel.R.PA[i][x],travel.R.PA[i][z] = on_axle_movement(constant.R.PA[x],constant.R.PA[z],constant.R.LA[x],constant.R.LA[z],travel.R.LA[i][x],travel.R.LA[i][z],travel.R.pinion_rad[i]) # Calculate rear panhard X and Z movement
            travel.R.PA[i][y] = constant.R.PF[y]-sqrt(constant.R.P_length_3D**2-(constant.R.PF[x]-travel.R.PA[i][x])**2-(constant.R.PF[z]-travel.R.PA[i][z])**2) # Calculate rear panhard Y movement

        #---------------------------------------------------------------------------------Roll Calculations---------------------------------------------------------------------------------

        if constant.F.panhard: # If front panhard exists, calculate roll stuff based on it
            solver.upper_point[x],solver.upper_point[z] = ZeroY(constant.F.PF[x],constant.F.PF[y],constant.F.PF[z],travel.F.PA[i][x],travel.F.PA[i][y],travel.F.PA[i][z]) # Upper point is where panhard crosses centerline, y=0
            if constant.F.L_parallel: # If front lowers are parallel, find lower point such that roll slope will be parallel to lower links
                solver.lower_point[x] = solver.upper_point[x]+constant.F.LF[x]-travel.F.LA[i][x] # Add lower link x component to upper point
                solver.lower_point[z] = solver.upper_point[z]+constant.F.LF[z]-travel.F.LA[i][z] # Add lower link z component to upper point
            else: # Solve for lower point
                solver.lower_point[x],solver.lower_point[z] = ZeroY(constant.F.LF[x],constant.F.LF[y],constant.F.LF[z],travel.F.LA[i][x],travel.F.LA[i][y],travel.F.LA[i][z]) # Find where lower links intersect in top view, y=0
        else:
            if constant.F.U_parallel and constant.F.L_parallel: # If front lowers are parallel and front uppers are parallel, create flat roll slope at ground level
                solver.upper_point[x] = 0
                solver.upper_point[z] = 0
                solver.lower_point[x] = 1
                solver.lower_point[z] = 0
            elif constant.F.U_parallel: # If front uppers are parallel, find upper point such that roll slope will be parallel to upper links
                solver.lower_point[x],solver.lower_point[z] = ZeroY(constant.F.LF[x],constant.F.LF[y],constant.F.LF[z],travel.F.LA[i][x],travel.F.LA[i][y],travel.F.LA[i][z]) # Find where lower links intersect in top view, y=0
                solver.upper_point[x] = solver.lower_point[x]+constant.F.LF[x]-travel.F.UA[i][x] # Add upper link x component to lower point
                solver.upper_point[z] = solver.lower_point[z]+constant.F.LF[z]-travel.F.UA[i][z] # Add upper link z component to lower point
            elif constant.F.L_parallel: # If front lowers are parallel, find lower point such that roll slope will be parallel to lower links
                solver.upper_point[x],solver.upper_point[z] = ZeroY(constant.F.UF[x],constant.F.UF[y],constant.F.UF[z],travel.F.UA[i][x],travel.F.UA[i][y],travel.F.UA[i][z]) # Find where upper links intersect in top view, y=0
                solver.lower_point[x] = solver.upper_point[x]+constant.F.LF[x]-travel.F.LA[i][x] # Add lower link x component to upper point
                solver.lower_point[z] = solver.upper_point[z]+constant.F.LF[z]-travel.F.LA[i][z] # Add lower link z component to upper point
            else:
                solver.upper_point[x],solver.upper_point[z] = ZeroY(constant.F.UF[x],constant.F.UF[y],constant.F.UF[z],travel.F.UA[i][x],travel.F.UA[i][y],travel.F.UA[i][z]) # Find where upper links intersect in top view, y=0
                solver.lower_point[x],solver.lower_point[z] = ZeroY(constant.F.LF[x],constant.F.LF[y],constant.F.LF[z],travel.F.LA[i][x],travel.F.LA[i][y],travel.F.LA[i][z]) # Find where lower links intersect in top view, y=0
        travel.F.roll_slope_dpd[i] = (solver.upper_point[z]-solver.lower_point[z])/(solver.upper_point[x]-solver.lower_point[x]) # Calculate front roll slope [distance rise/distance run]
        travel.F.roll_center[i] = LineIntersect(solver.upper_point[x],solver.upper_point[z],solver.lower_point[x],solver.lower_point[z],travel.F.hub[i][x],0,travel.F.hub[i][x],1)[1] # Find front roll center by using intersect between roll slope and vertical line at the wheel hubs

        if constant.R.panhard: # If rear panhard exists, calculate roll stuff based on it
            solver.upper_point[x],solver.upper_point[z] = ZeroY(constant.R.PF[x],constant.R.PF[y],constant.R.PF[z],travel.R.PA[i][x],travel.R.PA[i][y],travel.R.PA[i][z]) # Upper point is where panhard crosses centerline, y=0
            if constant.R.L_parallel: # If rear lowers are parallel, find lower point such that roll slope will be parallel to lower links
                solver.lower_point[x] = solver.upper_point[x]+constant.R.LF[x]-travel.R.LA[i][x] # Add lower link x component to upper point
                solver.lower_point[z] = solver.upper_point[z]+constant.R.LF[z]-travel.R.LA[i][z] # Add lower link z component to upper point
            else: # Solve for lower point
                solver.lower_point[x],solver.lower_point[z] = ZeroY(constant.R.LF[x],constant.R.LF[y],constant.R.LF[z],travel.R.LA[i][x],travel.R.LA[i][y],travel.R.LA[i][z]) # Find where lower links intersect in top view, y=0
        else:
            if constant.R.U_parallel and constant.R.L_parallel: # If rear lowers are parallel and rear uppers are parallel, create flat roll slope at ground level
                solver.upper_point[x] = 0
                solver.upper_point[z] = 0
                solver.lower_point[x] = 1
                solver.lower_point[z] = 0
            elif constant.R.U_parallel: # If rear uppers are parallel, find upper point such that roll slope will be parallel to upper links
                solver.lower_point[x],solver.lower_point[z] = ZeroY(constant.R.LF[x],constant.R.LF[y],constant.R.LF[z],travel.R.LA[i][x],travel.R.LA[i][y],travel.R.LA[i][z]) # Find where lower links intersect in top view, y=0
                solver.upper_point[x] = solver.lower_point[x]+constant.R.LF[x]-travel.R.UA[i][x] # Add upper link x component to lower point
                solver.upper_point[z] = solver.lower_point[z]+constant.R.LF[z]-travel.R.UA[i][z] # Add upper link z component to lower point
            elif constant.R.L_parallel: # If rear lowers are parallel, find lower point such that roll slope will be parallel to lower links
                solver.upper_point[x],solver.upper_point[z] = ZeroY(constant.R.UF[x],constant.R.UF[y],constant.R.UF[z],travel.R.UA[i][x],travel.R.UA[i][y],travel.R.UA[i][z]) # Find where upper links intersect in top view, y=0
                solver.lower_point[x] = solver.upper_point[x]+constant.R.LF[x]-travel.R.LA[i][x] # Add lower link x component to upper point
                solver.lower_point[z] = solver.upper_point[z]+constant.R.LF[z]-travel.R.LA[i][z] # Add lower link z component to upper point
            else:
                solver.upper_point[x],solver.upper_point[z] = ZeroY(constant.R.UF[x],constant.R.UF[y],constant.R.UF[z],travel.R.UA[i][x],travel.R.UA[i][y],travel.R.UA[i][z]) # Find where upper links intersect in top view, y=0
                solver.lower_point[x],solver.lower_point[z] = ZeroY(constant.R.LF[x],constant.R.LF[y],constant.R.LF[z],travel.R.LA[i][x],travel.R.LA[i][y],travel.R.LA[i][z]) # Find where lower links intersect in top view, y=0
        travel.R.roll_slope_dpd[i] = (solver.upper_point[z]-solver.lower_point[z])/(solver.upper_point[x]-solver.lower_point[x]) # Calculate front roll slope [distance rise/distance run]
        travel.R.roll_center[i] = LineIntersect(solver.upper_point[x],solver.upper_point[z],solver.lower_point[x],solver.lower_point[z],travel.R.hub[i][x],0,travel.R.hub[i][x],1)[1] # Find rear roll center by using intersect between roll slope and vertical line at the wheel hubs

        #---------------------------------------------------------------------------------Anti Calculations---------------------------------------------------------------------------------

        if S.simulate_tire_loading: # If tire loading is being simulated
            solver.F.wheel_contact = travel.F.hub[i][z]-(constant.F.tire_diameter*.5-constant.F.tire_rate*(travel.F.travel_dist[i]-constant.F.droop)) # Calculate front contanct point
            solver.R.wheel_contact = travel.R.hub[i][z]-(constant.R.tire_diameter*.5-constant.R.tire_rate*(travel.R.travel_dist[i]-constant.R.droop)) # Calculate rear contanct point
        else:
            solver.F.wheel_contact = travel.F.hub[i][z]-constant.F.tire_radius # Calculate front contanct point
            solver.R.wheel_contact = travel.R.hub[i][z]-constant.R.tire_radius # Calculate rear contanct point

        if (constant.F.LF[z]-travel.F.LA[i][z])/(constant.F.LF[x]-travel.F.LA[i][x]) == (constant.F.UF[z]-travel.F.UA[i][z])/(constant.F.UF[x]-travel.F.UA[i][x]): # If slope of the front lower links is the same as the slope of the front upper links
            travel.F.IC[i][x] = travel.F.hub[i][x] + (constant.F.LF[x]-travel.F.LA[i][x]) # Define point on wheel contact to infinite IC line
            travel.F.IC[i][z] = solver.F.wheel_contact + (constant.F.LF[z]-travel.F.LA[i][z]) # Define point on wheel contact to infinite IC line
        else:
            travel.F.IC[i][x],travel.F.IC[i][z] = LineIntersect(constant.F.LF[x],constant.F.LF[z],travel.F.LA[i][x],travel.F.LA[i][z],constant.F.UF[x],constant.F.UF[z],travel.F.UA[i][x],travel.F.UA[i][z]) # Find intersection of upper and lower links in side view
        if (constant.R.LF[z]-travel.R.LA[i][z])/(constant.R.LF[x]-travel.R.LA[i][x]) == (constant.R.UF[z]-travel.R.UA[i][z])/(constant.R.UF[x]-travel.R.UA[i][x]): # If slope of the rear lower links is the same as the slope of the rear upper links
            travel.R.IC[i][x] = travel.R.hub[i][x] + (constant.R.LF[x]-travel.R.LA[i][x]) # Define point on wheel contact to infinite IC line
            travel.R.IC[i][z] = solver.R.wheel_contact + (constant.R.LF[z]-travel.R.LA[i][z]) # Define point on wheel contact to infinite IC line
        else:
            travel.R.IC[i][x],travel.R.IC[i][z] = LineIntersect(constant.R.LF[x],constant.R.LF[z],travel.R.LA[i][x],travel.R.LA[i][z],constant.R.UF[x],constant.R.UF[z],travel.R.UA[i][x],travel.R.UA[i][z]) # Find intersection of upper and lower links in side view

        solver.F.drive_x = travel.F.hub[i][x]*(1-constant.V.drive_bias) # Find front anti lift x measument point, accounting for change in wheelbase
        solver.F.brake_x = travel.F.hub[i][x]*(1-constant.V.brake_bias) # Find front anti dive x measument point, accounting for change in wheelbase
        solver.R.drive_x = (constant.V.wheelbase-travel.R.hub[i][x])*(1-constant.V.drive_bias)+travel.R.hub[i][x] # Find rear anti squat x measument point, accounting for change in wheelbase
        solver.R.brake_x = (constant.V.wheelbase-travel.R.hub[i][x])*(1-constant.V.brake_bias)+travel.R.hub[i][x] # Find rear anti lift x measument point, accounting for change in wheelbase

        solver.F.drive_intersect_z = LineIntersect(travel.F.hub[i][x],solver.F.wheel_contact,travel.F.IC[i][x],travel.F.IC[i][z],solver.F.drive_x,0,solver.F.drive_x,1)[1] # Find where anti line crosses under/over measurement point
        solver.F.brake_intersect_z = LineIntersect(travel.F.hub[i][x],solver.F.wheel_contact,travel.F.IC[i][x],travel.F.IC[i][z],solver.F.brake_x,0,solver.F.brake_x,1)[1] # Find where anti line crosses under/over measurement point
        solver.R.drive_intersect_z = LineIntersect(travel.R.hub[i][x],solver.R.wheel_contact,travel.R.IC[i][x],travel.R.IC[i][z],solver.R.drive_x,0,solver.R.drive_x,1)[1] # Find where anti line crosses under/over measurement point
        solver.R.brake_intersect_z = LineIntersect(travel.R.hub[i][x],solver.R.wheel_contact,travel.R.IC[i][x],travel.R.IC[i][z],solver.R.brake_x,0,solver.R.brake_x,1)[1] # Find where anti line crosses under/over measurement point

        travel.F.anti_lift[i] = (solver.F.drive_intersect_z-solver.F.wheel_contact)/(constant.F.anti_CG-solver.F.wheel_contact) # Calculate front anti lift
        travel.F.anti_dive[i] = (solver.F.brake_intersect_z-solver.F.wheel_contact)/(constant.F.anti_CG-solver.F.wheel_contact) # Calculate front anti dive
        travel.R.anti_squat[i]= (solver.R.drive_intersect_z-solver.R.wheel_contact)/(constant.R.anti_CG-solver.R.wheel_contact) # Calculate rear anti squat
        travel.R.anti_lift[i] = (solver.R.brake_intersect_z-solver.R.wheel_contact)/(constant.R.anti_CG-solver.R.wheel_contact) # Calculate rear anti lift
        #---------------------------------------------------------------------------------Force Calculations---------------------------------------------------------------------------------
        solver.F.U_force[i] = (-1*constant.V.mass*constant.V.acceleration*travel.F.LA[i][z]/constant.F.U_count)/((constant.F.UF[x]-travel.F.UA[i][x])/constant.F.U_length_3D*(travel.F.UA[i][z]-travel.F.LA[i][z])+(constant.F.UF[z]-travel.F.UA[i][z])/constant.F.U_length_3D*(travel.F.UA[i][x]-constant.V.wheelbase)) # Calculate force in front upper link
        solver.F.L_force[i] = (constant.V.mass*constant.V.acceleration*travel.F.UA[i][z]/2)/((constant.F.LF[x]-travel.F.LA[i][x])/constant.F.L_length_3D*(travel.F.UA[i][z]-travel.F.LA[i][z])+(constant.F.LF[z]-travel.F.LA[i][z])/constant.F.L_length_3D*(travel.F.LA[i][x]-constant.V.wheelbase)) # Calculate force in front lower link
        solver.R.U_force[i] = (constant.V.mass*constant.V.acceleration*travel.R.LA[i][z]/constant.R.U_count)/((constant.R.UF[x]-travel.R.UA[i][x])/constant.R.U_length_3D*(travel.R.UA[i][z]-travel.R.LA[i][z])+(constant.R.UF[z]-travel.R.UA[i][z])/constant.R.U_length_3D*travel.R.UA[i][x]) # Calculate force in rear upper link
        solver.R.L_force[i] = (-1*constant.V.mass*constant.V.acceleration*travel.R.UA[i][z]/2)/((constant.R.LF[x]-travel.R.LA[i][x])/constant.R.L_length_3D*(travel.R.UA[i][z]-travel.R.LA[i][z])+(constant.R.LF[z]-travel.R.LA[i][z])/constant.R.L_length_3D*travel.R.LA[i][x]) # Calculate force in rear lower link
        if constant.F.panhard: solver.F.P_force[i] = abs(constant.V.mass*constant.V.transverse_acceleration/((constant.F.PF[y]-travel.F.PA[i][y])/constant.F.P_length_3D)) # Calculate force in front panhard link
        if constant.R.panhard: solver.R.P_force[i] = abs(constant.V.mass*constant.V.transverse_acceleration/((constant.R.PF[y]-travel.R.PA[i][y])/constant.R.P_length_3D)) # Calculate force in rear panhard link

        min_distance = SegSep(constant.F.LF[x],constant.F.LF[y],constant.F.LF[z],travel.F.LA[i][x],travel.F.LA[i][y],travel.F.LA[i][z],constant.F.UF[x],constant.F.UF[y],constant.F.UF[z],travel.F.UA[i][x],travel.F.UA[i][y],travel.F.UA[i][z])
        if min_distance < constant.F.min_distance: constant.F.min_distance = min_distance

        min_distance = SegSep(constant.R.LF[x],constant.R.LF[y],constant.R.LF[z],travel.R.LA[i][x],travel.R.LA[i][y],travel.R.LA[i][z],constant.R.UF[x],constant.R.UF[y],constant.R.UF[z],travel.R.UA[i][x],travel.R.UA[i][y],travel.R.UA[i][z])
        if min_distance < constant.R.min_distance: constant.R.min_distance = min_distance

        if constant.F.panhard: travel.F.panhard_transverse_movement[i] = constant.F.PA[y]-travel.F.PA[i][y]
        if constant.R.panhard: travel.R.panhard_transverse_movement[i] = constant.R.PA[y]-travel.R.PA[i][y]

        solver.F.UF[x],solver.F.UF[z] = on_axle_movement(constant.F.UF[x],constant.F.UF[z],constant.F.LA[x],constant.F.LA[z],travel.F.LA[i][x],travel.F.LA[i][z],travel.F.pinion_rad[i]) # Calculate front upper frame relative location
        solver.F.LF[x],solver.F.LF[z] = on_axle_movement(constant.F.LF[x],constant.F.LF[z],constant.F.LA[x],constant.F.LA[z],travel.F.LA[i][x],travel.F.LA[i][z],travel.F.pinion_rad[i]) # Calculate front lower frame relative location
        solver.R.UF[x],solver.R.UF[z] = on_axle_movement(constant.R.UF[x],constant.R.UF[z],constant.R.LA[x],constant.R.LA[z],travel.R.LA[i][x],travel.R.LA[i][z],travel.R.pinion_rad[i]) # Calculate front upper frame relative location
        solver.R.LF[x],solver.R.LF[z] = on_axle_movement(constant.R.LF[x],constant.R.LF[z],constant.R.LA[x],constant.R.LA[z],travel.R.LA[i][x],travel.R.LA[i][z],travel.R.pinion_rad[i]) # Calculate front lower frame relative location
        if constant.F.panhard: solver.F.PF[x],solver.F.PF[z] = on_axle_movement(constant.F.UF[x],constant.F.UF[z],constant.F.LA[x],constant.F.LA[z],travel.F.LA[i][x],travel.F.LA[i][z],travel.F.pinion_rad[i]) # Calculate front panhard frame relative location
        if constant.R.panhard: solver.R.PF[x],solver.R.PF[z] = on_axle_movement(constant.F.UF[x],constant.R.UF[z],constant.R.LA[x],constant.R.LA[z],travel.R.LA[i][x],travel.R.LA[i][z],travel.R.pinion_rad[i]) # Calculate rear panhard frame relative location
    
        angle = atan2(travel.F.LA[i][z]-solver.F.LF[z],travel.F.LA[i][x]-solver.F.LF[x])-atan2(travel.F.LA[i][z]-constant.F.LF[z],travel.F.LA[i][x]-constant.F.LF[x])
        constant.F.LA_side_view_angle_range = [min(angle,constant.F.LA_side_view_angle_range[0]),max(angle,constant.F.LA_side_view_angle_range[1])]
        angle = atan2(travel.F.LA[i][z] - constant.F.LF[z], travel.F.LA[i][x] - constant.F.LF[x]) - atan2(constant.F.LA[z] - constant.F.LF[z], constant.F.LA[x] - constant.F.LF[x])
        constant.F.LF_side_view_angle_range = [min(angle,constant.F.LF_side_view_angle_range[0]),max(angle,constant.F.LF_side_view_angle_range[1])]
        angle = atan2(travel.F.UA[i][z]-solver.F.UF[z],travel.F.UA[i][x]-solver.F.UF[x])-atan2(travel.F.UA[i][z]-constant.F.UF[z],travel.F.UA[i][x]-constant.F.UF[x])
        constant.F.UA_side_view_angle_range = [min(angle,constant.F.UA_side_view_angle_range[0]),max(angle,constant.F.UA_side_view_angle_range[1])]
        angle = atan2(travel.F.UA[i][z] - constant.F.UF[z], travel.F.UA[i][x] - constant.F.UF[x]) - atan2(constant.F.UA[z] - constant.F.UF[z], constant.F.UA[x] - constant.F.UF[x])
        constant.F.UF_side_view_angle_range = [min(angle,constant.F.UF_side_view_angle_range[0]),max(angle,constant.F.UF_side_view_angle_range[1])]
        if constant.F.panhard:
            angle = atan2(solver.F.PF[z]-travel.F.PA[i][z],solver.F.PF[y]-travel.F.PA[i][y]) - atan2(constant.F.PF[z]-travel.F.PA[i][z],constant.F.PF[y]-travel.F.PA[i][y])
            constant.F.PA_front_view_angle_range = [min(angle,constant.F.PA_front_view_angle_range[0]),max(angle,constant.F.PA_front_view_angle_range[1])]
            angle = atan2(solver.F.PF[y]-travel.F.PA[i][y],solver.F.PF[x]-travel.F.PA[i][x]) - atan2(constant.F.PF[y]-travel.F.PA[i][y],constant.F.PF[x]-travel.F.PA[i][x])
            constant.F.PA_top_view_angle_range = [min(angle,constant.F.PA_top_view_angle_range[0]),max(angle,constant.F.PA_top_view_angle_range[1])]
            angle = atan2(travel.F.PA[i][z]-constant.F.PF[z],travel.F.PA[i][y]-constant.F.PF[y]) - atan2(constant.F.PA[z]-constant.F.PF[z],constant.F.PA[y]-constant.F.PF[y])
            constant.F.PF_front_view_angle_range = [min(angle,constant.F.PF_front_view_angle_range[0]),max(angle,constant.F.PF_front_view_angle_range[1])]
            angle = atan2(travel.F.PA[i][y]-constant.F.PF[y],travel.F.PA[i][x]-constant.F.PF[x]) - atan2(constant.F.PA[y]-constant.F.PF[y],constant.F.PA[x]-constant.F.PF[x])
            constant.F.PF_top_view_angle_range = [min(angle,constant.F.PF_top_view_angle_range[0]),max(angle,constant.F.PF_top_view_angle_range[1])]

        angle = atan2(solver.R.LF[z]-travel.R.LA[i][z],solver.R.LF[x]-travel.R.LA[i][x])-atan2(constant.R.LF[z]-travel.R.LA[i][z],constant.R.LF[x]-travel.R.LA[i][x])
        constant.R.LA_side_view_angle_range = [min(angle,constant.R.LA_side_view_angle_range[0]),max(angle,constant.R.LA_side_view_angle_range[1])]
        angle = atan2(constant.R.LF[z]-travel.R.LA[i][z], constant.R.LF[x]-travel.R.LA[i][x]) - atan2(constant.R.LF[z]-constant.R.LA[z], constant.R.LF[x]-constant.R.LA[x])
        constant.R.LF_side_view_angle_range = [min(angle,constant.R.LF_side_view_angle_range[0]),max(angle,constant.R.LF_side_view_angle_range[1])]
        angle = atan2(solver.R.UF[z]-travel.R.UA[i][z],solver.R.UF[x]-travel.R.UA[i][x])-atan2(constant.R.UF[z]-travel.R.UA[i][z],constant.R.UF[x]-travel.R.UA[i][x])
        constant.R.UA_side_view_angle_range = [min(angle,constant.R.UA_side_view_angle_range[0]),max(angle,constant.R.UA_side_view_angle_range[1])]
        angle = atan2(constant.R.UF[z]-travel.R.UA[i][z], constant.R.UF[x]-travel.R.UA[i][x]) - atan2(constant.R.UF[z]-constant.R.UA[z], constant.R.UF[x]-constant.R.UA[x])
        constant.R.UF_side_view_angle_range = [min(angle,constant.R.UF_side_view_angle_range[0]),max(angle,constant.R.UF_side_view_angle_range[1])]
        if constant.R.panhard:
            angle = atan2(solver.R.PF[z]-travel.R.PA[i][z],solver.R.PF[y]-travel.R.PA[i][y]) - atan2(constant.R.PF[z]-travel.R.PA[i][z],constant.R.PF[y]-travel.R.PA[i][y])
            constant.R.PA_rear_view_angle_range = [min(angle,constant.R.PA_rear_view_angle_range[0]),max(angle,constant.R.PA_rear_view_angle_range[1])]
            angle = atan2(solver.R.PF[y]-travel.R.PA[i][y],solver.R.PF[x]-travel.R.PA[i][x]) - atan2(constant.R.PF[y]-travel.R.PA[i][y],constant.R.PF[x]-travel.R.PA[i][x])
            constant.R.PA_top_view_angle_range = [min(angle,constant.R.PA_top_view_angle_range[0]),max(angle,constant.R.PA_top_view_angle_range[1])]
            angle = atan2(travel.R.PA[i][z]-constant.R.PF[z],travel.R.PA[i][y]-constant.R.PF[y]) - atan2(constant.R.PA[z]-constant.R.PF[z],constant.R.PA[y]-constant.R.PF[y])
            constant.R.PF_rear_view_angle_range = [min(angle,constant.R.PF_rear_view_angle_range[0]),max(angle,constant.R.PF_rear_view_angle_range[1])]
            angle = atan2(travel.R.PA[i][y]-constant.R.PF[y],travel.R.PA[i][x]-constant.R.PF[x]) - atan2(constant.R.PA[y]-constant.R.PF[y],constant.R.PA[x]-constant.R.PF[x])
            constant.R.PF_top_view_angle_range = [min(angle,constant.R.PF_top_view_angle_range[0]),max(angle,constant.R.PF_top_view_angle_range[1])]

    constant.F.U_top_view_angle = abs(atan2(constant.F.UA[y]-constant.F.UF[y],constant.F.UA[x]-constant.F.UF[x]))
    constant.F.L_top_view_angle = abs(atan2(constant.F.LA[y]-constant.F.LF[y],constant.F.LA[x]-constant.F.LF[x]))
    constant.R.U_top_view_angle = abs(atan2(constant.R.UA[y]-constant.R.UF[y],constant.R.UA[x]-constant.R.UF[x]))
    constant.F.L_top_view_angle = abs(atan2(constant.R.LA[y]-constant.R.LF[y],constant.R.LA[x]-constant.R.LF[x]))

    constant.V.roll_slope_dpd = (travel.F.roll_center[S.sample_points]-travel.R.roll_center[S.sample_points])/(constant.F.hub[x]-constant.R.hub[x]) # Calculate vehicle roll slope [distance rise/distance run]

    constant.F.U_force = max(solver.F.U_force,key=abs) # Find most extreme force on front upper link
    constant.F.L_force = max(solver.F.L_force,key=abs) # Find most extreme force on front lower link
    constant.R.U_force = max(solver.R.U_force,key=abs) # Find most extreme force on rear upper link
    constant.R.L_force = max(solver.R.L_force,key=abs) # Find most extreme force on rear lower link
    if constant.F.panhard: constant.F.P_force = max(solver.F.P_force,key=abs) # Find most extreme force on front panhard link
    if constant.R.panhard: constant.R.P_force = max(solver.R.P_force,key=abs) # Find most extreme force on rear panhard link

    constant.F.U_converge = abs(acos(((constant.F.UA[x]-constant.F.UF[x])**2-(constant.F.UA[y]-constant.F.UF[y])**2)/(dis2D(constant.F.UA[x],constant.F.UA[y],constant.F.UF[x],constant.F.UF[y])**2)))
    constant.F.L_converge = abs(acos(((constant.F.LA[x]-constant.F.LF[x])**2-(constant.F.LA[y]-constant.F.LF[y])**2)/(dis2D(constant.F.LA[x],constant.F.LA[y],constant.F.LF[x],constant.F.LF[y])**2)))
    if (constant.F.UA[y]-constant.F.UF[y])/abs(constant.F.UA[y]-constant.F.UF[y]) == (constant.F.LA[y]-constant.F.LF[y])/abs(constant.F.LA[y]-constant.F.LF[y]):
        constant.F.total_converge = abs(constant.F.U_converge-constant.F.L_converge)
    else:
        constant.F.total_converge = constant.F.U_converge+constant.F.L_converge

    constant.R.U_converge = abs(acos(((constant.R.UA[x]-constant.R.UF[x])**2-(constant.R.UA[y]-constant.R.UF[y])**2)/(dis2D(constant.R.UA[x],constant.R.UA[y],constant.R.UF[x],constant.R.UF[y])**2)))
    constant.R.L_converge = abs(acos(((constant.R.LA[x]-constant.R.LF[x])**2-(constant.R.LA[y]-constant.R.LF[y])**2)/(dis2D(constant.R.LA[x],constant.R.LA[y],constant.R.LF[x],constant.R.LF[y])**2)))
    if (constant.R.UA[y]-constant.R.UF[y])/abs(constant.R.UA[y]-constant.R.UF[y]) == (constant.R.LA[y]-constant.R.LF[y])/abs(constant.R.LA[y]-constant.R.LF[y]):
        constant.R.total_converge = abs(constant.R.U_converge-constant.R.L_converge)
    else:
        constant.R.total_converge = constant.R.U_converge+constant.R.L_converge

    if constant.F.panhard:
        constant.F.U_converge_point[x],constant.F.U_converge_point[z] = ZeroY(constant.F.PA[x],constant.F.PA[y],constant.F.PA[z],constant.F.PF[x],constant.F.PF[y],constant.F.PF[z])
    else:
        constant.F.U_converge_point[x],constant.F.U_converge_point[z] = ZeroY(constant.F.UF[x],constant.F.UF[y],constant.F.UF[z],constant.F.UA[x],constant.F.UA[y],constant.F.UA[z])
    constant.F.L_converge_point[x],constant.F.L_converge_point[z] = ZeroY(constant.F.LF[x],constant.F.LF[y],constant.F.LF[z],constant.F.LA[x],constant.F.LA[y],constant.F.LA[z])
    if constant.R.panhard:
        constant.R.U_converge_point[x],constant.R.U_converge_point[z] = ZeroY(constant.R.PA[x],constant.R.PA[y],constant.R.PA[z],constant.R.PF[x],constant.R.PF[y],constant.R.PF[z])
    else:
        constant.R.U_converge_point[x],constant.R.U_converge_point[z] = ZeroY(constant.R.UF[x],constant.R.UF[y],constant.R.UF[z],constant.R.UA[x],constant.R.UA[y],constant.R.UA[z])
    constant.R.L_converge_point[x],constant.R.L_converge_point[z] = ZeroY(constant.R.LF[x],constant.R.LF[y],constant.R.LF[z],constant.R.LA[x],constant.R.LA[y],constant.R.LA[z])

    constant.F.U_top_view_angle = abs(constant.F.U_converge)/2
    constant.F.L_top_view_angle = abs(constant.F.L_converge)/2
    constant.R.U_top_view_angle = abs(constant.R.U_converge)/2
    constant.R.L_top_view_angle = abs(constant.R.L_converge)/2

    constant.V.climb_angle = .5*pi-atan2(constant.V.CG_height,solver.CG_x)
    constant.V.descent_angle = .5*pi-atan2(constant.V.CG_height,constant.V.wheelbase-solver.CG_x)
    solver.width_at_CG_x = (constant.F.track_width+constant.F.tire_width)/2-((constant.F.track_width+constant.F.tire_width)/2-(constant.R.track_width+constant.R.tire_width)/2)/constant.V.wheelbase*solver.CG_x
    constant.V.side_roll_angle = .5*pi-atan2(constant.V.CG_height,solver.width_at_CG_x)

    constant.F.sprung_CG_height_above_roll_center = constant.V.sprung_cg[z]-travel.F.roll_center[S.sample_points]
    constant.R.sprung_CG_height_above_roll_center = constant.V.sprung_cg[z]-travel.R.roll_center[S.sample_points]
    constant.V.sprung_CG_height_above_roll_axis = abs((constant.V.wheelbase-0)*(travel.R.roll_center[S.sample_points]-constant.V.sprung_cg[z])-(0-constant.V.sprung_cg[x]*(travel.F.roll_center[S.sample_points]-travel.R.roll_center[S.sample_points])))/sqrt((constant.V.wheelbase-0)**2+(travel.F.roll_center[S.sample_points]-travel.R.roll_center[S.sample_points])**2)

    output_processing_link_calc()

    del solver
    del angle
    del h_F
    del h_R
    del min_distance
    del i