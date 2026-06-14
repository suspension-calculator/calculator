# src/suspension/io/IO_Conversion/convert_all_inputs.py

# IO Imports
from tool_io.initialize_IO import inputs
from tool_io.variables import S

# Core Imports
from core.functions.unit_conversion import (
    in2mm,
    mm2in,
    kg2lb,
    lb2kg,
    kmh2mph,
    mph2kmh,
    npmm2lbpin,
    lbpin2npmm,
)

def unit_change():
    if S.units == "metric":
        S.position_units = "mm"
        S.mass_units = "kg"
        S.speed_units = "kph"
        S.pressure_units = "MPa"
        S.density_units = "kg/cm^3"
        S.force_units = "N"

        ############ Front
        # Link Geometry
        inputs.F.LA = in2mm(inputs.F.LA)
        inputs.F.LF = in2mm(inputs.F.LF)
        inputs.F.UA = in2mm(inputs.F.UA)
        inputs.F.UF = in2mm(inputs.F.UF)
        inputs.F.PA = in2mm(inputs.F.PA)
        inputs.F.PF = in2mm(inputs.F.PF)

        inputs.F.bump = in2mm(inputs.F.bump)
        inputs.F.droop = in2mm(inputs.F.droop)

        inputs.F.tire_radius = in2mm(inputs.F.tire_radius)
        inputs.F.tire_diameter = in2mm(inputs.F.tire_diameter)
        inputs.F.tire_width = in2mm(inputs.F.tire_width)
        inputs.F.portal_height = in2mm(inputs.F.portal_height)
        inputs.F.track_width = in2mm(inputs.F.track_width)
        inputs.F.axle_tube = in2mm(inputs.F.axle_tube)

        inputs.F.unsprung_mass = lb2kg(inputs.F.unsprung_mass)

        # Link Sizing
        inputs.F.U_OD = in2mm(inputs.F.U_OD)
        inputs.F.L_OD = in2mm(inputs.F.L_OD)
        inputs.F.P_OD = in2mm(inputs.F.P_OD)
        inputs.F.U_wall = in2mm(inputs.F.U_wall)
        inputs.F.L_wall = in2mm(inputs.F.L_wall)
        inputs.F.P_wall = in2mm(inputs.F.P_wall)

        # Driveshaft
        inputs.F.pinion = in2mm(inputs.F.pinion)
        inputs.F.T_case = in2mm(inputs.F.T_case)
        inputs.F.pinion_hypoid = in2mm(inputs.F.pinion_hypoid)
        inputs.F.pinion_length = in2mm(inputs.F.pinion_length)

        # Shocks
        inputs.F.preload_goal = in2mm(inputs.F.preload_goal)
        inputs.F.used_main_spring = lbpin2npmm(inputs.F.used_main_spring)
        inputs.F.used_tender_spring = lbpin2npmm(inputs.F.used_tender_spring)

        inputs.F.shock1.chassis_mount = in2mm(inputs.F.shock1.chassis_mount)
        inputs.F.shock1.susp_mount = in2mm(inputs.F.shock1.susp_mount)
        inputs.F.shock1.length_extended = in2mm(inputs.F.shock1.length_extended)
        inputs.F.shock1.length_compressed = in2mm(inputs.F.shock1.length_compressed)

        inputs.F.shock2.chassis_mount = in2mm(inputs.F.shock2.chassis_mount)
        inputs.F.shock2.susp_mount = in2mm(inputs.F.shock2.susp_mount)
        inputs.F.shock2.length_extended = in2mm(inputs.F.shock2.length_extended)
        inputs.F.shock2.length_compressed = in2mm(inputs.F.shock2.length_compressed)

        # Pitch
        inputs.F.pitch_travel = in2mm(inputs.F.pitch_travel)

        ############# REAR
        # Link Geometry

        inputs.R.LA = in2mm(inputs.R.LA)
        inputs.R.LF = in2mm(inputs.R.LF)
        inputs.R.UA = in2mm(inputs.R.UA)
        inputs.R.UF = in2mm(inputs.R.UF)
        inputs.R.PA = in2mm(inputs.R.PA)
        inputs.R.PF = in2mm(inputs.R.PF)

        inputs.R.bump = in2mm(inputs.R.bump)
        inputs.R.droop = in2mm(inputs.R.droop)

        inputs.R.tire_radius = in2mm(inputs.R.tire_radius)
        inputs.R.tire_diameter = in2mm(inputs.R.tire_diameter)
        inputs.R.tire_width = in2mm(inputs.R.tire_width)
        inputs.R.portal_height = in2mm(inputs.R.portal_height)
        inputs.R.track_width = in2mm(inputs.R.track_width)
        inputs.R.axle_tube = in2mm(inputs.R.axle_tube)

        inputs.R.unsprung_mass = lb2kg(inputs.R.unsprung_mass)

        # Link Sizing
        inputs.R.U_OD = in2mm(inputs.R.U_OD)
        inputs.R.L_OD = in2mm(inputs.R.L_OD)
        inputs.R.P_OD = in2mm(inputs.R.P_OD)
        inputs.R.U_wall = in2mm(inputs.R.U_wall)
        inputs.R.L_wall = in2mm(inputs.R.L_wall)
        inputs.R.P_wall = in2mm(inputs.R.P_wall)

        # Driveshaft
        inputs.R.pinion = in2mm(inputs.R.pinion)
        inputs.R.T_case = in2mm(inputs.R.T_case)
        inputs.R.pinion_hypoid = in2mm(inputs.R.pinion_hypoid)
        inputs.R.pinion_length = in2mm(inputs.R.pinion_length)

        # Shocks
        inputs.R.preload_goal = in2mm(inputs.R.preload_goal)
        inputs.R.used_main_spring = lbpin2npmm(inputs.R.used_main_spring)
        inputs.R.used_tender_spring = lbpin2npmm(inputs.R.used_tender_spring)

        inputs.R.shock1.chassis_mount = in2mm(inputs.R.shock1.chassis_mount)
        inputs.R.shock1.susp_mount = in2mm(inputs.R.shock1.susp_mount)
        inputs.R.shock1.length_extended = in2mm(inputs.R.shock1.length_extended)
        inputs.R.shock1.length_compressed = in2mm(inputs.R.shock1.length_compressed)

        inputs.R.shock2.chassis_mount = in2mm(inputs.R.shock2.chassis_mount)
        inputs.R.shock2.susp_mount = in2mm(inputs.R.shock2.susp_mount)
        inputs.R.shock2.length_extended = in2mm(inputs.R.shock2.length_extended)
        inputs.R.shock2.length_compressed = in2mm(inputs.R.shock2.length_compressed)

        # Pitch
        inputs.R.pitch_travel = in2mm(inputs.R.pitch_travel)

        ############### Vehicle
        inputs.V.wheelbase = in2mm(inputs.V.wheelbase)
        inputs.V.CG_height = in2mm(inputs.V.CG_height)
        inputs.V.mass = lb2kg(inputs.V.mass)

        inputs.V.desired_speed = mph2kmh(inputs.V.desired_speed)

    else:
        S.position_units = "in"
        S.mass_units = "lbs"
        S.speed_units = "mph"
        S.pressure_units = "psi"
        S.density_units = "lbs/in^3"
        S.force_units = "lbs"

        ############ Front
        # Link Geometry
        inputs.F.LA = mm2in(inputs.F.LA)
        inputs.F.LF = mm2in(inputs.F.LF)
        inputs.F.UA = mm2in(inputs.F.UA)
        inputs.F.UF = mm2in(inputs.F.UF)
        inputs.F.PA = mm2in(inputs.F.PA)
        inputs.F.PF = mm2in(inputs.F.PF)

        inputs.F.bump = mm2in(inputs.F.bump)
        inputs.F.droop = mm2in(inputs.F.droop)

        inputs.F.tire_radius = mm2in(inputs.F.tire_radius)
        inputs.F.tire_diameter = mm2in(inputs.F.tire_diameter)
        inputs.F.tire_width = mm2in(inputs.F.tire_width)
        inputs.F.portal_height = mm2in(inputs.F.portal_height)
        inputs.F.track_width = mm2in(inputs.F.track_width)
        inputs.F.axle_tube = mm2in(inputs.F.axle_tube)

        inputs.F.unsprung_mass = kg2lb(inputs.F.unsprung_mass)

        # Link Sizing
        inputs.F.U_OD = mm2in(inputs.F.U_OD)
        inputs.F.L_OD = mm2in(inputs.F.L_OD)
        inputs.F.P_OD = mm2in(inputs.F.P_OD)
        inputs.F.U_wall = mm2in(inputs.F.U_wall)
        inputs.F.L_wall = mm2in(inputs.F.L_wall)
        inputs.F.P_wall = mm2in(inputs.F.P_wall)

        # Driveshaft
        inputs.F.pinion = mm2in(inputs.F.pinion)
        inputs.F.T_case = mm2in(inputs.F.T_case)
        inputs.F.pinion_hypoid = mm2in(inputs.F.pinion_hypoid)
        inputs.F.pinion_length = mm2in(inputs.F.pinion_length)

        # Shocks
        inputs.F.preload_goal = mm2in(inputs.F.preload_goal)
        inputs.F.used_main_spring = npmm2lbpin(inputs.F.used_main_spring)
        inputs.F.used_tender_spring = npmm2lbpin(inputs.F.used_tender_spring)

        inputs.F.shock1.chassis_mount = mm2in(inputs.F.shock1.chassis_mount)
        inputs.F.shock1.susp_mount = mm2in(inputs.F.shock1.susp_mount)
        inputs.F.shock1.length_extended = mm2in(inputs.F.shock1.length_extended)
        inputs.F.shock1.length_compressed = mm2in(inputs.F.shock1.length_compressed)

        inputs.F.shock2.chassis_mount = mm2in(inputs.F.shock2.chassis_mount)
        inputs.F.shock2.susp_mount = mm2in(inputs.F.shock2.susp_mount)
        inputs.F.shock2.length_extended = mm2in(inputs.F.shock2.length_extended)
        inputs.F.shock2.length_compressed = mm2in(inputs.F.shock2.length_compressed)

        # Pitch
        inputs.F.pitch_travel = mm2in(inputs.F.pitch_travel)

        ############# REAR
        # Link Geometry

        inputs.R.LA = mm2in(inputs.R.LA)
        inputs.R.LF = mm2in(inputs.R.LF)
        inputs.R.UA = mm2in(inputs.R.UA)
        inputs.R.UF = mm2in(inputs.R.UF)
        inputs.R.PA = mm2in(inputs.R.PA)
        inputs.R.PF = mm2in(inputs.R.PF)

        inputs.R.bump = mm2in(inputs.R.bump)
        inputs.R.droop = mm2in(inputs.R.droop)

        inputs.R.tire_radius = mm2in(inputs.R.tire_radius)
        inputs.R.tire_diameter = mm2in(inputs.R.tire_diameter)
        inputs.R.tire_width = mm2in(inputs.R.tire_width)
        inputs.R.portal_height = mm2in(inputs.R.portal_height)
        inputs.R.track_width = mm2in(inputs.R.track_width)
        inputs.R.axle_tube = mm2in(inputs.R.axle_tube)

        inputs.R.unsprung_mass = kg2lb(inputs.R.unsprung_mass)

        # Link Sizing
        inputs.R.U_OD = mm2in(inputs.R.U_OD)
        inputs.R.L_OD = mm2in(inputs.R.L_OD)
        inputs.R.P_OD = mm2in(inputs.R.P_OD)
        inputs.R.U_wall = mm2in(inputs.R.U_wall)
        inputs.R.L_wall = mm2in(inputs.R.L_wall)
        inputs.R.P_wall = mm2in(inputs.R.P_wall)

        # Driveshaft
        inputs.R.pinion = mm2in(inputs.R.pinion)
        inputs.R.T_case = mm2in(inputs.R.T_case)
        inputs.R.pinion_hypoid = mm2in(inputs.R.pinion_hypoid)
        inputs.R.pinion_length = mm2in(inputs.R.pinion_length)

        # Shocks
        inputs.R.preload_goal = mm2in(inputs.R.preload_goal)
        inputs.R.used_main_spring = npmm2lbpin(inputs.R.used_main_spring)
        inputs.R.used_tender_spring = npmm2lbpin(inputs.R.used_tender_spring)

        inputs.R.shock1.chassis_mount = mm2in(inputs.R.shock1.chassis_mount)
        inputs.R.shock1.susp_mount = mm2in(inputs.R.shock1.susp_mount)
        inputs.R.shock1.length_extended = mm2in(inputs.R.shock1.length_extended)
        inputs.R.shock1.length_compressed = mm2in(inputs.R.shock1.length_compressed)

        inputs.R.shock2.chassis_mount = mm2in(inputs.R.shock2.chassis_mount)
        inputs.R.shock2.susp_mount = mm2in(inputs.R.shock2.susp_mount)
        inputs.R.shock2.length_extended = mm2in(inputs.R.shock2.length_extended)
        inputs.R.shock2.length_compressed = mm2in(inputs.R.shock2.length_compressed)

        # Pitch
        inputs.R.pitch_travel = mm2in(inputs.R.pitch_travel)

        ############### Vehicle
        inputs.V.wheelbase = mm2in(inputs.V.wheelbase)
        inputs.V.CG_height = mm2in(inputs.V.CG_height)
        inputs.V.mass = kg2lb(inputs.V.mass)

        inputs.V.desired_speed = kmh2mph(inputs.V.desired_speed)
