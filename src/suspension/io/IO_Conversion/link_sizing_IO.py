# src/suspension/io/IO_Conversion/link_sizing_IO.py


def input_processing_link_sizing():
    from suspension.io.initialize_IO import inputs
    from suspension.io.variables import constant, S
    from suspension.core.functions.unit_conversion import (
        mm2in,
    )

    # degree to rad conversion

    constant.F.U_solid = inputs.F.U_solid
    constant.F.L_solid = inputs.F.L_solid
    constant.F.P_solid = inputs.F.P_solid

    constant.F.U_material = inputs.F.U_material
    constant.F.L_material = inputs.F.L_material
    constant.F.P_material = inputs.F.P_material

    constant.F.U_rod_end = inputs.F.U_rod_end
    constant.F.L_rod_end = inputs.F.L_rod_end
    constant.F.P_rod_end = inputs.F.P_rod_end

    constant.R.U_solid = inputs.R.U_solid
    constant.R.L_solid = inputs.R.L_solid
    constant.R.P_solid = inputs.R.P_solid

    constant.R.U_material = inputs.R.U_material
    constant.R.L_material = inputs.R.L_material
    constant.R.P_material = inputs.R.P_material

    constant.R.U_rod_end = inputs.R.U_rod_end
    constant.R.L_rod_end = inputs.R.L_rod_end
    constant.R.P_rod_end = inputs.R.P_rod_end

    constant.V.Desired_FS_Yield = inputs.V.Desired_FS_Yield * 1
    constant.V.Desired_FS_Buckling = inputs.V.Desired_FS_Buckling * 1
    constant.V.Desired_FS_Bending = inputs.V.Desired_FS_Bending * 1
    constant.V.Desired_FS_RE = inputs.V.Desired_FS_RE * 1
    constant.V.Desired_FS_Dent = inputs.V.Desired_FS_Dent * 1

    if S.units == "metric":
        # if metric convert all inputs to sae and set variables

        constant.F.U_OD = mm2in(inputs.F.U_OD)
        constant.F.L_OD = mm2in(inputs.F.L_OD)
        constant.F.P_OD = mm2in(inputs.F.P_OD)
        constant.F.U_wall = mm2in(inputs.F.U_wall)
        constant.F.L_wall = mm2in(inputs.F.L_wall)
        constant.F.P_wall = mm2in(inputs.F.P_wall)

        constant.F.pinion = mm2in(inputs.F.pinion)
        constant.F.T_case = mm2in(inputs.F.T_case)
        constant.F.pinion_hypoid = mm2in(inputs.F.pinion_hypoid)
        constant.F.pinion_length = mm2in(inputs.F.pinion_length)

        constant.R.U_OD = mm2in(inputs.R.U_OD)
        constant.R.L_OD = mm2in(inputs.R.L_OD)
        constant.R.P_OD = mm2in(inputs.R.P_OD)
        constant.R.U_wall = mm2in(inputs.R.U_wall)
        constant.R.L_wall = mm2in(inputs.R.L_wall)
        constant.R.P_wall = mm2in(inputs.R.P_wall)

    else:
        # set variables
        constant.F.U_OD = inputs.F.U_OD * 1
        constant.F.L_OD = inputs.F.L_OD * 1
        constant.F.P_OD = inputs.F.P_OD * 1
        constant.F.U_wall = inputs.F.U_wall * 1
        constant.F.L_wall = inputs.F.L_wall * 1
        constant.F.P_wall = inputs.F.P_wall * 1

        constant.R.U_OD = inputs.R.U_OD * 1
        constant.R.L_OD = inputs.R.L_OD * 1
        constant.R.P_OD = inputs.R.P_OD * 1
        constant.R.U_wall = inputs.R.U_wall * 1
        constant.R.L_wall = inputs.R.L_wall * 1
        constant.R.P_wall = inputs.R.P_wall * 1
        a = 1


