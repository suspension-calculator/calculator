# VariablesIO/IO_Conversion/driveshaft_IO.py

def input_processing_driveshaft():
    from VariableIO.initialize_IO import inputs
    from VariableIO.variables import constant,S,x,y,z
    from Functions.unit_conversion import in2mm, mm2in, kg2lb, lb2kg, kmh2mph, mph2kmh, npmm2lbpin, lbpin2npmm
    from math import radians

    #degree to rad conversion
    constant.F.T_case_side_angle = radians(inputs.F.T_case_side_angle)
    constant.F.T_case_top_angle = radians(inputs.F.T_case_top_angle)
    constant.F.pinion_angle = radians(inputs.F.pinion_angle)
    constant.F.caster = radians(inputs.F.caster)

    constant.R.T_case_side_angle = -radians(inputs.R.T_case_side_angle)
    constant.R.T_case_top_angle = radians(inputs.R.T_case_top_angle)
    constant.R.pinion_angle = radians(inputs.R.pinion_angle)
    constant.R.caster = radians(inputs.R.caster)

    constant.F.pinion_location_method = inputs.F.pinion_location_method*1
    constant.R.pinion_location_method = inputs.R.pinion_location_method*1

    if S.units == 'metric':
        # if metric convert all inputs to sae and set variables

        constant.F.pinion = mm2in(inputs.F.pinion)
        constant.F.T_case = mm2in(inputs.F.T_case)
        constant.F.pinion_hypoid = mm2in(inputs.F.pinion_hypoid)
        constant.F.pinion_length = mm2in(inputs.F.pinion_length)

        constant.R.pinion = mm2in(inputs.R.pinion)
        constant.R.T_case = mm2in(inputs.R.T_case)
        constant.R.pinion_hypoid = mm2in(inputs.R.pinion_hypoid)
        constant.R.pinion_length = mm2in(inputs.R.pinion_length)

    else:
        # set variables
        constant.F.pinion = inputs.F.pinion*1
        constant.F.T_case = inputs.F.T_case*1
        constant.F.pinion_hypoid = inputs.F.pinion_hypoid*1
        constant.F.pinion_length = inputs.F.pinion_length*1

        constant.R.pinion = inputs.R.pinion*1
        constant.R.T_case = inputs.R.T_case*1
        constant.R.pinion_hypoid = inputs.R.pinion_hypoid*1
        constant.R.pinion_length = inputs.R.pinion_length*1

    if S.reversed_front_x:
        constant.F.pinion[x] = constant.V.wheelbase - constant.F.pinion[x]
        constant.F.T_case[x] = constant.V.wheelbase - constant.F.T_case[x]
    else:
        constant.F.pinion[x] = constant.V.wheelbase + constant.F.pinion[x]
        constant.F.T_case[x] = constant.V.wheelbase + constant.F.T_case[x]
        

def output_processing_driveshaft():
    from VariableIO.initialize_IO import outputs
    from VariableIO.variables import constant,travel,S
    from Functions.unit_conversion import in2mm, mm2in, kg2lb, lb2kg, kmh2mph, mph2kmh, npmm2lbpin, lbpin2npmm, lb2N
    from math import pi

    outputs.F.T_Case_U_Joint = travel.F.T_case_U_joint_angle_rad*180/pi
    outputs.F.Pinion_U_Joint = travel.F.pinion_U_joint_angle_rad*180/pi
    
    outputs.R.T_Case_U_Joint = travel.R.T_case_U_joint_angle_rad*180/pi
    outputs.R.Pinion_U_Joint = travel.R.pinion_U_joint_angle_rad*180/pi

    if S.units == 'metric':
    # if metric convert all outputs to metric
        outputs.F.Max_Length = in2mm(constant.F.driveshaft_max_length)
        outputs.F.Ride_Length = in2mm(constant.F.driveshaft_length_ride)
        outputs.F.Min_Length = in2mm(constant.F.driveshaft_min_length)
        outputs.F.Driveshaft_Travel = in2mm(constant.F.driveshaft_length_delta)
    
        outputs.R.Max_Length = in2mm(constant.R.driveshaft_max_length)
        outputs.R.Ride_Length = in2mm(constant.R.driveshaft_length_ride)
        outputs.R.Min_Length = in2mm(constant.R.driveshaft_min_length)
        outputs.R.Driveshaft_Travel = in2mm(constant.R.driveshaft_length_delta)

    else:
        outputs.F.Max_Length = constant.F.driveshaft_max_length*1
        outputs.F.Ride_Length = constant.F.driveshaft_length_ride*1
        outputs.F.Min_Length = constant.F.driveshaft_min_length*1
        outputs.F.Driveshaft_Travel = constant.F.driveshaft_length_delta*1

        outputs.R.Max_Length = constant.R.driveshaft_max_length*1
        outputs.R.Ride_Length = constant.R.driveshaft_length_ride*1
        outputs.R.Min_Length = constant.R.driveshaft_min_length*1
        outputs.R.Driveshaft_Travel = constant.R.driveshaft_length_delta*1