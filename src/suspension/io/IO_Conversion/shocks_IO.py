# src/suspension/io/IO_Conversion/link_sizing_IO.py

def input_processing_shocks():
    from suspension.io.initialize_IO import inputs
    from suspension.io.variables import constant,S, x,y,z
    from suspension.core.functions.unit_conversion import in2mm, mm2in, kg2lb, lb2kg, kmh2mph, mph2kmh, npmm2lbpin, lbpin2npmm
    from math import radians

    #degree to rad conversion

    constant.V.freq_approach = inputs.V.freq_approach*1
    constant.V.spring_method = inputs.V.spring_method*1

    constant.F.main_spring_length = "{:.0f}".format(inputs.F.shock1.travel+inputs.F.shock1.main_spring_extra_length*1)
    constant.F.tender_spring_length = "{:.0f}".format(inputs.F.shock1.travel*1)
    constant.F.used_main_spring = inputs.F.used_main_spring*1
    constant.F.used_tender_spring = inputs.F.used_tender_spring*1

    constant.R.main_spring_length = "{:.0f}".format(inputs.R.shock1.travel+inputs.R.shock1.main_spring_extra_length*1)
    constant.R.tender_spring_length = "{:.0f}".format(inputs.R.shock1.travel*1)
    constant.R.used_main_spring = inputs.R.used_main_spring*1
    constant.R.used_tender_spring = inputs.R.used_tender_spring*1

    constant.F.coil_size = inputs.F.shock1.size
    constant.R.coil_size = inputs.R.shock1.size

    constant.V.freq_approach = inputs.V.freq_approach*1
    constant.F.freq_goal = inputs.F.freq_goal*1
    constant.R.freq_goal = inputs.R.freq_goal*1
    constant.F.step_up_ratio = inputs.F.step_up_ratio*1
    constant.R.step_up_ratio = inputs.R.step_up_ratio*1

    constant.F.shock1.location = inputs.F.shock1.location*1
    constant.F.shock2.location = inputs.F.shock2.location*1
    constant.R.shock1.location = inputs.R.shock1.location*1
    constant.R.shock2.location = inputs.R.shock2.location*1

    if S.units == 'metric':
        # if metric convert all inputs to sae and set variables
        constant.F.shock1.susp_mount= mm2in(inputs.F.shock1.susp_mount)
        constant.F.shock2.susp_mount= mm2in(inputs.F.shock2.susp_mount)
        constant.F.preload_goal = mm2in(inputs.F.preload_goal)
        constant.F.used_main_spring = npmm2lbpin(inputs.F.used_main_spring)
        constant.F.used_tender_spring = npmm2lbpin(inputs.F.used_tender_spring)
        constant.F.preload_goal = mm2in(inputs.F.preload_goal)

        constant.R.shock1.susp_mount= mm2in(inputs.R.shock1.susp_mount)
        constant.R.shock2.susp_mount= mm2in(inputs.R.shock2.susp_mount)
        constant.R.preload_goal = mm2in(inputs.R.preload_goal)
        constant.R.used_main_spring = npmm2lbpin(inputs.R.used_main_spring)
        constant.R.used_tender_spring = npmm2lbpin(inputs.R.used_tender_spring)
        constant.R.preload_goal = mm2in(inputs.R.preload_goal)

        constant.F.shock1.length_extended = mm2in(inputs.F.shock1.length_extended)
        constant.F.shock1.length_compressed = mm2in(inputs.F.shock1.length_compressed)
        constant.F.shock2.length_extended = mm2in(inputs.F.shock2.length_extended)
        constant.F.shock2.length_compressed = mm2in(inputs.F.shock2.length_compressed)
    
        constant.R.shock1.length_extended = mm2in(inputs.R.shock1.length_extended)
        constant.R.shock1.length_compressed = mm2in(inputs.R.shock1.length_compressed)
        constant.R.shock2.length_extended = mm2in(inputs.R.shock2.length_extended)
        constant.R.shock2.length_compressed = mm2in(inputs.R.shock2.length_compressed)

    else:
        # set variables

        constant.F.shock1.susp_mount= inputs.F.shock1.susp_mount*1
        constant.F.shock2.susp_mount= inputs.F.shock2.susp_mount*1
        constant.F.preload_goal = inputs.F.preload_goal*1
        constant.F.used_main_spring = inputs.F.used_main_spring*1
        constant.F.used_tender_spring = inputs.F.used_tender_spring*1

        constant.R.shock1.susp_mount= inputs.R.shock1.susp_mount*1
        constant.R.shock2.susp_mount= inputs.R.shock2.susp_mount*1
        constant.R.preload_goal = inputs.R.preload_goal*1
        constant.R.used_main_spring = inputs.R.used_main_spring*1
        constant.R.used_tender_spring = inputs.R.used_tender_spring*1
        constant.F.shock1.length_extended = inputs.F.shock1.length_extended*1
        constant.F.shock1.length_compressed = inputs.F.shock1.length_compressed*1
        constant.F.shock2.length_extended = inputs.F.shock2.length_extended*1
        constant.F.shock2.length_compressed = inputs.F.shock2.length_compressed*1

        constant.R.shock1.length_extended = inputs.R.shock1.length_extended*1
        constant.R.shock1.length_compressed = inputs.R.shock1.length_compressed*1
        constant.R.shock2.length_extended = inputs.R.shock2.length_extended*1
        constant.R.shock2.length_compressed = inputs.R.shock2.length_compressed*1

    if S.reversed_front_x:
        constant.F.shock1.chassis_mount[x] = constant.V.wheelbase - constant.F.shock1.chassis_mount[x]
        constant.F.shock1.susp_mount[x]    = constant.V.wheelbase - constant.F.shock1.susp_mount[x]
        constant.F.shock2.chassis_mount[x] = constant.V.wheelbase - constant.F.shock2.chassis_mount[x]
        constant.F.shock2.susp_mount[x]    = constant.V.wheelbase - constant.F.shock2.susp_mount[x]
    else:
        constant.F.shock1.chassis_mount[x] = constant.V.wheelbase + constant.F.shock1.chassis_mount[x]
        constant.F.shock1.susp_mount[x]    = constant.V.wheelbase + constant.F.shock1.susp_mount[x]
        constant.F.shock2.chassis_mount[x] = constant.V.wheelbase + constant.F.shock2.chassis_mount[x]
        constant.F.shock2.susp_mount[x]    = constant.V.wheelbase + constant.F.shock2.susp_mount[x]


