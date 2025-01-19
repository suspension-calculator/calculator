# src/suspension/io/initialize_IO.py

# Library Imports
import numpy as np

class inputs:
    class F:  # Front
        # Link Geometry
        panhard = False
        U_count = 2

        LA = np.array([-4, 19, 20])
        LF = np.array([-45, 9, 22])
        UA = np.array([0, 10, 30])
        UF = np.array([-28, 20, 29])
        PA = np.array([4, -24, 26])
        PF = np.array([4, 24, 26])

        bump = 8
        droop = -8

        tire_radius = 19
        tire_diameter = 42
        tire_width = 14.5
        portal_height = 0
        track_width = 74
        axle_tube = 3.5

        unsprung_mass = 600

        # Link Sizing
        U_OD = 1.75
        L_OD = 2.5
        P_OD = 1.75
        U_wall = 0.25
        L_wall = 0.25
        P_wall = 0.125
        U_solid = True
        L_solid = True
        P_solid = False

        U_material = "Aluminum 7075-T6"
        L_material = "Aluminum 7075-T6"
        P_material = "Steel 1018"
        U_rod_end = "JMX14T-770"
        L_rod_end = "JMX16-1"
        P_rod_end = "JMX16-1"

        # Driveshaft
        pinion = np.array([-8.125, 10, 22])
        T_case = np.array([-50.487, 9.435, 26.45])
        pinion_location_method = 1
        T_case_side_angle = 5
        T_case_top_angle = 0
        pinion_angle = 5
        pinion_hypoid = -1.25
        pinion_length = -8
        caster = 0

        # Shocks
        spring_method = 0
        freq_goal = 0.5
        preload_goal = 2
        step_up_ratio = 3
        used_main_spring = 150
        used_tender_spring = 125

        class shock1:
            size = "2.5"
            travel = 16
            main_spring_extra_length = 2
            chassis_mount = np.array([-15.5, 16, 52])
            susp_mount = np.array([-3.25, 22, 20.125])
            location = 0
            length_extended = 42.25
            length_compressed = 38.430

        class shock2:
            size = "2.5"
            travel = 16
            chassis_mount = np.array([-20, 15, 48])
            susp_mount = np.array([-6, 18.75, 20])
            location = 0
            exists = True
            length_extended = 38.430
            length_compressed = 24.430

        # Pitch
        pitch_travel = 5

    class R:  # Rear
        # Link Geometry
        panhard = False
        U_count = 2

        LA = np.array([4, 19, 20])
        LF = np.array([40, 9, 22])
        UA = np.array([0, 10, 30])
        UF = np.array([27, 20, 29.5])
        PA = np.array([-8, -24, 23])
        PF = np.array([-8, 24, 23])

        bump = 8
        droop = -8

        tire_radius = 19
        tire_diameter = 42
        tire_width = 14.5
        portal_height = 0
        track_width = 74
        axle_tube = 4

        unsprung_mass = 500

        # Link Sizing
        U_OD = 1.75
        L_OD = 2.5
        P_OD = 1.75
        U_wall = 0.25
        L_wall = 0.25
        P_wall = 0.125
        U_solid = True
        L_solid = True
        P_solid = False

        U_material = "Aluminum 7075-T6"
        L_material = "Aluminum 7075-T6"
        P_material = "Steel 1018"
        U_rod_end = "JMX14T-770"
        L_rod_end = "JMX16-1"
        P_rod_end = "JMX16-1"

        # Driveshaft
        pinion = np.array([8, 0, 22])
        T_case = np.array([43.25, 0, 26.697])
        pinion_location_method = 1
        T_case_side_angle = -5
        T_case_top_angle = 0
        pinion_angle = 5
        pinion_hypoid = -0.125
        pinion_length = 8
        caster = 0

        # Shocks
        spring_method = 0
        freq_goal = 0.5
        preload_goal = 3
        step_up_ratio = 0
        used_main_spring = 150
        used_tender_spring = 100

        class shock1:
            size = "2.5"
            travel = 16
            main_spring_extra_length = 2
            chassis_mount = np.array([9.75, 13, 55.375])
            susp_mount = np.array([0.625, 20.750, 22.75])
            location = 0
            length_extended = 42.250
            length_compressed = 26.750

        class shock2:
            size = "3.0"
            travel = 16
            chassis_mount = np.array([9, 16, 53.875])
            susp_mount = np.array([-1, 19.5, 21])
            location = 0
            exists = True
            length_extended = 42.430
            length_compressed = 26.430

        # Pitch
        pitch_travel = -5

    class V:  # Vehicle
        wheelbase = 110
        drive_bias = 0.5
        brake_bias = 0.6
        CG_height = 30
        weight_distribution = 0.55
        mass = 3000
        acceleration = 1
        transverse_acceleration = 1

        Desired_FS_Yield = 15
        Desired_FS_Buckling = 6
        Desired_FS_Bending = 2
        Desired_FS_RE = 6
        Desired_FS_Dent = 15

        desired_speed = 40
        freq_approach = 0
        spring_method = 0

        pitch_slope = 45  # needs to be degrees
        pitch_acceleration = 1
        pitch_drive_bias = 0.5
        pitch_brake_bias = 0.6


