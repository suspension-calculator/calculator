# src/suspension/core/calculations/link_sizing.py


def run_link_sizing():
    # ------------------------------ Values In -------------------------------------
    from math import pi

    from suspension.io.variables import constant
    from suspension.io.IO_Conversion.link_sizing_IO import (
        input_processing_link_sizing,
        output_processing_link_sizing,
    )

    input_processing_link_sizing()

    # ------------------------------ For Loop Setup -------------------------------------
    link_OD = [
        constant.F.U_OD,
        constant.F.L_OD,
        constant.R.U_OD,
        constant.R.L_OD,
        1,
        1,
    ]  # Link diameter array
    if constant.F.panhard:
        link_OD[4] = constant.F.P_OD
    if constant.R.panhard:
        link_OD[5] = constant.R.P_OD

    if constant.F.U_solid:
        constant.F.U_wall = constant.F.U_OD / 2  # If solid link wall is 1/2 diameter
    if constant.F.L_solid:
        constant.F.L_wall = constant.F.L_OD / 2  # If solid link wall is 1/2 diameter
    if constant.R.U_solid:
        constant.R.U_wall = constant.R.U_OD / 2  # If solid link wall is 1/2 diameter
    if constant.R.L_solid:
        constant.R.L_wall = constant.R.L_OD / 2  # If solid link wall is 1/2 diameter
    if constant.F.P_solid:
        constant.F.P_wall = constant.F.P_OD / 2  # If solid link wall is 1/2 diameter
    if constant.R.P_solid:
        constant.R.P_wall = constant.R.P_OD / 2  # If solid link wall is 1/2 diameter

    link_wall = [
        constant.F.U_wall,
        constant.F.L_wall,
        constant.R.U_wall,
        constant.R.L_wall,
        0.5,
        0.5,
    ]  # Link wall thickness array
    if constant.F.panhard:
        link_wall[4] = constant.F.P_wall
    if constant.R.panhard:
        link_wall[5] = constant.R.P_wall

    link_rod_end = [
        constant.F.U_rod_end,
        constant.F.L_rod_end,
        constant.R.U_rod_end,
        constant.R.L_rod_end,
        "a",
        "a",
    ]  # Rod end name array
    if constant.F.panhard:
        link_rod_end[4] = constant.F.P_rod_end
    if constant.R.panhard:
        link_rod_end[5] = constant.R.P_rod_end

    link_length = [
        constant.F.U_length_3D,
        constant.F.L_length_3D,
        constant.R.U_length_3D,
        constant.R.L_length_3D,
        1,
        1,
    ]  # Link length array
    if constant.F.panhard:
        link_length[4] = constant.F.P_length_3D
    if constant.R.panhard:
        link_length[5] = constant.R.P_length_3D

    link_force = [
        constant.F.U_force,
        constant.F.L_force,
        constant.R.U_force,
        constant.R.L_force,
        1,
        1,
    ]  # Link force
    if constant.F.panhard:
        link_force[4] = constant.F.P_force
    if constant.R.panhard:
        link_force[5] = constant.R.P_force

    # ------------------------------ Material Properties import -------------------------------------
    yield_strength = [0] * 6  # Preallocate yield strength movement array
    modulus_elasticity = [0] * 6  # Preallocate modulus of elasticity array
    density = [0] * 6  # Preallocate density array

    Mat_index = [0] * 6
    Mat_index[0] = constant.materials.name.index(constant.F.U_material)
    Mat_index[1] = constant.materials.name.index(constant.F.L_material)
    Mat_index[2] = constant.materials.name.index(constant.R.U_material)
    Mat_index[3] = constant.materials.name.index(constant.R.L_material)
    Mat_index[4] = constant.materials.name.index(constant.F.P_material)
    Mat_index[5] = constant.materials.name.index(constant.R.P_material)

    for i in range(0, 6):
        yield_strength[i] = constant.materials.yield_strength[Mat_index[i]]
        modulus_elasticity[i] = constant.materials.modulus_elasticity[Mat_index[i]]
        density[i] = constant.materials.density[Mat_index[i]]

    # ------------------------------ Rod End Imports -------------------------------------
    rod_end_radial_load = [0] * 6  # Preallocate rod end radial_load movement array

    RE_index = [0] * 6
    RE_index[0] = constant.rod_ends.name.index(constant.F.U_rod_end)
    RE_index[1] = constant.rod_ends.name.index(constant.F.L_rod_end)
    RE_index[2] = constant.rod_ends.name.index(constant.R.U_rod_end)
    RE_index[3] = constant.rod_ends.name.index(constant.R.L_rod_end)
    RE_index[4] = constant.rod_ends.name.index(constant.F.P_rod_end)
    RE_index[5] = constant.rod_ends.name.index(constant.R.P_rod_end)

    for i in range(0, 6):
        rod_end_radial_load[i] = constant.rod_ends.radial_load[RE_index[i]]
        constant.sizing.RE_weight[i] = 2 * constant.rod_ends.weight[RE_index[i]]
        constant.sizing.RE_hole_diameter[i] = constant.rod_ends.hole_diameter[
            RE_index[i]
        ]
        constant.sizing.RE_thread_diameter[i] = constant.rod_ends.shank_diameter[
            RE_index[i]
        ]
        constant.sizing.RE_thread[i] = constant.rod_ends.thread[RE_index[i]]

    # ------------------------------ Math Preallocate and Setup -------------------------------------

    dent_resistance_constant = (53700**2) * (
        0.25**4
    )  # 1018 Steel, 0.25" thick, using:https://www.azom.com/article.aspx?ArticleID=1629, k divides out in FS calc

    # ------------------------------ Maths -------------------------------------
    for i in range(0, 6):
        inertia_moment = (
            pi / 64 * (link_OD[i] ** 4 - (link_OD[i] - 2 * link_wall[i]) ** 4)
        )
        cross_section_area = (
            pi * (link_OD[i] ** 2 - (link_OD[i] - 2 * link_wall[i]) ** 2) / 4
        )
        constant.sizing.link_weight[i] = (
            link_length[i] * cross_section_area * density[i]
        )
        constant.sizing.total_link_weight[i] = (
            constant.sizing.link_weight[i] + constant.sizing.RE_weight[i]
        )
        constant.sizing.FS_yield[i] = abs(
            yield_strength[i] * cross_section_area / link_force[i]
        )
        constant.sizing.FS_buckling[i] = abs(
            pi**2
            * modulus_elasticity[i]
            * inertia_moment
            / (link_length[i] ** 2)
            / link_force[i]
        )
        constant.sizing.FS_bending[i] = abs(
            yield_strength[i]
            * inertia_moment
            / (0.125 * link_OD[i] * link_length[i])
            / (0.5 * constant.V.mass)
        )
        constant.sizing.dent_resistance[i] = (
            (yield_strength[i] ** 2) * (link_wall[i] ** 4)
        ) / dent_resistance_constant
        constant.sizing.FS_RE[i] = abs(rod_end_radial_load[i] / link_force[i])

    constant.V.combined_link_weight = (
        2
        * (constant.sizing.total_link_weight[1] + constant.sizing.total_link_weight[3])
        + constant.sizing.total_link_weight[0] * constant.F.U_count
        + constant.sizing.total_link_weight[2] * constant.R.U_count
    )
    if constant.F.panhard:
        constant.V.combined_link_weight += constant.sizing.total_link_weight[4]
    if constant.R.panhard:
        constant.V.combined_link_weight += constant.sizing.total_link_weight[5]

    constant.F.spacing_warning = (
        0.5 * (constant.F.L_OD + constant.F.U_OD) < constant.F.min_distance
    )
    constant.R.spacing_warning = (
        0.5 * (constant.R.L_OD + constant.R.U_OD) < constant.R.min_distance
    )

    output_processing_link_sizing()
