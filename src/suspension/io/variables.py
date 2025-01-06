# src/suspension/io/variables.py

x = 0
y = 1
z = 2

#import tkinter as tk
#ORIGINAL_DPI = 96.01758241758242
#def get_dpi():
#    screen = tk.Tk()
#    current_dpi = screen.winfo_fpixels('1i')
#    screen.destroy()
#    return current_dpi
#screen_scale = get_dpi()/ORIGINAL_DPI 

import numpy as np

class constant:
    class F: # Front
        # Link Geometry
        panhard = True
        U_count = 0
        U_parallel = False
        L_parallel = False

        LA = np.zeros(3)
        LF = np.zeros(3)
        UA = np.zeros(3)
        UF = np.zeros(3)
        PA = np.zeros(3)
        PF = np.zeros(3)
        hub = np.zeros(3)

        bump = 0
        droop = 0
        percent_up_remaining = 0
        
        tire_radius = 0
        tire_diameter = 0
        tire_width = 0
        portal_height= 0
        track_width = 0
        tire_rate = 0

        unsprung_mass = 0
        unsprung_CG_height = 0
        anti_CG = 0
        corner_sprung_weight = 0

        U_length_2D = 0
        L_length_2D = 0
        P_length_2D = 0
        U_length_3D = 0
        L_length_3D = 0
        P_length_3D = 0
        F_sep_2D = 0
        A_sep_2D = 0

        U_force = 0
        L_force = 0
        P_force = 0

        min_distance = 0
        sprung_CG_height_above_roll_center = 0

        U_converge = 0
        L_converge = 0
        total_converge = 0
        U_converge_point = np.zeros(3)
        L_converge_point = np.zeros(3)

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
        U_OD = 0
        L_OD = 0
        P_OD = 0
        U_wall = 0
        L_wall = 0
        P_wall = 0
        U_solid = False
        L_solid = False
        P_solid = False

        U_material = ''
        L_material = ''
        P_material = ''
        U_rod_end = ''
        L_rod_end = ''
        P_rod_end = ''

        spacing_warning = False

        # Driveshaft
        pinion = np.zeros(3)
        T_case = np.zeros(3)
        T_case_side_angle = 0
        T_case_top_angle = 0
        pinion_angle = 0
        pinion_hypoid = 0
        pinion_length = 0
        pinion_location_method = 0
        driveshaft_max_length = 0
        driveshaft_min_length = 0
        driveshaft_length_ride = 0
        driveshaft_length_delta = 0
        caster = 0

        # Shocks
        spring_method = 0
        shock_sep = 0
        freq_goal = 0
        main_spring_length = 0
        tender_spring_length = 0
        coil_size = 0
        preload_goal = 0
        step_up_ratio = 0
        used_main_spring = 0
        used_tender_spring = 0
        slider_stop = 0
        slider_anti_lift = [0,0] # First value is anti, second is insert location
        slider_anti_dive = [0,0] # First value is anti, second is insert location

        target_initial_frequency = 0
        target_final_frequency = 0
        target_initial_wheel_rate = 0
        target_final_wheel_rate = 0
        target_initial_spring_rate = 0
        target_main_spring_rate = 0
        target_tender_spring_rate = 0
        closest_match_main_spring = 0
        closest_match_tender_spring = 0
        closest_match_Ki = 0
        closest_match_WRi = 0
        closest_match_WRf = 0
        closest_match_SUR = 0
        closest_match_Fni = 0
        closest_match_Fnf = 0
        closest_match_preload = 0
        used_Ki = 0
        used_WRi = 0
        used_WRf = 0
        used_SUR = 0
        used_Fni = 0
        used_Fnf = 0
        used_preload = 0

        class shock1:
            chassis_mount = np.zeros(3)
            susp_mount = np.zeros(3)
            location = 0
            link_factor = 1
            bump_length = 0
            ride_length = 0
            droop_length = 0
            travel_used = 0
            travel_used_percent = 0
            travel_ride_percent = 0
            distance_to_body_roll_axis = 0
            length_extended = 0
            length_compressed = 0
            percent_bump_reminaing = 0
        class shock2:
            chassis_mount = np.zeros(3)
            susp_mount = np.zeros(3)
            location = 0
            exists = False
            link_factor = 1
            bump_length = 0
            ride_length = 0
            droop_length = 0
            travel_used = 0
            travel_used_percent = 0
            travel_ride_percent = 0
            distance_to_body_roll_axis = 0
            length_extended = 0
            length_compressed = 0
            percent_bump_reminaing = 0
        
        # Pitch
        pitch_travel = 0

    class R: # Rear
        # Link Geometry
        panhard = True
        U_count = 0
        U_parallel = False
        L_parallel = False

        LA = np.zeros(3)
        LF = np.zeros(3)
        UA = np.zeros(3)
        UF = np.zeros(3)
        PA = np.zeros(3)
        PF = np.zeros(3)
        hub = np.zeros(3)

        bump = 0
        droop = 0
        percent_up_remaining = 0
        
        tire_radius = 0
        tire_diameter = 0
        tire_width = 0
        portal_height= 0
        track_width = 0
        tire_rate = 0

        unsprung_mass = 0
        unsprung_CG_height = 0
        anti_CG = 0
        corner_sprung_weight = 0

        U_length_2D = 0
        L_length_2D = 0
        P_length_2D = 0
        U_length_3D = 0
        L_length_3D = 0
        P_length_3D = 0
        F_sep_2D = 0
        A_sep_2D = 0

        U_force = 0
        L_force = 0
        P_force = 0

        min_distance = 0
        sprung_CG_height_above_roll_center = 0
        
        U_converge = 0
        L_converge = 0
        total_converge = 0
        U_converge_point = np.zeros(3)
        L_converge_point = np.zeros(3)

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
        U_OD = 0
        L_OD = 0
        P_OD = 0
        U_wall = 0
        L_wall = 0
        P_wall = 0
        U_solid = False
        L_solid = False
        P_solid = False

        U_material = ''
        L_material = ''
        P_material = ''
        U_rod_end = ''
        L_rod_end = ''
        P_rod_end = ''

        spacing_warning = False

        # Driveshaft
        pinion = np.zeros(3)
        T_case = np.zeros(3)
        T_case_side_angle = 0
        T_case_top_angle = 0
        pinion_angle = 0
        pinion_hypoid = 0
        pinion_length = 0
        pinion_location_method = 0
        driveshaft_max_length = 0
        driveshaft_min_length = 0
        driveshaft_length_ride = 0
        driveshaft_length_delta = 0
        caster = 0

        # Shocks
        spring_method = 0
        shock_sep = 0
        freq_goal = 0
        main_spring_length = 0
        tender_spring_length = 0
        coil_size = 0
        preload_goal = 0
        step_up_ratio = 0
        used_main_spring = 0
        used_tender_spring = 0
        slider_stop = 0
        slider_anti_lift = [0,0] # First value is anti, second is insert location
        slider_anti_squat = [0,0] # First value is anti, second is insert location

        target_initial_frequency = 0
        target_final_frequency = 0
        target_initial_wheel_rate = 0
        target_final_wheel_rate = 0
        target_initial_spring_rate = 0
        target_main_spring_rate = 0
        target_tender_spring_rate = 0
        closest_match_main_spring = 0
        closest_match_tender_spring = 0
        closest_match_Ki = 0
        closest_match_WRi = 0
        closest_match_WRf = 0
        closest_match_SUR = 0
        closest_match_Fni = 0
        closest_match_Fnf = 0
        closest_match_preload = 0
        used_Ki = 0
        used_WRi = 0
        used_WRf = 0
        used_SUR = 0
        used_Fni = 0
        used_Fnf = 0
        used_preload = 0

        class shock1:
            chassis_mount = np.zeros(3)
            susp_mount = np.zeros(3)
            location = 0
            link_factor = 1
            bump_length = 0
            ride_length = 0
            droop_length = 0
            travel_used = 0
            travel_used_percent = 0
            travel_ride_percent = 0
            distance_to_body_roll_axis = 0
            length_extended = 0
            length_compressed = 0
            percent_bump_reminaing = 0
        class shock2:
            chassis_mount = np.zeros(3)
            susp_mount = np.zeros(3)
            location = 0
            exists = False
            link_factor = 1
            bump_length = 0
            ride_length = 0
            droop_length = 0
            travel_used = 0
            travel_used_percent = 0
            travel_ride_percent = 0
            distance_to_body_roll_axis = 0
            length_extended = 0
            length_compressed = 0
            percent_bump_reminaing = 0

        # Pitch
        pitch_travel = 0

    class V: # Vehicle
        wheelbase = 0
        drive_bias = 0
        brake_bias = 0
        CG_height = 0
        weight_distribution = .5
        mass = 0
        sprung_mass = 0
        sprung_cg = np.zeros(3)
        acceleration = 0
        transverse_acceleration = 0
        climb_angle = 0
        descent_angle = 0
        side_roll_angle = 0
        
        roll_slope_dpd = 0
        sprung_CG_height_above_roll_axis = 0

        Desired_FS_Yield = 0
        Desired_FS_Buckling = 0
        Desired_FS_Bending = 0
        Desired_FS_RE = 0
        Desired_FS_Dent = 0
        combined_link_weight = 0

        desired_speed = 0
        spring_method = 0
        freq_approach = 0
        closest_match_speed = 0
        used_match_speed = 0

    class pitch:
        front_travel_est = np.zeros(5)
        rear_travel_est = np.zeros(5)
        load_bias = np.zeros(5)
        
        drive_bias = 0
        brake_bias = 0
        slope = 0
        acceleration = 0
        angle = [0 for _ in range(7)]
        body_roll_slope_dpd = [0 for _ in range(7)]
        sprung_mass_CG = [0 for _ in range(7)]
        class F:
            UA = np.zeros((7,3))
            UF = np.zeros((7,3))
            LA = np.zeros((7,3))
            LF = np.zeros((7,3))
            PA = np.zeros((7,3))
            PF = np.zeros((7,3))
            hub = np.zeros((7,3))
            anti_dive = np.zeros(7)
            anti_lift = np.zeros(7)
            roll_slope_dpd = np.zeros(7)
            roll_center = np.zeros(7)
            travel = np.zeros(7)

        class R:
            UA = np.zeros((7,3))
            UF = np.zeros((7,3))
            LA = np.zeros((7,3))
            LF = np.zeros((7,3))
            PA = np.zeros((7,3))
            PF = np.zeros((7,3))
            hub = np.zeros((7,3))
            anti_lift = np.zeros(7)
            anti_squat = np.zeros(7)
            roll_slope_dpd = np.zeros(7)
            roll_center = np.zeros(7)
            travel = np.zeros(7)

    class sizing:
        FS_yield = [0,0,0,0,0,0]
        FS_buckling = [0,0,0,0,0,0]
        FS_bending = [0,0,0,0,0,0]
        dent_resistance = [0,0,0,0,0,0]
        FS_RE = [0,0,0,0,0,0]
        link_weight = [0,0,0,0,0,0]
        total_link_weight = [0,0,0,0,0,0]
        RE_weight = [0,0,0,0,0,0]
        RE_thread = ['a','a','a','a','a','a']
        RE_hole_diameter = ['a','a','a','a','a','a']
        RE_thread_diameter = [0,0,0,0,0,0]

    class rod_ends:
        name = []
        radial_load = []
        weight = []
        hole_diameter = []
        shank_diameter = []
        thread = []

    class materials:
        name = []
        yield_strength = []
        modulus_elasticity = []
        density = []
        notes = []

    class springs:
        s20 = {}
        s25 = {}
        s30 = {}
        sizes = ["2.0","2.5","3.0"]