class outputs:
    class F:
        # Link Calc
        UA = np.zeros((2, 3))
        LA = np.zeros((2, 3))
        UF = np.zeros((1, 3))
        LF = np.zeros((1, 3))
        PA = np.zeros((2, 3))
        PF = np.zeros((1, 3))
        U_Length_3D = 0
        L_Length_3D = 0
        P_Length_3D = 0
        U_Length_2D = 0
        L_Length_2D = 0
        P_Length_2D = 0
        U_Max_Force = 0
        L_Max_Force = 0
        P_Max_Force = 0
        Travel = np.zeros(2)
        Anti_Dive = np.zeros(2)
        Anti_Lift = np.zeros(2)
        Anti_CG = 0
        Roll_Slope = np.zeros(2)
        Roll_Center = np.zeros(2)
        Pinion_Change = np.zeros(2)
        Panhard_Transverse_Movement = np.zeros(2)
        IC = np.zeros((2, 3))
        Hub = np.zeros((2, 3))
        Upper_Convergence = 0
        Lower_Convergence = 0
        Total_Convergence = 0
        U_converge_point = np.zeros(3)
        L_converge_point = np.zeros(3)
        Sprung_CG_height_Above_Roll_Center = 0
        Min_Sep = 0
        LA_side_view_angle_range = np.zeros(2)
        LF_side_view_angle_range = np.zeros(2)
        L_top_view_angle = 0
        UA_side_view_angle_range = np.zeros(2)
        UF_side_view_angle_range = np.zeros(2)
        U_top_view_angle = 0
        PA_front_view_angle_range = np.zeros(2)
        PA_top_view_angle_range = np.zeros(2)
        PF_front_view_angle_range = np.zeros(2)
        PF_top_view_angle_range = np.zeros(2)

        # Link Sizing
        U_Thread = "a"
        L_Thread = "a"
        P_Thread = "a"
        U_Hole = "a"
        L_Hole = "a"
        P_Hole = "a"
        U_Link_Weight = 0
        L_Link_Weight = 0
        P_Link_Weight = 0
        U_RE_Weight = 0
        L_RE_Weight = 0
        P_RE_Weight = 0
        U_Weight = 0
        L_Weight = 0
        P_Weight = 0
        U_FS_Yield = 0
        L_FS_Yield = 0
        P_FS_Yield = 0
        U_FS_buckling = 0
        L_FS_buckling = 0
        P_FS_buckling = 0
        U_FS_bending = 0
        L_FS_bending = 0
        P_FS_bending = 0
        U_Dent_Resistance = 0
        L_Dent_Resistance = 0
        P_Dent_Resistance = 0
        U_FS_RE = 0
        L_FS_RE = 0
        P_FS_RE = 0

        # Driveshafts
        Max_Length = 0
        Ride_Length = 0
        Min_Length = 0
        Driveshaft_Travel = 0
        T_Case_U_Joint = np.zeros(2)
        Pinion_U_Joint = np.zeros(2)

        # Shocks
        Dist_Between = 0
        Percent_Up_Travel = 0

        class Shock1:
            Full_Bump_Length = 0
            Full_Droop_Length = 0
            Percent_Bump_Remaining = 0
            Lever_Arm_2_Body_Roll = 0
            Force_Closest = np.zeros(2)
            Force_Chosen = np.zeros(2)
            IR = np.zeros(2)
            Link_Ratio = np.zeros(2)
            Distance_Ratio = np.zeros(2)
            Shock_Angle = np.zeros(2)
            Wheel_IC = np.zeros(2)
            Shock_Inboard = np.zeros(2)
            Corner_Sprung_Weight = 0
            Ideal_Main_Spring = 0
            Ideal_Tender_Spring = 0
            Ideal_Ride_Freq = 0
            Ideal_Full_Bump_Freq = 0
            Closest_Main_Spring = 0
            Closest_Tender_Spring = 0
            Closest_Step_Up = 0
            Closest_Ride_Freq = 0
            Closest_Full_Bump_Freq = 0
            Closest_Preload = 0
            Chosen_Step_Up = 0
            Chosen_Ride_Freq = 0
            Chosen_Full_Bump_Freq = 0
            Chosen_Preload = 0

        class Shock2:
            Full_Bump_Length = 0
            Full_Droop_Length = 0
            Percent_Bump_Remaining = 0
            Lever_Arm_2_Body_Roll = 0
            IR = np.zeros(2)
            Link_Ratio = np.zeros(2)
            Distance_Ratio = np.zeros(2)
            Shock_Angle = np.zeros(2)
            Wheel_IC = np.zeros(2)
            Shock_Inboard = np.zeros(2)

    class R:
        # Link Calc
        UA = np.zeros((2, 3))
        LA = np.zeros((2, 3))
        UF = np.zeros((1, 3))
        LF = np.zeros((1, 3))
        PA = np.zeros((2, 3))
        PF = np.zeros((1, 3))
        U_Length_3D = 0
        L_Length_3D = 0
        P_Length_3D = 0
        U_Length_2D = 0
        L_Length_2D = 0
        P_Length_2D = 0
        U_Max_Force = 0
        L_Max_Force = 0
        P_Max_Force = 0
        Travel = np.zeros(2)
        Anti_Squat = np.zeros(2)
        Anti_Lift = np.zeros(2)
        Anti_CG = 0
        Roll_Slope = np.zeros(2)
        Roll_Center = np.zeros(2)
        Pinion_Change = np.zeros(2)
        Panhard_Transverse_Movement = np.zeros(2)
        IC = np.zeros((2, 3))
        Hub = np.zeros((2, 3))
        Upper_Convergence = 0
        Lower_Convergence = 0
        Total_Convergence = 0
        U_converge_point = np.zeros(3)
        L_converge_point = np.zeros(3)
        Sprung_CG_height_Above_Roll_Center = 0
        Min_Sep = 0
        LA_side_view_angle_range = np.zeros(2)
        LF_side_view_angle_range = np.zeros(2)
        L_top_view_angle = 0
        UA_side_view_angle_range = np.zeros(2)
        UF_side_view_angle_range = np.zeros(2)
        U_top_view_angle = 0
        PA_rear_view_angle_range = np.zeros(2)
        PA_top_view_angle_range = np.zeros(2)
        PF_rear_view_angle_range = np.zeros(2)
        PF_top_view_angle_range = np.zeros(2)

        # Link Sizing
        U_Thread = "a"
        L_Thread = "a"
        P_Thread = "a"
        U_Hole = "a"
        L_Hole = "a"
        P_Hole = "a"
        U_Link_Weight = 0
        L_Link_Weight = 0
        P_Link_Weight = 0
        U_RE_Weight = 0
        L_RE_Weight = 0
        P_RE_Weight = 0
        U_Weight = 0
        L_Weight = 0
        P_Weight = 0
        U_FS_Yield = 0
        L_FS_Yield = 0
        P_FS_Yield = 0
        U_FS_buckling = 0
        L_FS_buckling = 0
        P_FS_buckling = 0
        U_FS_bending = 0
        L_FS_bending = 0
        P_FS_bending = 0
        U_Dent_Resistance = 0
        L_Dent_Resistance = 0
        P_Dent_Resistance = 0
        U_FS_RE = 0
        L_FS_RE = 0
        P_FS_RE = 0

        # Driveshafts
        Max_Length = 0
        Ride_Length = 0
        Min_Length = 0
        Driveshaft_Travel = 0
        T_Case_U_Joint = np.zeros(2)
        Pinion_U_Joint = np.zeros(2)

        # Shocks
        Dist_Between = 0
        Percent_Up_Travel = 0

        class Shock1:
            Full_Bump_Length = 0
            Full_Droop_Length = 0
            Percent_Bump_Remaining = 0
            Lever_Arm_2_Body_Roll = 0
            Force_Closest = np.zeros(2)
            Force_Chosen = np.zeros(2)
            IR = np.zeros(2)
            Link_Ratio = np.zeros(2)
            Distance_Ratio = np.zeros(2)
            Shock_Angle = np.zeros(2)
            Wheel_IC = np.zeros(2)
            Shock_Inboard = np.zeros(2)
            Corner_Sprung_Weight = 0
            Ideal_Main_Spring = 0
            Ideal_Tender_Spring = 0
            Ideal_Ride_Freq = 0
            Ideal_Full_Bump_Freq = 0
            Closest_Main_Spring = 0
            Closest_Tender_Spring = 0
            Closest_Step_Up = 0
            Closest_Ride_Freq = 0
            Closest_Full_Bump_Freq = 0
            Closest_Preload = 0
            Chosen_Step_Up = 0
            Chosen_Ride_Freq = 0
            Chosen_Full_Bump_Freq = 0
            Chosen_Preload = 0

        class Shock2:
            Full_Bump_Length = 0
            Full_Droop_Length = 0
            Percent_Bump_Remaining = 0
            Lever_Arm_2_Body_Roll = 0
            IR = np.zeros(2)
            Link_Ratio = np.zeros(2)
            Distance_Ratio = np.zeros(2)
            Shock_Angle = np.zeros(2)
            Wheel_IC = np.zeros(2)
            Shock_Inboard = np.zeros(2)

    class V:
        # Link Calc
        Acceleration = 0
        Transverse_Acceleration = 0
        Sprung_CG_height = 0
        Sprung_CG_height_Above_Roll_Axis = 0
        Roll_Axis = 0
        Climb_Angle = 0
        Descent_Angle = 0
        Side_Roll_Angle = 0

        # Link Sizing
        Combined_Link_Weight = 0

        # Shocks
        Closest_Anti_Pitching_Speed = 0
        Chosen_Anti_Pitching_Speed = 0

    class Pitch:
        front_travel_est = np.zeros(5)
        rear_travel_est = np.zeros(5)
        load_bias = np.zeros(5)

        class User_Input:
            Angle = 0
            Front_Travel = 0
            Rear_Travel = 0
            Body_Roll_Axis = 0
            Sprung_Mass_CG = 0

            class F:
                Anti_Dive = 0
                Anti_Lift = 0
                Roll_Slope = 0
                Roll_Center = 0
                UA = np.zeros(3)
                UF = np.zeros(3)
                LA = np.zeros(3)
                LF = np.zeros(3)
                PA = np.zeros(3)
                PF = np.zeros(3)
                Hub = np.zeros(3)

            class R:
                Anti_Squat = 0
                Anti_Lift = 0
                Roll_Slope = 0
                Roll_Center = 0
                UA = np.zeros(3)
                UF = np.zeros(3)
                LA = np.zeros(3)
                LF = np.zeros(3)
                PA = np.zeros(3)
                PF = np.zeros(3)
                Hub = np.zeros(3)

        class Half_Rear:
            Angle = 0
            Front_Travel = 0
            Rear_Travel = 0
            Body_Roll_Axis = 0
            Sprung_Mass_CG = 0

            class F:
                Anti_Dive = 0
                Anti_Lift = 0
                Roll_Slope = 0
                Roll_Center = 0
                UA = np.zeros(3)
                UF = np.zeros(3)
                LA = np.zeros(3)
                LF = np.zeros(3)
                PA = np.zeros(3)
                PF = np.zeros(3)
                Hub = np.zeros(3)

            class R:
                Anti_Squat = 0
                Anti_Lift = 0
                Roll_Slope = 0
                Roll_Center = 0
                UA = np.zeros(3)
                UF = np.zeros(3)
                LA = np.zeros(3)
                LF = np.zeros(3)
                PA = np.zeros(3)
                PF = np.zeros(3)
                Hub = np.zeros(3)

        class Half_Front:
            Angle = 0
            Front_Travel = 0
            Rear_Travel = 0
            Body_Roll_Axis = 0
            Sprung_Mass_CG = 0

            class F:
                Anti_Dive = 0
                Anti_Lift = 0
                Roll_Slope = 0
                Roll_Center = 0
                UA = np.zeros(3)
                UF = np.zeros(3)
                LA = np.zeros(3)
                LF = np.zeros(3)
                PA = np.zeros(3)
                PF = np.zeros(3)
                Hub = np.zeros(3)

            class R:
                Anti_Squat = 0
                Anti_Lift = 0
                Roll_Slope = 0
                Roll_Center = 0
                UA = np.zeros(3)
                UF = np.zeros(3)
                LA = np.zeros(3)
                LF = np.zeros(3)
                PA = np.zeros(3)
                PF = np.zeros(3)
                Hub = np.zeros(3)

        class Full_Rear:
            Angle = 0
            Front_Travel = 0
            Rear_Travel = 0
            Body_Roll_Axis = 0
            Sprung_Mass_CG = 0

            class F:
                Anti_Dive = 0
                Anti_Lift = 0
                Roll_Slope = 0
                Roll_Center = 0
                UA = np.zeros(3)
                UF = np.zeros(3)
                LA = np.zeros(3)
                LF = np.zeros(3)
                PA = np.zeros(3)
                PF = np.zeros(3)
                Hub = np.zeros(3)

            class R:
                Anti_Squat = 0
                Anti_Lift = 0
                Roll_Slope = 0
                Roll_Center = 0
                UA = np.zeros(3)
                UF = np.zeros(3)
                LA = np.zeros(3)
                LF = np.zeros(3)
                PA = np.zeros(3)
                PF = np.zeros(3)
                Hub = np.zeros(3)

        class Full_Front:
            Angle = 0
            Front_Travel = 0
            Rear_Travel = 0
            Body_Roll_Axis = 0
            Sprung_Mass_CG = 0

            class F:
                Anti_Dive = 0
                Anti_Lift = 0
                Roll_Slope = 0
                Roll_Center = 0
                UA = np.zeros(3)
                UF = np.zeros(3)
                LA = np.zeros(3)
                LF = np.zeros(3)
                PA = np.zeros(3)
                PF = np.zeros(3)
                Hub = np.zeros(3)

            class R:
                Anti_Squat = 0
                Anti_Lift = 0
                Roll_Slope = 0
                Roll_Center = 0
                UA = np.zeros(3)
                UF = np.zeros(3)
                LA = np.zeros(3)
                LF = np.zeros(3)
                PA = np.zeros(3)
                PF = np.zeros(3)
                Hub = np.zeros(3)

        class Full_Up:
            Angle = 0
            Front_Travel = 0
            Rear_Travel = 0
            Body_Roll_Axis = 0
            Sprung_Mass_CG = 0

            class F:
                Anti_Dive = 0
                Anti_Lift = 0
                Roll_Slope = 0
                Roll_Center = 0
                UA = np.zeros(3)
                UF = np.zeros(3)
                LA = np.zeros(3)
                LF = np.zeros(3)
                PA = np.zeros(3)
                PF = np.zeros(3)
                Hub = np.zeros(3)

            class R:
                Anti_Squat = 0
                Anti_Lift = 0
                Roll_Slope = 0
                Roll_Center = 0
                UA = np.zeros(3)
                UF = np.zeros(3)
                LA = np.zeros(3)
                LF = np.zeros(3)
                PA = np.zeros(3)
                PF = np.zeros(3)
                Hub = np.zeros(3)

        class Full_Down:
            Angle = 0
            Front_Travel = 0
            Rear_Travel = 0
            Body_Roll_Axis = 0
            Sprung_Mass_CG = 0

            class F:
                Anti_Dive = 0
                Anti_Lift = 0
                Roll_Slope = 0
                Roll_Center = 0
                UA = np.zeros(3)
                UF = np.zeros(3)
                LA = np.zeros(3)
                LF = np.zeros(3)
                PA = np.zeros(3)
                PF = np.zeros(3)
                Hub = np.zeros(3)

            class R:
                Anti_Squat = 0
                Anti_Lift = 0
                Roll_Slope = 0
                Roll_Center = 0
                UA = np.zeros(3)
                UF = np.zeros(3)
                LA = np.zeros(3)
                LF = np.zeros(3)
                PA = np.zeros(3)
                PF = np.zeros(3)
                Hub = np.zeros(3)
