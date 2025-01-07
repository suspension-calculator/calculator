# src/suspension/io/IO_Conversion/x_direction_change.py


def flip_front_x():
    from suspension.io.initialize_IO import inputs
    from suspension.io.variables import x

    inputs.F.LA[x] = inputs.F.LA[x] * -1
    inputs.F.LF[x] = inputs.F.LF[x] * -1
    inputs.F.UA[x] = inputs.F.UA[x] * -1
    inputs.F.UF[x] = inputs.F.UF[x] * -1
    inputs.F.PA[x] = inputs.F.PA[x] * -1
    inputs.F.PF[x] = inputs.F.PF[x] * -1

    inputs.F.pinion[x] = inputs.F.pinion[x] * -1
    inputs.F.T_case[x] = inputs.F.T_case[x] * -1

    inputs.F.shock1.chassis_mount[x] = inputs.F.shock1.chassis_mount[x] * -1
    inputs.F.shock1.susp_mount[x] = inputs.F.shock1.susp_mount[x] * -1

    inputs.F.shock2.chassis_mount[x] = inputs.F.shock2.chassis_mount[x] * -1
    inputs.F.shock2.susp_mount[x] = inputs.F.shock2.susp_mount[x] * -1
