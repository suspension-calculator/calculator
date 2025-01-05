def run_driveshaft():
    from math import acos, sqrt, sin, cos, tan
    import numpy as np
    from Functions.axle_point_movement import on_axle_movement
    from Functions.distance_3d import dis3D

    from VariableIO.variables import constant, travel, S, x,y,z
    from VariableIO.IO_Conversion.driveshaft_IO import input_processing_driveshaft, output_processing_driveshaft

    input_processing_driveshaft()

    #------------------------------ Preallocation -------------------------------------
    class solver:
        pinion_travel = np.zeros(3) # Preallocate pinion travel x,y,z
        driveshaft_delta = np.zeros(3) # Preallocate driveshaft delta x,y,z
        pinion_vector = np.zeros(3)
        class F:
            T_case_vector = np.zeros(3)
        class R:
            T_case_vector = np.zeros(3)

    travel.F.driveshaft_length = np.zeros(2*S.sample_points+1) # Preallocate front driveshaft lengths
    travel.R.driveshaft_length = np.zeros(2*S.sample_points+1) # Preallocate rear driveshaft lengths
    travel.F.T_case_U_joint_angle_rad = np.zeros(2*S.sample_points+1) # Preallocate front T-case U-joint angle during travel
    travel.R.T_case_U_joint_angle_rad = np.zeros(2*S.sample_points+1) # Preallocate rear T-case U-joint angle during travel

    travel.F.pinion_U_joint_angle_rad = np.zeros(2*S.sample_points+1) # Preallocate front pinion U-joint angle during travel
    travel.R.pinion_U_joint_angle_rad = np.zeros(2*S.sample_points+1) # Preallocate rear pinion U-joint angle during travel

    travel.F.pinion_angle_rad = np.zeros(2*S.sample_points+1)
    travel.R.pinion_angle_rad = np.zeros(2*S.sample_points+1)

    temp1 = np.zeros(2*S.sample_points+1)
    temp2 = np.zeros(2*S.sample_points+1)

    #------------------------------ Maths -------------------------------------
    if constant.F.pinion_location_method == 0: # calculate x,y,z from hypoid offset and pinion length
        constant.F.pinion[x] = constant.V.wheelbase - cos(constant.F.caster)*constant.F.portal_height + (constant.F.pinion_hypoid*cos(constant.F.pinion_angle)+constant.F.pinion_length*sin(constant.F.pinion_angle))
        constant.F.pinion[z] = constant.F.tire_radius + sin(constant.F.caster)*constant.F.portal_height + (-constant.F.pinion_length*cos(constant.F.pinion_angle)+constant.F.pinion_hypoid*sin(constant.F.pinion_angle))

    if constant.R.pinion_location_method == 0: # calculate x,y,z from hypoid offset and pinion length
        constant.R.pinion[x] = cos(constant.R.caster)*constant.R.portal_height + (constant.R.pinion_hypoid*cos(constant.R.pinion_angle)-constant.R.pinion_length*sin(constant.R.pinion_angle))
        constant.R.pinion[z] = constant.R.tire_radius+sin(constant.R.caster)*constant.R.portal_height + (constant.R.pinion_length*cos(constant.R.pinion_angle)+constant.R.pinion_hypoid*sin(constant.R.pinion_angle))

    solver.F.T_case_vector[x] = -1
    solver.F.T_case_vector[y] = -1*tan(constant.F.T_case_top_angle)
    solver.F.T_case_vector[z] = -1*tan(constant.F.T_case_side_angle)
    solver.R.T_case_vector[x] = 1
    solver.R.T_case_vector[y] = tan(constant.R.T_case_top_angle)
    solver.R.T_case_vector[z] = tan(constant.R.T_case_side_angle)

    for i in range(0,S.sample_points*2+1):
        travel.F.pinion_angle_rad[i] = -travel.F.pinion_rad[i] + constant.F.pinion_angle
        travel.R.pinion_angle_rad[i] = travel.R.pinion_rad[i] + constant.R.pinion_angle

        if constant.F.panhard: # If front panhard is used
            solver.pinion_travel[y] = constant.F.pinion[y] + travel.F.PA[i][y]-travel.F.PA[S.sample_points][y]
        else:
            solver.pinion_travel[y] = constant.F.pinion[y]

        solver.pinion_travel[x],solver.pinion_travel[z] = on_axle_movement(constant.F.pinion[x],constant.F.pinion[z],constant.F.LA[x],constant.F.LA[z],travel.F.LA[i][x],travel.F.LA[i][z],travel.F.pinion_rad[i])

        travel.F.driveshaft_length[i] = dis3D(solver.pinion_travel[x],solver.pinion_travel[y],solver.pinion_travel[z],constant.F.T_case[x],constant.F.T_case[y],constant.F.T_case[z])

        solver.driveshaft_delta[x] = constant.F.T_case[x] - solver.pinion_travel[x]
        solver.driveshaft_delta[y] = constant.F.T_case[y] - solver.pinion_travel[y]
        solver.driveshaft_delta[z] = constant.F.T_case[z] - solver.pinion_travel[z]

        solver.pinion_vector[x] = -1
        solver.pinion_vector[z] = tan(travel.F.pinion_angle_rad[i])

        travel.F.T_case_U_joint_angle_rad[i] = acos((solver.F.T_case_vector[x]*solver.driveshaft_delta[x]+solver.F.T_case_vector[y]*solver.driveshaft_delta[y]+solver.F.T_case_vector[z]*solver.driveshaft_delta[z])/(sqrt(solver.F.T_case_vector[x]**2+solver.F.T_case_vector[y]**2+solver.F.T_case_vector[z]**2)*travel.F.driveshaft_length[i]))
        travel.F.pinion_U_joint_angle_rad[i] = acos((solver.pinion_vector[x]*solver.driveshaft_delta[x]+solver.pinion_vector[y]*solver.driveshaft_delta[y]+solver.pinion_vector[z]*solver.driveshaft_delta[z])/(sqrt(solver.pinion_vector[x]**2+solver.pinion_vector[y]**2+solver.pinion_vector[z]**2)*travel.F.driveshaft_length[i]))

        if constant.R.panhard: # If front panhard is used
            solver.pinion_travel[y] = constant.R.pinion[y] + travel.R.PA[i][y]-travel.R.PA[S.sample_points][y]
        else:
            solver.pinion_travel[y] = constant.R.pinion[y]

        solver.pinion_travel[x],solver.pinion_travel[z] = on_axle_movement(constant.R.pinion[x],constant.R.pinion[z],constant.R.LA[x],constant.R.LA[z],travel.R.LA[i][x],travel.R.LA[i][z],travel.R.pinion_rad[i])

        temp1[i] = solver.pinion_travel[x]
        temp2[i] = solver.pinion_travel[z]

        travel.R.driveshaft_length[i] = dis3D(solver.pinion_travel[x],solver.pinion_travel[y],solver.pinion_travel[z],constant.R.T_case[x],constant.R.T_case[y],constant.R.T_case[z])

        solver.driveshaft_delta[x] = constant.R.T_case[x] - solver.pinion_travel[x]
        solver.driveshaft_delta[y] = constant.R.T_case[y] - solver.pinion_travel[y]
        solver.driveshaft_delta[z] = constant.R.T_case[z] - solver.pinion_travel[z]

        solver.pinion_vector[x] = 1
        solver.pinion_vector[z] = tan(travel.R.pinion_angle_rad[i])

        travel.R.T_case_U_joint_angle_rad[i] = acos((solver.R.T_case_vector[x]*solver.driveshaft_delta[x]+solver.R.T_case_vector[y]*solver.driveshaft_delta[y]+solver.R.T_case_vector[z]*solver.driveshaft_delta[z])/(sqrt(solver.R.T_case_vector[x]**2+solver.R.T_case_vector[y]**2+solver.R.T_case_vector[z]**2)*travel.R.driveshaft_length[i]))
        travel.R.pinion_U_joint_angle_rad[i] = acos((solver.pinion_vector[x]*solver.driveshaft_delta[x]+solver.pinion_vector[y]*solver.driveshaft_delta[y]+solver.pinion_vector[z]*solver.driveshaft_delta[z])/(sqrt(solver.pinion_vector[x]**2+solver.pinion_vector[y]**2+solver.pinion_vector[z]**2)*travel.R.driveshaft_length[i]))

    constant.F.driveshaft_max_length = max(travel.F.driveshaft_length)
    constant.F.driveshaft_min_length = min(travel.F.driveshaft_length)
    constant.F.driveshaft_length_ride = travel.F.driveshaft_length[S.sample_points]
    constant.F.driveshaft_length_delta = constant.F.driveshaft_max_length - constant.F.driveshaft_min_length

    constant.R.driveshaft_max_length = max(travel.R.driveshaft_length)
    constant.R.driveshaft_min_length = min(travel.R.driveshaft_length)
    constant.R.driveshaft_length_ride = travel.R.driveshaft_length[S.sample_points]
    constant.R.driveshaft_length_delta = constant.R.driveshaft_max_length - constant.R.driveshaft_min_length

    #import matplotlib.pyplot as plt
    #from VariableIO.initialize_IO import inputs,outputs
    #plt.plot(temp1,temp2)
    #plt.show()

    output_processing_driveshaft()