# src/suspension/io/load_suspension.py

def load_susp():
    from suspension.io.variables import S,x,y,z
    from suspension.io.initialize_IO import inputs
    from calculations.link_calc import run_link_calc
    from calculations.link_sizing import run_link_sizing
    from calculations.driveshaft import run_driveshaft
    from calculations.shocks import run_shocks
    from calculations.vehicle_pitch import run_vehicle_pitch
    from suspension.io.material_add import add_material
    from suspension.io.rod_end_add import add_rod_end
    import csv
    from tkinter import filedialog
    import tkinter as tk
    from pathlib import Path

    S.file_mame = filedialog.askopenfilename(initialdir = Path.cwd(),title="Open File",filetypes=(("text files","*.txt"),("all files","*.*")))

    with open(S.file_mame,'r') as file:
        saved = csv.reader(file)
        for row in saved:
            field = row[0]
            match field:
                case 'units':
                    S.units = row[1]
                    if S.units == 'metric':
                        S.position_units = "mm"
                        S.mass_units = "kg"
                        S.speed_units = "kph"
                        S.pressure_units = "MPa"
                        S.density_units = "kg/cm^3"
                        S.force_units = "N"
                    else:
                        S.position_units = "in"
                        S.mass_units = "lbs"
                        S.speed_units = "mph"
                        S.pressure_units = "psi"
                        S.density_units = "lbs/in^3"
                        S.force_units = "lbs"
                case 'reversed front x':
                    S.reversed_front_x = row[1] == "True"
                case 'tire loading':
                    S.simulate_tire_loading = row[1] == "True"
                case 'sample points':
                    S.sample_points = int(row[1])
                case 'front type':
                    match row[1]:
                        case 'SA triangualted 4 link':
                            inputs.F.U_count = 2
                            inputs.F.panhard = False
                        case 'SA 3 link with panhard':
                            inputs.F.U_count = 1
                            inputs.F.panhard = True
                        case 'SA 4 link with panhard':
                            inputs.F.U_count = 2
                            inputs.F.panhard = True
                        case'SA radius arm':
                            inputs.F.U_count = 2
                            inputs.F.panhard = True
                case 'front upper frame':
                    inputs.F.UF[x] = float(row[1])
                    inputs.F.UF[y] = float(row[2])
                    inputs.F.UF[z] = float(row[3])
                case 'front upper axle':
                    inputs.F.UA[x] = float(row[1])
                    inputs.F.UA[y] = float(row[2])
                    inputs.F.UA[z] = float(row[3])
                case 'front lower frame':
                    inputs.F.LF[x] = float(row[1])
                    inputs.F.LF[y] = float(row[2])
                    inputs.F.LF[z] = float(row[3])
                case 'front lower axle':
                    inputs.F.LA[x] = float(row[1])
                    inputs.F.LA[y] = float(row[2])
                    inputs.F.LA[z] = float(row[3])
                case 'front panhard frame':
                    inputs.F.PF[x] = float(row[1])
                    inputs.F.PF[y] = float(row[2])
                    inputs.F.PF[z] = float(row[3])
                case 'front panhard axle':
                    inputs.F.PA[x] = float(row[1])
                    inputs.F.PA[y] = float(row[2])
                    inputs.F.PA[z] = float(row[3])
                case 'front bump':
                    inputs.F.bump = float(row[1])
                case 'front droop':
                    inputs.F.droop = float(row[1])
                case 'front tire radius':
                    inputs.F.tire_radius = float(row[1])
                case 'front tire diameter':
                    inputs.F.tire_diameter = float(row[1])
                case 'front tire width':
                    inputs.F.tire_width = float(row[1])
                case 'front portal height':
                    inputs.F.portal_height = float(row[1])
                case 'front track width':
                    inputs.F.track_width = float(row[1])
                case 'front mass':
                    inputs.F.unsprung_mass = float(row[1])
                case 'front upper od':
                    inputs.F.U_OD = float(row[1])
                case 'front lower od':
                    inputs.F.L_OD = float(row[1])
                case 'front panhard od':
                    inputs.F.P_OD = float(row[1])
                case 'front upper wall':
                    inputs.F.U_wall = float(row[1])
                case 'front lower wall':
                    inputs.F.L_wall = float(row[1])
                case 'front panhard wall':
                    inputs.F.P_wall = float(row[1])
                case 'front upper solid':
                    inputs.F.U_solid = row[1] == "True"
                case 'front lower solid':
                    inputs.F.L_solid = row[1] == "True"
                case 'front panhard solid':
                    inputs.F.P_solid = row[1] == "True"
                case 'front upper material':
                    add_material(row[1],row[2],row[3],row[4],row[5])
                    inputs.F.U_material = row[1]
                case 'front lower material':
                    add_material(row[1],row[2],row[3],row[4],row[5])
                    inputs.F.L_material = row[1]
                case 'front panhard material':
                    add_material(row[1],row[2],row[3],row[4],row[5])
                    inputs.F.P_material = row[1]
                case 'front upper rod end':
                    add_rod_end(row[1],row[2],row[3],row[4],row[5],row[6])
                    inputs.F.U_rod_end = row[1]
                case 'front lower rod end':
                    add_rod_end(row[1],row[2],row[3],row[4],row[5],row[6])
                    inputs.F.L_rod_end = row[1]
                case 'front panhard rod end':
                    add_rod_end(row[1],row[2],row[3],row[4],row[5],row[6])
                    inputs.F.P_rod_end = row[1]
                case 'front pinion':
                    inputs.F.pinion[x] = float(row[1])
                    inputs.F.pinion[y] = float(row[2])
                    inputs.F.pinion[z] = float(row[3])
                case 'front T case':
                    inputs.F.T_case[x] = float(row[1])
                    inputs.F.T_case[y] = float(row[2])
                    inputs.F.T_case[z] = float(row[3])
                case 'front pinion location method':
                    inputs.F.pinion_location_method = float(row[1])
                case 'front T case side angle':
                    inputs.F.T_case_side_angle = float(row[1])
                case 'front T case top angle':
                    inputs.F.T_case_top_angle = float(row[1])
                case 'front pinion angle':
                    inputs.F.pinion_angle = float(row[1])
                case 'front pinion hypoid':
                    inputs.F.pinion_hypoid = float(row[1])
                case 'front pinion length':
                    inputs.F.pinion_length = float(row[1])
                case 'front caster':
                    inputs.F.caster = float(row[1])
                case 'front spring method':
                    inputs.F.spring_method = float(row[1])
                case 'front freq goal':
                    inputs.F.freq_goal = float(row[1])
                case 'front preload goal':
                    inputs.F.preload_goal = float(row[1])
                case 'front step up ratio':
                    inputs.F.step_up_ratio = float(row[1])
                case 'front used main spring':
                    inputs.F.used_main_spring = float(row[1])
                case 'front used tender spring':
                    inputs.F.used_tender_spring = float(row[1])
                case 'front shock 1 size':
                    inputs.F.shock1.size = row[1]
                case 'front shock 1 travel':
                    inputs.F.shock1.travel = int(row[1])
                case 'front shock 1 main spring extra length':
                    inputs.F.shock1.main_spring_extra_length = float(row[1])
                case 'front shock 1 chassis mount':
                    inputs.F.shock1.chassis_mount[x] = float(row[1])
                    inputs.F.shock1.chassis_mount[y] = float(row[2])
                    inputs.F.shock1.chassis_mount[z] = float(row[3])
                case 'front shock 1 susp mount':
                    inputs.F.shock1.susp_mount[x] = float(row[1])
                    inputs.F.shock1.susp_mount[y] = float(row[2])
                    inputs.F.shock1.susp_mount[z] = float(row[3])
                case 'front shock 1 location':
                    inputs.F.shock1.location = float(row[1])
                case 'front shock 1 length extended':
                    inputs.F.shock1.length_extended = float(row[1])
                case 'front shock 1 length compressed':
                    inputs.F.shock1.length_compressed = float(row[1])
                case 'front shock 2 size':
                    inputs.F.shock2.size = row[1]
                case 'front shock 2 travel':
                    inputs.F.shock2.travel = float(row[1])
                case 'front shock 2 chassis mount':
                    inputs.F.shock2.chassis_mount[x] = float(row[1])
                    inputs.F.shock2.chassis_mount[y] = float(row[2])
                    inputs.F.shock2.chassis_mount[z] = float(row[3])
                case 'front shock 2 susp mount':
                    inputs.F.shock2.susp_mount[x] = float(row[1])
                    inputs.F.shock2.susp_mount[y] = float(row[2])
                    inputs.F.shock2.susp_mount[z] = float(row[3])
                case 'front shock 2 location':
                    inputs.F.shock2.location = float(row[1])
                case 'front shock 2 exists':
                    inputs.F.shock2.exists = row[1] == "True"
                case 'front shock 2 length extended':
                    inputs.F.shock2.length_extended = float(row[1])
                case 'front shock 2 length compressed':
                    inputs.F.shock2.length_compressed = float(row[1])
                case 'rear type':
                    match row[1]:
                        case 'SA triangualted 4 link':
                            inputs.R.U_count = 2
                            inputs.R.panhard = False
                        case 'SA 3 link with panhard':
                            inputs.R.U_count = 1
                            inputs.R.panhard = True
                        case 'SA 4 link with panhard':
                            inputs.R.U_count = 2
                            inputs.R.panhard = True
                        case'SA radius arm':
                            inputs.R.U_count = 2
                            inputs.R.panhard = True
                case 'rear upper frame':
                    inputs.R.UF[x] = float(row[1])
                    inputs.R.UF[y] = float(row[2])
                    inputs.R.UF[z] = float(row[3])
                case 'rear upper axle':
                    inputs.R.UA[x] = float(row[1])
                    inputs.R.UA[y] = float(row[2])
                    inputs.R.UA[z] = float(row[3])
                case 'rear lower frame':
                    inputs.R.LF[x] = float(row[1])
                    inputs.R.LF[y] = float(row[2])
                    inputs.R.LF[z] = float(row[3])
                case 'rear lower axle':
                    inputs.R.LA[x] = float(row[1])
                    inputs.R.LA[y] = float(row[2])
                    inputs.R.LA[z] = float(row[3])
                case 'rear panhard frame':
                    inputs.R.PF[x] = float(row[1])
                    inputs.R.PF[y] = float(row[2])
                    inputs.R.PF[z] = float(row[3])
                case 'rear panhard axle':
                    inputs.R.PA[x] = float(row[1])
                    inputs.R.PA[y] = float(row[2])
                    inputs.R.PA[z] = float(row[3])
                case 'rear bump':
                    inputs.R.bump = float(row[1])
                case 'rear droop':
                    inputs.R.droop = float(row[1])
                case 'rear tire radius':
                    inputs.R.tire_radius = float(row[1])
                case 'rear tire diameter':
                    inputs.R.tire_diameter = float(row[1])
                case 'rear tire width':
                    inputs.R.tire_width = float(row[1])
                case 'rear portal height':
                    inputs.R.portal_height = float(row[1])
                case 'rear track width':
                    inputs.R.track_width = float(row[1])
                case 'rear mass':
                    inputs.R.unsprung_mass = float(row[1])
                case 'rear upper od':
                    inputs.R.U_OD = float(row[1])
                case 'rear lower od':
                    inputs.R.L_OD = float(row[1])
                case 'rear panhard od':
                    inputs.R.P_OD = float(row[1])
                case 'rear upper wall':
                    inputs.R.U_wall = float(row[1])
                case 'rear lower wall':
                    inputs.R.L_wall = float(row[1])
                case 'rear panhard wall':
                    inputs.R.P_wall = float(row[1])
                case 'rear upper solid':
                    inputs.R.U_solid = row[1] == "True"
                case 'rear lower solid':
                    inputs.R.L_solid = row[1] == "True"
                case 'rear panhard solid':
                    inputs.R.P_solid = row[1] == "True"
                case 'rear upper material':
                    add_material(row[1],row[2],row[3],row[4],row[5])
                    inputs.R.U_material = row[1]
                case 'rear lower material':
                    add_material(row[1],row[2],row[3],row[4],row[5])
                    inputs.R.L_material = row[1]
                case 'rear panhard material':
                    add_material(row[1],row[2],row[3],row[4],row[5])
                    inputs.R.P_material = row[1]
                case 'rear upper rod end':
                    add_rod_end(row[1],row[2],row[3],row[4],row[5],row[6])
                    inputs.R.U_rod_end = row[1]
                case 'rear lower rod end':
                    add_rod_end(row[1],row[2],row[3],row[4],row[5],row[6])
                    inputs.R.L_rod_end = row[1]
                case 'rear panhard rod end':
                    add_rod_end(row[1],row[2],row[3],row[4],row[5],row[6])
                    inputs.R.P_rod_end = row[1]
                case 'rear pinion':
                    inputs.R.pinion[x] = float(row[1])
                    inputs.R.pinion[y] = float(row[2])
                    inputs.R.pinion[z] = float(row[3])
                case 'rear T case':
                    inputs.R.T_case[x] = float(row[1])
                    inputs.R.T_case[y] = float(row[2])
                    inputs.R.T_case[z] = float(row[3])
                case 'rear pinion location method':
                    inputs.R.pinion_location_method = float(row[1])
                case 'rear T case side angle':
                    inputs.R.T_case_side_angle = float(row[1])
                case 'rear T case top angle':
                    inputs.R.T_case_top_angle = float(row[1])
                case 'rear pinion angle':
                    inputs.R.pinion_angle = float(row[1])
                case 'rear pinion hypoid':
                    inputs.R.pinion_hypoid = float(row[1])
                case 'rear pinion length':
                    inputs.R.pinion_length = float(row[1])
                case 'rear caster':
                    inputs.R.caster = float(row[1])
                case 'rear spring method':
                    inputs.R.spring_method = float(row[1])
                case 'rear freq goal':
                    inputs.R.freq_goal = float(row[1])
                case 'rear preload goal':
                    inputs.R.preload_goal = float(row[1])
                case 'rear step up ratio':
                    inputs.R.step_up_ratio = float(row[1])
                case 'rear used main spring':
                    inputs.R.used_main_spring = float(row[1])
                case 'rear used tender spring':
                    inputs.R.used_tender_spring = float(row[1])
                case 'rear shock 1 size':
                    inputs.R.shock1.size = row[1]
                case 'rear shock 1 travel':
                    inputs.R.shock1.travel = int(row[1])
                case 'rear shock 1 main spring extra length':
                    inputs.R.shock1.main_spring_extra_length = float(row[1])
                case 'rear shock 1 chassis mount':
                    inputs.R.shock1.chassis_mount[x] = float(row[1])
                    inputs.R.shock1.chassis_mount[y] = float(row[2])
                    inputs.R.shock1.chassis_mount[z] = float(row[3])
                case 'rear shock 1 susp mount':
                    inputs.R.shock1.susp_mount[x] = float(row[1])
                    inputs.R.shock1.susp_mount[y] = float(row[2])
                    inputs.R.shock1.susp_mount[z] = float(row[3])
                case 'rear shock 1 location':
                    inputs.R.shock1.location = float(row[1])
                case 'rear shock 1 length extended':
                    inputs.R.shock1.length_extended = float(row[1])
                case 'rear shock 1 length compressed':
                    inputs.R.shock1.length_compressed = float(row[1])
                case 'rear shock 2 size':
                    inputs.R.shock2.size = float(row[1])
                case 'rear shock 2 travel':
                    inputs.R.shock2.travel = float(row[1])
                case 'rear shock 2 chassis mount':
                    inputs.R.shock2.chassis_mount[x] = float(row[1])
                    inputs.R.shock2.chassis_mount[y] = float(row[2])
                    inputs.R.shock2.chassis_mount[z] = float(row[3])
                case 'rear shock 2 susp mount':
                    inputs.R.shock2.susp_mount[x] = float(row[1])
                    inputs.R.shock2.susp_mount[y] = float(row[2])
                    inputs.R.shock2.susp_mount[z] = float(row[3])
                case 'rear shock 2 location':
                    inputs.R.shock2.location = float(row[1])
                case 'rear shock 2 exists':
                    inputs.R.shock2.exists = row[1] == "True"
                case 'rear shock 2 length extended':
                    inputs.R.shock2.length_extended = float(row[1])
                case 'rear shock 2 length compressed':
                    inputs.R.shock2.length_compressed = float(row[1])
                case 'rear pitch travel':
                    inputs.R.pitch_travel = float(row[1])
                case 'vehicle wheelbase':
                    inputs.V.wheelbase = float(row[1])
                case 'vehicle drive bias':
                    inputs.V.drive_bias = float(row[1])
                case 'vehicle brake bias':
                    inputs.V.brake_bias = float(row[1])
                case 'vehicle CG height':
                    inputs.V.CG_height = float(row[1])
                case 'vehicle weight distribution':
                    inputs.V.weight_distribution = float(row[1])
                case 'vehicle mass':
                    inputs.V.mass = float(row[1])
                case 'vehicle acceleration':
                    inputs.V.acceleration = float(row[1])
                case 'vehicle transverse acceleration':
                    inputs.V.Desired_FS_Yield = float(row[1])
                case 'vehicle desired FS buckling':
                    inputs.V.Desired_FS_Buckling = float(row[1])
                case 'vehicle desired FS bending':
                    inputs.V.Desired_FS_Bending = float(row[1])
                case 'vehicle desired FS rod end':
                    inputs.V.Desired_FS_RE = float(row[1])
                case 'vehicle desired FS denting':
                    inputs.V.Desired_FS_Dent = float(row[1])
                case 'vehicle desired speed':
                    inputs.V.desired_speed = float(row[1])
                case 'vehicle freq approach':
                    inputs.V.freq_approach = float(row[1])
                case 'vehicle spring method':
                    inputs.V.spring_method = float(row[1])
                case 'vehicle pitch slope':
                    inputs.V.pitch_slope = float(row[1])
                case 'vehicle pitch acceleration':
                    inputs.V.pitch_acceleration = float(row[1])
                case 'vehicle pitch drive bias':
                    inputs.V.pitch_drive_bias = float(row[1])
                case 'vehicle pitch brake bias':
                    inputs.V.pitch_brake_bias = float(row[1])
        
    run_link_calc()
    run_link_sizing()
    run_driveshaft()
    run_shocks()
    run_vehicle_pitch()