def output_processing_link_sizing():
    from suspension.io.initialize_IO import outputs
    from suspension.io.variables import constant, S
    from suspension.core.functions.unit_conversion import (
        lb2kg,
    )

    outputs.F.U_Thread = constant.sizing.RE_thread[0]
    outputs.F.L_Thread = constant.sizing.RE_thread[1]
    outputs.F.P_Thread = constant.sizing.RE_thread[4]
    outputs.F.U_Hole = constant.sizing.RE_hole_diameter[0]
    outputs.F.L_Hole = constant.sizing.RE_hole_diameter[1]
    outputs.F.P_Hole = constant.sizing.RE_hole_diameter[4]
    outputs.F.U_FS_Yield = constant.sizing.FS_yield[0]
    outputs.F.L_FS_Yield = constant.sizing.FS_yield[1]
    outputs.F.P_FS_Yield = constant.sizing.FS_yield[4]
    outputs.F.U_FS_buckling = constant.sizing.FS_buckling[0]
    outputs.F.L_FS_buckling = constant.sizing.FS_buckling[1]
    outputs.F.P_FS_buckling = constant.sizing.FS_buckling[4]
    outputs.F.U_FS_bending = constant.sizing.FS_bending[0]
    outputs.F.L_FS_bending = constant.sizing.FS_bending[1]
    outputs.F.P_FS_bending = constant.sizing.FS_bending[4]
    outputs.F.U_Dent_Resistance = constant.sizing.dent_resistance[0]
    outputs.F.L_Dent_Resistance = constant.sizing.dent_resistance[1]
    outputs.F.P_Dent_Resistance = constant.sizing.dent_resistance[4]
    outputs.F.U_FS_RE = constant.sizing.FS_RE[0]
    outputs.F.L_FS_RE = constant.sizing.FS_RE[1]
    outputs.F.P_FS_RE = constant.sizing.FS_RE[4]

    outputs.R.U_Thread = constant.sizing.RE_thread[2]
    outputs.R.L_Thread = constant.sizing.RE_thread[3]
    outputs.R.P_Thread = constant.sizing.RE_thread[5]
    outputs.R.U_Hole = constant.sizing.RE_hole_diameter[2]
    outputs.R.L_Hole = constant.sizing.RE_hole_diameter[3]
    outputs.R.P_Hole = constant.sizing.RE_hole_diameter[5]
    outputs.R.U_FS_Yield = constant.sizing.FS_yield[2]
    outputs.R.L_FS_Yield = constant.sizing.FS_yield[3]
    outputs.R.P_FS_Yield = constant.sizing.FS_yield[5]
    outputs.R.U_FS_buckling = constant.sizing.FS_buckling[2]
    outputs.R.L_FS_buckling = constant.sizing.FS_buckling[3]
    outputs.R.P_FS_buckling = constant.sizing.FS_buckling[5]
    outputs.R.U_FS_bending = constant.sizing.FS_bending[2]
    outputs.R.L_FS_bending = constant.sizing.FS_bending[3]
    outputs.R.P_FS_bending = constant.sizing.FS_bending[5]
    outputs.R.U_Dent_Resistance = constant.sizing.dent_resistance[2]
    outputs.R.L_Dent_Resistance = constant.sizing.dent_resistance[3]
    outputs.R.P_Dent_Resistance = constant.sizing.dent_resistance[5]
    outputs.R.U_FS_RE = constant.sizing.FS_RE[2]
    outputs.R.L_FS_RE = constant.sizing.FS_RE[3]
    outputs.R.P_FS_RE = constant.sizing.FS_RE[5]

    if S.units == "metric":
        # if metric convert all outputs to metric
        outputs.F.U_Link_Weight = lb2kg(constant.sizing.link_weight[0])
        outputs.F.L_Link_Weight = lb2kg(constant.sizing.link_weight[1])
        outputs.F.P_Link_Weight = lb2kg(constant.sizing.link_weight[4])
        outputs.F.U_RE_Weight = lb2kg(constant.sizing.RE_weight[0])
        outputs.F.L_RE_Weight = lb2kg(constant.sizing.RE_weight[1])
        outputs.F.P_RE_Weight = lb2kg(constant.sizing.RE_weight[4])
        outputs.F.U_Weight = lb2kg(constant.sizing.total_link_weight[0])
        outputs.F.L_Weight = lb2kg(constant.sizing.total_link_weight[1])
        outputs.F.P_Weight = lb2kg(constant.sizing.total_link_weight[4])

        outputs.R.U_Link_Weight = lb2kg(constant.sizing.link_weight[2])
        outputs.R.L_Link_Weight = lb2kg(constant.sizing.link_weight[3])
        outputs.R.P_Link_Weight = lb2kg(constant.sizing.link_weight[5])
        outputs.R.U_RE_Weight = lb2kg(constant.sizing.RE_weight[2])
        outputs.R.L_RE_Weight = lb2kg(constant.sizing.RE_weight[3])
        outputs.R.P_RE_Weight = lb2kg(constant.sizing.RE_weight[5])
        outputs.R.U_Weight = lb2kg(constant.sizing.total_link_weight[2])
        outputs.R.L_Weight = lb2kg(constant.sizing.total_link_weight[3])
        outputs.R.P_Weight = lb2kg(constant.sizing.total_link_weight[5])

        outputs.V.Combined_Link_Weight = lb2kg(constant.V.combined_link_weight)

    else:
        outputs.F.U_Link_Weight = constant.sizing.link_weight[0] * 1
        outputs.F.L_Link_Weight = constant.sizing.link_weight[1] * 1
        outputs.F.P_Link_Weight = constant.sizing.link_weight[4] * 1
        outputs.F.U_RE_Weight = constant.sizing.RE_weight[0] * 1
        outputs.F.L_RE_Weight = constant.sizing.RE_weight[1] * 1
        outputs.F.P_RE_Weight = constant.sizing.RE_weight[4] * 1
        outputs.F.U_Weight = constant.sizing.total_link_weight[0] * 1
        outputs.F.L_Weight = constant.sizing.total_link_weight[1] * 1
        outputs.F.P_Weight = constant.sizing.total_link_weight[4] * 1

        outputs.R.U_Link_Weight = constant.sizing.link_weight[2] * 1
        outputs.R.L_Link_Weight = constant.sizing.link_weight[3] * 1
        outputs.R.P_Link_Weight = constant.sizing.link_weight[5] * 1
        outputs.R.U_RE_Weight = constant.sizing.RE_weight[2] * 1
        outputs.R.L_RE_Weight = constant.sizing.RE_weight[3] * 1
        outputs.R.P_RE_Weight = constant.sizing.RE_weight[5] * 1
        outputs.R.U_Weight = constant.sizing.total_link_weight[2] * 1
        outputs.R.L_Weight = constant.sizing.total_link_weight[3] * 1
        outputs.R.P_Weight = constant.sizing.total_link_weight[5] * 1

        outputs.V.Combined_Link_Weight = constant.V.combined_link_weight