class travel:
    class F: # Front
        # link calc
        LA = np.zeros((2,3))
        UA = np.zeros((2,3))
        PA = np.zeros((2,3))
        hub = np.zeros((2,3))
        pinion_rad = np.zeros(2)
        roll_slope_dpd = np.zeros(2)
        roll_center = np.zeros(2)
        IC = np.zeros((2,3))
        anti = np.zeros(2)
        anti_lift = np.zeros(2)
        anti_dive = np.zeros(2)

        travel_dist = np.zeros(2)
        panhard_transverse_movement = np.zeros(2)

        pinion = np.zeros(2)

        # driveshaft
        driveshaft_length = np.zeros(2)
        T_case_U_joint_angle_rad = np.zeros(2)
        pinion_U_joint_angle_rad = np.zeros(2)
        pinion_angle_rad = np.zeros(2)

        # shocks
        shock_seperation = 0
        wheel_force_closest = np.zeros(2)
        wheel_rate_closest = np.zeros(2)
        wheel_force_chosen = np.zeros(2)
        wheel_rate_chosen = np.zeros(2)
        spring_force_closest = np.zeros(2)
        spring_force_chosen = np.zeros(2)
        class shock1:
            susp_mount = np.zeros((2,3))
            IR = np.zeros(2)
            length = np.zeros(2)
            class factor:
                inboard = np.zeros(2)
                distance = np.zeros(2)
                shock_angle = np.zeros(2)
                wheel = np.zeros(2)
        class shock2:
            susp_mount = np.zeros((2,3))
            IR = np.zeros(2)
            length = np.zeros(2)
            class factor:
                inboard = np.zeros(2)
                distance = np.zeros(2)
                shock_angle = np.zeros(2)
                wheel = np.zeros(2)

    class R: # Rear
        # link calc
        LA = np.zeros((2,3))
        UA = np.zeros((2,3))
        PA = np.zeros((2,3))
        hub = np.zeros((2,3))
        pinion_rad = np.zeros(2)
        roll_slope_dpd = np.zeros(2)
        roll_center = np.zeros(2)
        IC = np.zeros((2,3))
        anti = np.zeros(2)
        anti_lift = np.zeros(2)
        anti_squat = np.zeros(2)

        travel_dist = np.zeros(2)
        panhard_transverse_movement = np.zeros(2)

        pinion = np.zeros(2)

        # driveshaft
        driveshaft_length = np.zeros(2)
        T_case_U_joint_angle_rad = np.zeros(2)
        pinion_U_joint_angle_rad = np.zeros(2)
        pinion_angle_rad = np.zeros(2)

        # shocks
        shock_seperation = 0
        wheel_force_closest = np.zeros(2)
        wheel_rate_closest = np.zeros(2)
        wheel_force_chosen = np.zeros(2)
        wheel_rate_chosen = np.zeros(2)
        spring_force_closest = np.zeros(2)
        spring_force_chosen = np.zeros(2)
        class shock1:
            susp_mount = np.zeros((2,3))
            IR = np.zeros(2)
            length = np.zeros(2)
            class factor:
                inboard = np.zeros(2)
                distance = np.zeros(2)
                shock_angle = np.zeros(2)
                wheel = np.zeros(2)
        class shock2:
            susp_mount = np.zeros((2,3))
            IR = np.zeros(2)
            length = np.zeros(2)
            class factor:
                inboard = np.zeros(2)
                distance = np.zeros(2)
                shock_angle = np.zeros(2)
                wheel = np.zeros(2)

class S: # settings
    sample_points = 50
    simulate_tire_loading = False
    units = "Imperial"
    reversed_front_x = False
    file_mame = ''

    position_units = "in"
    mass_units = "lbs"
    speed_units = "mph"
    pressure_units = "psi"
    density_units = "lbs/in^3"
    force_units = "lbs"

class PS: # plot settings
    converge = "Show"
    IC_move = "Show"
    high_travel = "Show"
    axle_roll = "Show"
    body_roll = "Show"
    anti_100 = "Show"
    ride_anti = "Show"
    roll_center = "Show"
    ride_IC = "Show"