def output_processing_shocks():
    from suspension.io.initialize_IO import outputs
    from suspension.io.variables import constant,travel,S
    from suspension.core.functions.unit_conversion import in2mm, mm2in, kg2lb, lb2kg, kmh2mph, mph2kmh, npmm2lbpin, lbpin2npmm, lb2N

    outputs.F.Percent_Up_Travel = constant.F.percent_up_remaining*1
    outputs.F.Shock1.Percent_Bump_Remaining = constant.F.shock1.percent_bump_reminaing*1
    outputs.F.Shock1.IR = travel.F.shock1.IR*1
    outputs.F.Shock1.Link_Ratio = constant.F.shock1.link_factor*1
    outputs.F.Shock1.Distance_Ratio = travel.F.shock1.factor.distance*1
    outputs.F.Shock1.Shock_Angle = travel.F.shock1.factor.shock_angle*1
    outputs.F.Shock1.Wheel_IC  = travel.F.shock1.factor.wheel*1
    outputs.F.Shock1.Shock_Inboard = travel.F.shock1.factor.inboard*1
    outputs.F.Shock1.Ideal_Ride_Freq = constant.F.target_initial_frequency*1
    outputs.F.Shock1.Ideal_Full_Bump_Freq = constant.F.target_final_frequency*1
    outputs.F.Shock1.Closest_Step_Up = constant.F.closest_match_SUR*1
    outputs.F.Shock1.Closest_Ride_Freq = constant.F.closest_match_Fni*1
    outputs.F.Shock1.Closest_Full_Bump_Freq = constant.F.closest_match_Fnf*1
    outputs.F.Shock1.Chosen_Step_Up = constant.F.used_SUR*1
    outputs.F.Shock1.Chosen_Ride_Freq = constant.F.used_Fni*1
    outputs.F.Shock1.Chosen_Full_Bump_Freq = constant.F.used_Fnf*1

    outputs.F.Shock2.Percent_Bump_Remaining = constant.F.shock2.percent_bump_reminaing*1
    outputs.F.Shock2.IR = travel.F.shock2.IR*1
    outputs.F.Shock2.Link_Ratio = constant.F.shock2.link_factor*1
    outputs.F.Shock2.Distance_Ratio = travel.F.shock2.factor.distance*1
    outputs.F.Shock2.Shock_Angle = travel.F.shock2.factor.shock_angle*1
    outputs.F.Shock2.Wheel_IC = travel.F.shock2.factor.wheel*1
    outputs.F.Shock2.Shock_Inboard = travel.F.shock2.factor.inboard*1

    outputs.R.Percent_Up_Travel = constant.R.percent_up_remaining*1
    outputs.R.Shock1.Percent_Bump_Remaining = constant.R.shock1.percent_bump_reminaing*1
    outputs.R.Shock1.IR = travel.R.shock1.IR*1
    outputs.R.Shock1.Link_Ratio = constant.R.shock1.link_factor*1
    outputs.R.Shock1.Distance_Ratio = travel.R.shock1.factor.distance*1
    outputs.R.Shock1.Shock_Angle = travel.R.shock1.factor.shock_angle*1
    outputs.R.Shock1.Wheel_IC = travel.R.shock1.factor.wheel*1
    outputs.R.Shock1.Shock_Inboard = travel.R.shock1.factor.inboard*1
    outputs.R.Shock1.Ideal_Ride_Freq = constant.R.target_initial_frequency*1
    outputs.R.Shock1.Ideal_Full_Bump_Freq = constant.R.target_final_frequency*1
    outputs.R.Shock1.Closest_Step_Up = constant.R.closest_match_SUR*1
    outputs.R.Shock1.Closest_Ride_Freq = constant.R.closest_match_Fni*1
    outputs.R.Shock1.Closest_Full_Bump_Freq = constant.R.closest_match_Fnf*1
    outputs.R.Shock1.Chosen_Step_Up = constant.R.used_SUR*1
    outputs.R.Shock1.Chosen_Ride_Freq = constant.R.used_Fni*1
    outputs.R.Shock1.Chosen_Full_Bump_Freq = constant.R.used_Fnf*1
    
    outputs.R.Shock2.Percent_Bump_Remaining = constant.R.shock2.percent_bump_reminaing*1
    outputs.R.Shock2.IR = travel.R.shock2.IR*1
    outputs.R.Shock2.Link_Ratio = constant.R.shock2.link_factor*1
    outputs.R.Shock2.Distance_Ratio = travel.R.shock2.factor.distance*1
    outputs.R.Shock2.Shock_Angle = travel.R.shock2.factor.shock_angle*1
    outputs.R.Shock2.Wheel_IC = travel.R.shock2.factor.wheel*1
    outputs.R.Shock2.Shock_Inboard = travel.R.shock2.factor.inboard*1

    if S.units == 'metric':
    # if metric convert all outputs to metric
        outputs.F.Dist_Between = in2mm(constant.F.shock_sep)
        
        outputs.F.Shock1.Full_Bump_Length = in2mm(constant.F.shock1.bump_length)
        outputs.F.Shock1.Full_Droop_Length = in2mm(constant.F.shock1.droop_length)
        outputs.F.Shock1.Lever_Arm_2_Body_Roll = in2mm(constant.F.shock1.distance_to_body_roll_axis)
        outputs.F.Shock1.Corner_Sprung_Weight = lb2kg(constant.F.corner_sprung_weight)
        outputs.F.Shock1.Ideal_Main_Spring = lbpin2npmm(constant.F.target_main_spring_rate)
        outputs.F.Shock1.Ideal_Tender_Spring = lbpin2npmm(constant.F.target_tender_spring_rate)
        outputs.F.Shock1.Closest_Main_Spring = lbpin2npmm(constant.F.closest_match_main_spring)
        outputs.F.Shock1.Closest_Tender_Spring = lbpin2npmm(constant.F.closest_match_tender_spring)
        outputs.F.Shock1.Closest_Preload = in2mm(constant.F.closest_match_preload)
        outputs.F.Shock1.Chosen_Preload = in2mm(constant.F.used_preload)

        outputs.F.Shock2.Full_Bump_Length = in2mm(constant.F.shock2.bump_length)
        outputs.F.Shock2.Full_Droop_Length = in2mm(constant.F.shock2.droop_length)
        outputs.F.Shock2.Lever_Arm_2_Body_Roll = in2mm(constant.F.shock2.distance_to_body_roll_axis)
        
        outputs.R.Dist_Between = in2mm(constant.R.shock_sep)
        
        outputs.R.Shock1.Full_Bump_Length = in2mm(constant.R.shock1.bump_length)
        outputs.R.Shock1.Full_Droop_Length = in2mm(constant.R.shock1.droop_length)
        outputs.R.Shock1.Lever_Arm_2_Body_Roll = in2mm(constant.R.shock1.distance_to_body_roll_axis)
        outputs.R.Shock1.Corner_Sprung_Weight = lb2kg(constant.R.corner_sprung_weight)
        outputs.R.Shock1.Ideal_Main_Spring = lbpin2npmm(constant.R.target_main_spring_rate)
        outputs.R.Shock1.Ideal_Tender_Spring = lbpin2npmm(constant.R.target_tender_spring_rate)
        outputs.R.Shock1.Closest_Main_Spring = lbpin2npmm(constant.R.closest_match_main_spring)
        outputs.R.Shock1.Closest_Tender_Spring = lbpin2npmm(constant.R.closest_match_tender_spring)
        
        outputs.R.Shock1.Closest_Preload = in2mm(constant.R.closest_match_preload)
        outputs.R.Shock1.Chosen_Preload = in2mm(constant.R.used_preload)

        outputs.F.Shock2.Full_Bump_Length = in2mm(constant.R.shock2.bump_length)
        outputs.R.Shock2.Full_Droop_Length = in2mm(constant.R.shock2.droop_length)
        outputs.R.Shock2.Lever_Arm_2_Body_Roll = in2mm(constant.R.shock2.distance_to_body_roll_axis)

        outputs.V.Closest_Anti_Pitching_Speed = mph2kmh(constant.V.closest_match_speed)
        outputs.V.Chosen_Anti_Pitching_Speed = mph2kmh(constant.V.used_match_speed)
    
    else:
        outputs.F.Dist_Between = constant.F.shock_sep
        
        outputs.F.Shock1.Full_Bump_Length = constant.F.shock1.bump_length*1
        outputs.F.Shock1.Full_Droop_Length = constant.F.shock1.droop_length*1
        outputs.F.Shock1.Lever_Arm_2_Body_Roll = constant.F.shock1.distance_to_body_roll_axis*1
        outputs.F.Shock1.Corner_Sprung_Weight = constant.F.corner_sprung_weight*1
        outputs.F.Shock1.Ideal_Main_Spring = constant.F.target_main_spring_rate*1
        outputs.F.Shock1.Ideal_Tender_Spring = constant.F.target_tender_spring_rate*1
        outputs.F.Shock1.Closest_Main_Spring = constant.F.closest_match_main_spring*1
        outputs.F.Shock1.Closest_Tender_Spring = constant.F.closest_match_tender_spring*1
        outputs.F.Shock1.Closest_Step_Up = constant.F.closest_match_SUR*1
        outputs.F.Shock1.Closest_Preload = constant.F.closest_match_preload*1
        outputs.F.Shock1.Chosen_Preload = constant.F.used_preload*1

        outputs.F.Shock2.Full_Bump_Length = constant.F.shock2.bump_length*1
        outputs.F.Shock2.Full_Droop_Length = constant.F.shock2.droop_length*1
        outputs.F.Shock2.Lever_Arm_2_Body_Roll = constant.F.shock2.distance_to_body_roll_axis*1
        
        outputs.R.Dist_Between = constant.R.shock_sep*1
        
        outputs.R.Shock1.Full_Bump_Length = constant.R.shock1.bump_length*1
        outputs.R.Shock1.Full_Droop_Length = constant.R.shock1.droop_length*1
        outputs.R.Shock1.Lever_Arm_2_Body_Roll = constant.R.shock1.distance_to_body_roll_axis*1
        outputs.R.Shock1.Corner_Sprung_Weight = constant.R.corner_sprung_weight*1
        outputs.R.Shock1.Ideal_Main_Spring = constant.R.target_main_spring_rate*1
        outputs.R.Shock1.Ideal_Tender_Spring = constant.R.target_tender_spring_rate*1
        outputs.R.Shock1.Closest_Main_Spring = constant.R.closest_match_main_spring*1
        outputs.R.Shock1.Closest_Tender_Spring = constant.R.closest_match_tender_spring*1
        outputs.R.Shock1.Closest_Step_Up = constant.R.closest_match_SUR*1
        outputs.R.Shock1.Closest_Preload = constant.R.closest_match_preload*1
        outputs.R.Shock1.Chosen_Preload = constant.R.used_preload*1

        outputs.F.Shock2.Full_Bump_Length = constant.R.shock2.bump_length*1
        outputs.R.Shock2.Full_Droop_Length = constant.R.shock2.droop_length*1
        outputs.R.Shock2.Lever_Arm_2_Body_Roll = constant.R.shock2.distance_to_body_roll_axis*1

        outputs.V.Closest_Anti_Pitching_Speed = constant.V.closest_match_speed*1
        outputs.V.Chosen_Anti_Pitching_Speed = constant.V.used_match_speed*1