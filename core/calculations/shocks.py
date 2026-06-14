# src/suspension/core/calculations/shocks.py

# IO Imports
from tool_io.variables import constant, travel, S, x, y, z
from tool_io.IO_Conversion.shocks_IO import (
    input_processing_shocks,
    output_processing_shocks,
)

# Core Imports
from core.functions.distance_2d import dis2D
from core.functions.distance_3d import dis3D
from core.functions.rotation import rotate
from core.functions.segment_seperation import SegSep
from core.functions.line_intersection import LineIntersect
from core.functions.link_travel import travel_solve
from core.functions.axle_point_movement import on_axle_movement
from core.functions.points_angle import point_angle
from core.functions.line_seperation import LineSeperation
from core.functions.pinion_rotation import pinion_angle_change

# Library Imports
from math import atan2, pi, sqrt, sin, cos
import numpy as np

def run_shocks():
    input_processing_shocks()

    # ------------------------------ Preallocation -------------------------------------
    class solver:
        point3 = np.zeros(3)
        link_angle = 0
        side_view_sqr = 0

        class F:
            U_ride_angle_rad = 0
            L_ride_angle_rad = 0
            period = 0
            stop_insert = 0
            slider_stop_IR = 0
            slider_shock_length = -1
            slider_travel = constant.F.slider_stop
            UA = np.zeros(3)
            LA = np.zeros(3)
            susp_mount = np.zeros(3)
            IC = np.zeros(3)
            pinion_rad = 0
            hub = np.zeros(3)
            wheel_contact = 0
            drive_x = 0
            brake_x = 0
            drive_intersect_z = 0
            brake_intersect_z = 0
            inboard_factor = 0
            distance_factor = 0
            shock_angle_factor = 0
            shock_wheel_factor = 0
            IR = 0
            main_spring_list = []
            tender_spring_list = []
            closest_match_period = 0
            used_period = 0

            class shock1:
                delta_y = 0

            class shock2:
                delta_y = 0

        class R:
            U_ride_angle_rad = 0
            L_ride_angle_rad = 0
            period = 0
            stop_insert = 0
            slider_stop_IR = 0
            slider_shock_length = -1
            slider_travel = constant.R.slider_stop
            UA = np.zeros(3)
            LA = np.zeros(3)
            susp_mount = np.zeros(3)
            IC = np.zeros(3)
            pinion_rad = 0
            hub = np.zeros(3)
            wheel_contact = 0
            drive_x = 0
            brake_x = 0
            drive_intersect_z = 0
            brake_intersect_z = 0
            inboard_factor = 0
            distance_factor = 0
            shock_angle_factor = 0
            shock_wheel_factor = 0
            IR = 0
            main_spring_list = []
            tender_spring_list = []
            closest_match_period = 0
            used_period = 0

            class shock1:
                delta_y = 0

            class shock2:
                delta_y = 0

    travel.F.shock1.susp_mount = [
        [0] * 3 for _ in range(S.sample_points * 2 + 1)
    ]  # Preallocate front shock 1 travel matrix
    travel.F.shock2.susp_mount = [
        [0] * 3 for _ in range(S.sample_points * 2 + 1)
    ]  # Preallocate front shock 2 travel matrix
    travel.R.shock1.susp_mount = [
        [0] * 3 for _ in range(S.sample_points * 2 + 1)
    ]  # Preallocate rear shock 1 travel matrix
    travel.R.shock2.susp_mount = [
        [0] * 3 for _ in range(S.sample_points * 2 + 1)
    ]  # Preallocate rear shock 2 travel matrix

    travel.F.shock1.factor.inboard = np.zeros(
        2 * S.sample_points + 1
    )  # Preallocate front shock 1 inboard factor matrix
    travel.F.shock2.factor.inboard = np.zeros(
        2 * S.sample_points + 1
    )  # Preallocate front shock 2 inboard factor matrix
    travel.R.shock1.factor.inboard = np.zeros(
        2 * S.sample_points + 1
    )  # Preallocate rear shock 1 inboard factor matrix
    travel.R.shock2.factor.inboard = np.zeros(
        2 * S.sample_points + 1
    )  # Preallocate rear shock 2 inboard factor matrix

    travel.F.shock1.factor.distance = np.zeros(
        2 * S.sample_points + 1
    )  # Preallocate front shock 1 distance factor matrix
    travel.F.shock2.factor.distance = np.zeros(
        2 * S.sample_points + 1
    )  # Preallocate front shock 2 distance factor matrix
    travel.R.shock1.factor.distance = np.zeros(
        2 * S.sample_points + 1
    )  # Preallocate rear shock 1 distance factor matrix
    travel.R.shock2.factor.distance = np.zeros(
        2 * S.sample_points + 1
    )  # Preallocate rear shock 2 distance factor matrix

    travel.F.shock1.factor.shock_angle = np.zeros(
        2 * S.sample_points + 1
    )  # Preallocate front shock 1 shock angle factor matrix
    travel.F.shock2.factor.shock_angle = np.zeros(
        2 * S.sample_points + 1
    )  # Preallocate front shock 2 shock angle factor matrix
    travel.R.shock1.factor.shock_angle = np.zeros(
        2 * S.sample_points + 1
    )  # Preallocate rear shock 1 shock angle factor matrix
    travel.R.shock2.factor.shock_angle = np.zeros(
        2 * S.sample_points + 1
    )  # Preallocate rear shock 2 shock angle factor matrix

    travel.F.shock1.factor.wheel = np.zeros(
        2 * S.sample_points + 1
    )  # Preallocate front shock wheel factor matrix
    travel.F.shock2.factor.wheel = np.zeros(
        2 * S.sample_points + 1
    )  # Preallocate front shock wheel factor matrix
    travel.R.shock1.factor.wheel = np.zeros(
        2 * S.sample_points + 1
    )  # Preallocate rear shock wheel factor matrix
    travel.R.shock2.factor.wheel = np.zeros(
        2 * S.sample_points + 1
    )  # Preallocate front shock wheel factor matrix

    travel.F.shock1.IR = np.zeros(
        2 * S.sample_points + 1
    )  # Preallocate front shock 1 installation ratio matrix
    travel.F.shock2.IR = np.zeros(
        2 * S.sample_points + 1
    )  # Preallocate front shock 2 installation ratio matrix
    travel.R.shock1.IR = np.zeros(
        2 * S.sample_points + 1
    )  # Preallocate rear shock 1 installation ratio matrix
    travel.R.shock2.IR = np.zeros(
        2 * S.sample_points + 1
    )  # Preallocate rear shock 2 installation ratio matrix

    travel.F.spring_force_closest = np.zeros(2 * S.sample_points + 1 + 2)
    travel.F.spring_force_chosen = np.zeros(2 * S.sample_points + 1 + 2)
    travel.R.spring_force_closest = np.zeros(2 * S.sample_points + 1 + 2)
    travel.R.spring_force_chosen = np.zeros(2 * S.sample_points + 1 + 2)

    travel.F.wheel_force_closest = np.zeros(2 * S.sample_points + 1 + 2)
    travel.F.wheel_rate_closest = np.zeros(2 * S.sample_points + 1 + 2)
    travel.F.wheel_force_chosen = np.zeros(2 * S.sample_points + 1 + 2)
    travel.F.wheel_rate_chosen = np.zeros(2 * S.sample_points + 1 + 2)
    travel.R.wheel_force_closest = np.zeros(2 * S.sample_points + 1 + 2)
    travel.R.wheel_rate_closest = np.zeros(2 * S.sample_points + 1 + 2)
    travel.R.wheel_force_chosen = np.zeros(2 * S.sample_points + 1 + 2)
    travel.R.wheel_rate_chosen = np.zeros(2 * S.sample_points + 1 + 2)

    travel.F.shock1.length = np.zeros(2 * S.sample_points + 1)
    travel.F.shock2.length = np.zeros(2 * S.sample_points + 1)
    travel.R.shock1.length = np.zeros(2 * S.sample_points + 1)
    travel.R.shock2.length = np.zeros(2 * S.sample_points + 1)

    # ------------------------------ Maths -------------------------------------

    if constant.F.shock1.location == 1 or (
        constant.F.shock2.exists and constant.F.shock2.location == 1
    ):
        solver.F.U_ride_angle_rad = atan2(
            constant.F.UA[z] - constant.F.UF[z], [constant.F.UA[x] - constant.F.UF[x]]
        )
    elif constant.F.shock1.location == 2 or (
        constant.F.shock2.exists and constant.F.shock2.location == 2
    ):
        solver.F.L_ride_angle_rad = atan2(
            constant.F.LA[z] - constant.F.LF[z], [constant.F.LA[x] - constant.F.LF[x]]
        )

    if constant.R.shock1.location == 1 or (
        constant.R.shock2.exists and constant.R.shock2.location == 1
    ):
        solver.R.U_ride_angle_rad = atan2(
            constant.R.UA[z] - constant.R.UF[z], [constant.R.UA[x] - constant.R.UF[x]]
        )
    elif constant.R.shock1.location == 2 or (
        constant.R.shock2.exists and constant.R.shock2.location == 2
    ):
        solver.R.L_ride_angle_rad = atan2(
            constant.R.LA[z] - constant.R.LF[z], [constant.R.LA[x] - constant.R.LF[x]]
        )

    solver.F.shock1.delta_y = (
        constant.F.shock1.chassis_mount[y] - constant.F.shock1.susp_mount[y]
    )
    if constant.F.shock2.exists:
        solver.F.shock2.delta_y = (
            constant.F.shock2.chassis_mount[y] - constant.F.shock2.susp_mount[y]
        )

    solver.R.shock1.delta_y = (
        constant.R.shock1.chassis_mount[y] - constant.R.shock1.susp_mount[y]
    )
    if constant.R.shock2.exists:
        solver.R.shock2.delta_y = (
            constant.R.shock2.chassis_mount[y] - constant.R.shock2.susp_mount[y]
        )

    if constant.F.shock1.location == 1:
        constant.F.shock1.link_factor = (
            dis2D(
                constant.F.UF[x],
                constant.F.UF[z],
                constant.F.shock1.susp_mount[x],
                constant.F.shock1.susp_mount[z],
            )
            / constant.F.U_length_2D
        )
    elif constant.F.shock1.location == 2:
        constant.F.shock1.link_factor = (
            dis2D(
                constant.F.LF[x],
                constant.F.LF[z],
                constant.F.shock1.susp_mount[x],
                constant.F.shock1.susp_mount[z],
            )
            / constant.F.L_length_2D
        )
    else:
        constant.F.shock1.link_factor = 1

    if constant.F.shock2.exists and constant.F.shock2.location == 1:
        constant.F.shock2.link_factor = (
            dis2D(
                constant.F.UF[x],
                constant.F.UF[z],
                constant.F.shock2.susp_mount[x],
                constant.F.shock2.susp_mount[z],
            )
            / constant.F.U_length_2D
        )
    elif constant.F.shock2.exists and constant.F.shock2.location == 2:
        constant.F.shock2.link_factor = (
            dis2D(
                constant.F.LF[x],
                constant.F.LF[z],
                constant.F.shock2.susp_mount[x],
                constant.F.shock2.susp_mount[z],
            )
            / constant.F.L_length_2D
        )
    else:
        constant.F.shock2.link_factor = 1

    if constant.R.shock1.location == 1:
        constant.R.shock1.link_factor = (
            dis2D(
                constant.R.UF[x],
                constant.R.UF[z],
                constant.R.shock1.susp_mount[x],
                constant.R.shock1.susp_mount[z],
            )
            / constant.R.U_length_2D
        )
    elif constant.R.shock1.location == 2:
        constant.R.shock1.link_factor = (
            dis2D(
                constant.R.LF[x],
                constant.R.LF[z],
                constant.R.shock1.susp_mount[x],
                constant.R.shock1.susp_mount[z],
            )
            / constant.R.L_length_2D
        )
    else:
        constant.R.shock1.link_factor = 1

    if constant.R.shock2.exists and constant.R.shock2.location == 1:
        constant.R.shock2.link_factor = (
            dis2D(
                constant.R.UF[x],
                constant.R.UF[z],
                constant.R.shock2.susp_mount[x],
                constant.R.shock2.susp_mount[z],
            )
            / constant.R.U_length_2D
        )
    elif constant.R.shock2.exists and constant.R.shock2.location == 2:
        constant.R.shock2.link_factor = (
            dis2D(
                constant.R.LF[x],
                constant.R.LF[z],
                constant.R.shock2.susp_mount[x],
                constant.R.shock2.susp_mount[z],
            )
            / constant.R.L_length_2D
        )
    else:
        constant.R.shock2.link_factor = 1

    for i in range(0, 2 * S.sample_points + 1):
        if constant.F.shock1.location == 0:  # Front shock 1 axle mounted
            travel.F.shock1.susp_mount[i][x], travel.F.shock1.susp_mount[i][z] = (
                on_axle_movement(
                    constant.F.shock1.susp_mount[x],
                    constant.F.shock1.susp_mount[z],
                    constant.F.LA[x],
                    constant.F.LA[z],
                    travel.F.LA[i][x],
                    travel.F.LA[i][z],
                    travel.F.pinion_rad[i],
                )
            )
            solver.point3 = travel.F.IC[i]
        elif constant.F.shock1.location == 1:  # Front shock 1 uppper link mounted
            solver.link_angle = atan2(
                travel.F.UA[i][z] - constant.F.UF[z],
                [travel.F.UA[i][x] - constant.F.UF[x]],
            )
            travel.F.shock1.susp_mount[i][x], travel.F.shock1.susp_mount[i][z] = rotate(
                constant.F.UF[x],
                constant.F.UF[z],
                constant.F.shock1.susp_mount[x],
                constant.F.shock1.susp_mount[z],
                solver.link_angle - solver.F.U_ride_angle_rad,
            )
            solver.point3 = constant.F.UF
        elif constant.F.shock1.location == 2:  # Front shock 1 lower link mounted
            solver.link_angle = atan2(
                travel.F.LA[i][z] - constant.F.LF[z],
                [travel.F.LA[i][x] - constant.F.LF[x]],
            )
            travel.F.shock1.susp_mount[i][x], travel.F.shock1.susp_mount[i][z] = rotate(
                constant.F.LF[x],
                constant.F.LF[z],
                constant.F.shock1.susp_mount[x],
                constant.F.shock1.susp_mount[z],
                solver.link_angle - solver.F.L_ride_angle_rad,
            )
            solver.point3 = constant.F.LF

        solver.side_view_sqr = (
            constant.F.shock1.chassis_mount[x] - travel.F.shock1.susp_mount[i][x]
        ) ** 2 + (
            constant.F.shock1.chassis_mount[z] - travel.F.shock1.susp_mount[i][z]
        ) ** 2
        travel.F.shock1.factor.inboard[i] = sqrt(solver.side_view_sqr) / sqrt(
            solver.side_view_sqr + solver.F.shock1.delta_y**2
        )
        travel.F.shock1.factor.distance[i] = dis2D(
            travel.F.IC[i][x],
            travel.F.IC[i][z],
            travel.F.shock1.susp_mount[i][x],
            travel.F.shock1.susp_mount[i][z],
        ) / dis2D(
            travel.F.IC[i][x], travel.F.IC[i][z], travel.F.hub[i][x], travel.F.hub[i][z]
        )
        travel.F.shock1.factor.shock_angle[i] = sin(
            point_angle(
                constant.F.shock1.chassis_mount[x],
                constant.F.shock1.chassis_mount[z],
                travel.F.shock1.susp_mount[i][x],
                travel.F.shock1.susp_mount[i][z],
                solver.point3[x],
                solver.point3[z],
            )
        )
        travel.F.shock1.factor.wheel[i] = cos(
            point_angle(
                travel.F.hub[i][x],
                travel.F.hub[i][z],
                travel.F.IC[i][x],
                travel.F.IC[i][z],
                travel.F.hub[i][x],
                travel.F.IC[i][z],
            )
        )

        travel.F.shock1.IR[i] = (
            constant.F.shock1.link_factor
            * travel.F.shock1.factor.inboard[i]
            * travel.F.shock1.factor.distance[i]
            * travel.F.shock1.factor.shock_angle[i]
            * travel.F.shock1.factor.wheel[i]
        )

        if constant.F.shock2.exists:
            if constant.F.shock2.location == 0:  # Front shock 2 axle mounted
                travel.F.shock2.susp_mount[i][x], travel.F.shock2.susp_mount[i][z] = (
                    on_axle_movement(
                        constant.F.shock2.susp_mount[x],
                        constant.F.shock2.susp_mount[z],
                        constant.F.LA[x],
                        constant.F.LA[z],
                        travel.F.LA[i][x],
                        travel.F.LA[i][z],
                        travel.F.pinion_rad[i],
                    )
                )
                solver.point3 = travel.F.IC[i]
            elif constant.F.shock2.location == 1:  # Front shock 2 uppper link mounted
                solver.link_angle = atan2(
                    travel.F.UA[i][z] - constant.F.UF[z],
                    [travel.F.UA[i][x] - constant.F.UF[x]],
                )
                travel.F.shock2.susp_mount[i][x], travel.F.shock2.susp_mount[i][z] = (
                    rotate(
                        constant.F.UF[x],
                        constant.F.UF[z],
                        constant.F.shock2.susp_mount[x],
                        constant.F.shock2.susp_mount[z],
                        solver.link_angle - solver.F.U_ride_angle_rad,
                    )
                )
                solver.point3 = constant.F.UF
            elif constant.F.shock2.location == 2:  # Front shock 2 lower link mounted
                solver.link_angle = atan2(
                    travel.F.LA[i][z] - constant.F.LF[z],
                    [travel.F.LA[i][x] - constant.F.LF[x]],
                )
                travel.F.shock2.susp_mount[i][x], travel.F.shock2.susp_mount[i][z] = (
                    rotate(
                        constant.F.LF[x],
                        constant.F.LF[z],
                        constant.F.shock2.susp_mount[x],
                        constant.F.shock2.susp_mount[z],
                        solver.link_angle - solver.F.L_ride_angle_rad,
                    )
                )
                solver.point3 = constant.F.LF
            shock_sep = SegSep(
                constant.F.shock1.chassis_mount[x],
                constant.F.shock1.chassis_mount[y],
                constant.F.shock1.chassis_mount[z],
                travel.F.shock1.susp_mount[i][x],
                travel.F.shock1.susp_mount[i][y],
                travel.F.shock1.susp_mount[i][z],
                constant.F.shock2.chassis_mount[x],
                constant.F.shock2.chassis_mount[y],
                constant.F.shock2.chassis_mount[z],
                travel.F.shock2.susp_mount[i][x],
                travel.F.shock2.susp_mount[i][y],
                travel.F.shock2.susp_mount[i][z],
            )
            if shock_sep < constant.F.shock_sep:
                constant.F.shock_sep = shock_sep

            solver.side_view_sqr = (
                constant.F.shock2.chassis_mount[x] - travel.F.shock2.susp_mount[i][x]
            ) ** 2 + (
                constant.F.shock2.chassis_mount[z] - travel.F.shock2.susp_mount[i][z]
            ) ** 2
            travel.F.shock2.factor.inboard[i] = sqrt(solver.side_view_sqr) / sqrt(
                solver.side_view_sqr + solver.F.shock2.delta_y**2
            )
            travel.F.shock2.factor.distance[i] = dis2D(
                travel.F.IC[i][x],
                travel.F.IC[i][z],
                travel.F.shock2.susp_mount[i][x],
                travel.F.shock2.susp_mount[i][z],
            ) / dis2D(
                travel.F.IC[i][x],
                travel.F.IC[i][z],
                travel.F.hub[i][x],
                travel.F.hub[i][z],
            )
            travel.F.shock2.factor.shock_angle[i] = sin(
                point_angle(
                    constant.F.shock2.chassis_mount[x],
                    constant.F.shock2.chassis_mount[z],
                    travel.F.shock2.susp_mount[i][x],
                    travel.F.shock2.susp_mount[i][z],
                    solver.point3[x],
                    solver.point3[z],
                )
            )
            travel.F.shock2.factor.wheel[i] = travel.F.shock1.factor.wheel[i]

            travel.F.shock2.IR[i] = (
                constant.F.shock2.link_factor
                * travel.F.shock2.factor.inboard[i]
                * travel.F.shock2.factor.distance[i]
                * travel.F.shock2.factor.shock_angle[i]
                * travel.F.shock2.factor.wheel[i]
            )

        if constant.R.shock1.location == 0:  # Rear shock 1 axle mounted
            travel.R.shock1.susp_mount[i][x], travel.R.shock1.susp_mount[i][z] = (
                on_axle_movement(
                    constant.R.shock1.susp_mount[x],
                    constant.R.shock1.susp_mount[z],
                    constant.R.LA[x],
                    constant.R.LA[z],
                    travel.R.LA[i][x],
                    travel.R.LA[i][z],
                    travel.R.pinion_rad[i],
                )
            )
            solver.point3 = travel.R.IC[i]
        elif constant.F.shock1.location == 1:  # Rear shock 1 uppper link mounted
            solver.link_angle = atan2(
                travel.R.UA[i][z] - constant.R.UF[z],
                [travel.R.UA[i][x] - constant.R.UF[x]],
            )
            travel.R.shock1.susp_mount[i][x], travel.R.shock1.susp_mount[i][z] = rotate(
                constant.R.UF[x],
                constant.R.UF[z],
                constant.R.shock1.susp_mount[x],
                constant.R.shock1.susp_mount[z],
                solver.link_angle - solver.R.U_ride_angle_rad,
            )
            solver.point3 = constant.R.UF
        elif constant.F.shock1.location == 2:  # Rear shock 1 lower link mounted
            solver.link_angle = atan2(
                travel.R.LA[i][z] - constant.R.LF[z],
                [travel.R.LA[i][x] - constant.R.LF[x]],
            )
            travel.R.shock1.susp_mount[i][x], travel.R.shock1.susp_mount[i][z] = rotate(
                constant.R.LF[x],
                constant.R.LF[z],
                constant.R.shock1.susp_mount[x],
                constant.R.shock1.susp_mount[z],
                solver.link_angle - solver.R.L_ride_angle_rad,
            )
            solver.point3 = constant.R.LF

        solver.side_view_sqr = (
            constant.R.shock1.chassis_mount[x] - travel.R.shock1.susp_mount[i][x]
        ) ** 2 + (
            constant.R.shock1.chassis_mount[z] - travel.R.shock1.susp_mount[i][z]
        ) ** 2
        travel.R.shock1.factor.inboard[i] = sqrt(solver.side_view_sqr) / sqrt(
            solver.side_view_sqr + solver.R.shock1.delta_y**2
        )
        travel.R.shock1.factor.distance[i] = dis2D(
            travel.R.IC[i][x],
            travel.R.IC[i][z],
            travel.R.shock1.susp_mount[i][x],
            travel.R.shock1.susp_mount[i][z],
        ) / dis2D(
            travel.R.IC[i][x], travel.R.IC[i][z], travel.R.hub[i][x], travel.R.hub[i][z]
        )
        travel.R.shock1.factor.shock_angle[i] = sin(
            point_angle(
                constant.R.shock1.chassis_mount[x],
                constant.R.shock1.chassis_mount[z],
                travel.R.shock1.susp_mount[i][x],
                travel.R.shock1.susp_mount[i][z],
                solver.point3[x],
                solver.point3[z],
            )
        )
        travel.R.shock1.factor.wheel[i] = cos(
            point_angle(
                travel.R.hub[i][x],
                travel.R.hub[i][z],
                travel.R.IC[i][x],
                travel.R.IC[i][z],
                travel.R.hub[i][x],
                travel.R.IC[i][z],
            )
        )

        travel.R.shock1.IR[i] = (
            constant.R.shock1.link_factor
            * travel.R.shock1.factor.inboard[i]
            * travel.R.shock1.factor.distance[i]
            * travel.R.shock1.factor.shock_angle[i]
            * travel.R.shock1.factor.wheel[i]
        )

        if constant.R.shock2.exists:
            if constant.R.shock2.location == 0:  # Rear shock 2 axle mounted
                travel.R.shock2.susp_mount[i][x], travel.R.shock2.susp_mount[i][z] = (
                    on_axle_movement(
                        constant.R.shock2.susp_mount[x],
                        constant.R.shock2.susp_mount[z],
                        constant.R.LA[x],
                        constant.R.LA[z],
                        travel.R.LA[i][x],
                        travel.R.LA[i][z],
                        travel.R.pinion_rad[i],
                    )
                )
                solver.point3 = travel.R.IC[i]
            elif constant.R.shock2.location == 1:  # Rear shock 2 uppper link mounted
                solver.link_angle = atan2(
                    travel.R.UA[i][z] - constant.R.UF[z],
                    [travel.R.UA[i][x] - constant.R.UF[x]],
                )
                constant.R.shock2.susp_mount[i][x], travel.R.shock2.susp_mount[i][z] = (
                    rotate(
                        constant.R.UF[x],
                        constant.R.UF[z],
                        constant.R.shock2.susp_mount[x],
                        constant.R.shock2.susp_mount[z],
                        solver.link_angle - solver.R.U_ride_angle_rad,
                    )
                )
                solver.point3 = constant.R.UF
            elif constant.R.shock2.location == 2:  # Rear shock 2 lower link mounted
                solver.link_angle = atan2(
                    travel.R.LA[i][z] - constant.R.LF[z],
                    [travel.R.LA[i][x] - constant.R.LF[x]],
                )
                travel.R.shock2.susp_mount[i][x], travel.R.shock2.susp_mount[i][z] = (
                    rotate(
                        constant.R.LF[x],
                        constant.R.LF[z],
                        constant.R.shock2.susp_mount[x],
                        constant.R.shock2.susp_mount[z],
                        solver.link_angle - solver.R.L_ride_angle_rad,
                    )
                )
                solver.point3 = constant.R.LF

            shock_sep = SegSep(
                constant.R.shock1.chassis_mount[x],
                constant.R.shock1.chassis_mount[y],
                constant.R.shock1.chassis_mount[z],
                travel.R.shock1.susp_mount[i][x],
                travel.R.shock1.susp_mount[i][y],
                travel.R.shock1.susp_mount[i][z],
                constant.R.shock2.chassis_mount[x],
                constant.R.shock2.chassis_mount[y],
                constant.R.shock2.chassis_mount[z],
                travel.R.shock2.susp_mount[i][x],
                travel.R.shock2.susp_mount[i][y],
                travel.R.shock2.susp_mount[i][z],
            )
            if shock_sep < constant.R.shock_sep:
                constant.R.shock_sep = shock_sep

            solver.side_view_sqr = (
                constant.R.shock2.chassis_mount[x] - travel.R.shock2.susp_mount[i][x]
            ) ** 2 + (
                constant.R.shock2.chassis_mount[z] - travel.R.shock2.susp_mount[i][z]
            ) ** 2
            travel.R.shock2.factor.inboard[i] = sqrt(solver.side_view_sqr) / sqrt(
                solver.side_view_sqr + solver.R.shock2.delta_y**2
            )
            travel.R.shock2.factor.distance[i] = dis2D(
                travel.R.IC[i][x],
                travel.R.IC[i][z],
                travel.R.shock2.susp_mount[i][x],
                travel.R.shock2.susp_mount[i][z],
            ) / dis2D(
                travel.R.IC[i][x],
                travel.R.IC[i][z],
                travel.R.hub[i][x],
                travel.R.hub[i][z],
            )
            travel.R.shock2.factor.shock_angle[i] = sin(
                point_angle(
                    constant.R.shock2.chassis_mount[x],
                    constant.R.shock2.chassis_mount[z],
                    travel.R.shock2.susp_mount[i][x],
                    travel.R.shock2.susp_mount[i][z],
                    solver.point3[x],
                    solver.point3[z],
                )
            )
            travel.R.shock2.factor.wheel[i] = travel.R.shock1.factor.wheel[i]

            travel.R.shock2.IR[i] = (
                constant.R.shock2.link_factor
                * travel.R.shock2.factor.inboard[i]
                * travel.R.shock2.factor.distance[i]
                * travel.R.shock2.factor.shock_angle[i]
                * travel.R.shock2.factor.wheel[i]
            )

        travel.F.shock1.length[i] = dis3D(
            travel.F.shock1.susp_mount[i][x],
            travel.F.shock1.susp_mount[i][y],
            travel.F.shock1.susp_mount[i][z],
            constant.F.shock1.chassis_mount[x],
            constant.F.shock1.chassis_mount[y],
            constant.F.shock1.chassis_mount[z],
        )
        travel.R.shock1.length[i] = dis3D(
            travel.R.shock1.susp_mount[i][x],
            travel.R.shock1.susp_mount[i][y],
            travel.R.shock1.susp_mount[i][z],
            constant.R.shock1.chassis_mount[x],
            constant.R.shock1.chassis_mount[y],
            constant.R.shock1.chassis_mount[z],
        )
        travel.F.shock2.length[i] = dis3D(
            travel.F.shock2.susp_mount[i][x],
            travel.F.shock2.susp_mount[i][y],
            travel.F.shock2.susp_mount[i][z],
            constant.F.shock2.chassis_mount[x],
            constant.F.shock2.chassis_mount[y],
            constant.F.shock2.chassis_mount[z],
        )
        travel.R.shock2.length[i] = dis3D(
            travel.R.shock2.susp_mount[i][x],
            travel.R.shock2.susp_mount[i][y],
            travel.R.shock2.susp_mount[i][z],
            constant.R.shock2.chassis_mount[x],
            constant.R.shock2.chassis_mount[y],
            constant.R.shock2.chassis_mount[z],
        )

    # -------------------------  Slider Stop math -----------------------------------------

    while (
        travel.F.shock1.length[S.sample_points]
        + constant.F.slider_stop
        - solver.F.slider_shock_length
        > 0.0001
    ):
        solver.F.UA[x], solver.F.UA[z], solver.F.LA[x], solver.F.LA[z] = travel_solve(
            solver.F.slider_travel,
            constant.F.UA[x],
            constant.F.UA[z],
            constant.F.UF[x],
            constant.F.UF[z],
            constant.F.LA[x],
            constant.F.LA[z],
            constant.F.LF[x],
            constant.F.LF[z],
            constant.F.U_length_2D,
            constant.F.L_length_2D,
            constant.F.A_sep_2D,
            constant.F.F_sep_2D,
        )  # Calculate front arm arcs
        solver.F.pinion_rad = pinion_angle_change(
            constant.F.UA[x],
            constant.F.UA[z],
            solver.F.UA[x],
            solver.F.UA[z],
            constant.F.LA[x],
            constant.F.LA[z],
            solver.F.LA[x],
            solver.F.LA[z],
        )  # Calculate front pinion angle change

        if constant.F.shock1.location == 0:  # Front shock 1 axle mounted
            solver.F.susp_mount[x], solver.F.susp_mount[z] = on_axle_movement(
                constant.F.shock1.susp_mount[x],
                constant.F.shock1.susp_mount[z],
                constant.F.LA[x],
                constant.F.LA[z],
                solver.F.LA[x],
                solver.F.LA[z],
                solver.F.pinion_rad,
            )
            solver.point3 = solver.F.IC
        elif constant.F.shock1.location == 1:  # Front shock 1 uppper link mounted
            solver.link_angle = atan2(
                solver.F.UA[z] - constant.F.UF[z], [solver.F.UA[x] - constant.F.UF[x]]
            )
            solver.F.susp_mount[x], solver.F.susp_mount[z] = rotate(
                constant.F.UF[x],
                constant.F.UF[z],
                constant.F.shock1.susp_mount[x],
                constant.F.shock1.susp_mount[z],
                solver.link_angle - solver.F.U_ride_angle_rad,
            )
            solver.point3 = constant.F.UF
        elif constant.F.shock1.location == 2:  # Front shock 1 lower link mounted
            solver.link_angle = atan2(
                solver.F.LA[z] - constant.F.LF[z], [solver.F.LA[x] - constant.F.LF[x]]
            )
            solver.F.susp_mount[x], solver.F.susp_mount[z] = rotate(
                constant.F.LF[x],
                constant.F.LF[z],
                constant.F.shock1.susp_mount[x],
                constant.F.shock1.susp_mount[z],
                solver.link_angle - solver.F.L_ride_angle_rad,
            )
            solver.point3 = constant.F.LF

        solver.F.slider_shock_length = dis3D(
            solver.F.susp_mount[x],
            solver.F.susp_mount[y],
            solver.F.susp_mount[z],
            constant.F.shock1.chassis_mount[x],
            constant.F.shock1.chassis_mount[y],
            constant.F.shock1.chassis_mount[z],
        )
        solver.F.slider_travel = (
            solver.F.slider_travel
            + travel.F.shock1.length[S.sample_points]
            + constant.F.slider_stop
            - solver.F.slider_shock_length
        )

    solver.F.hub[x], solver.F.hub[z] = on_axle_movement(
        constant.F.hub[x],
        constant.F.hub[z],
        constant.F.LA[x],
        constant.F.LA[z],
        solver.F.LA[x],
        solver.F.LA[z],
        solver.F.pinion_rad,
    )  # Calculate front hub center movement
    if S.simulate_tire_loading:  # If tire loading is being simulated
        solver.F.wheel_contact = solver.F.hub[z] - (
            constant.F.tire_diameter * 0.5
            - constant.F.tire_rate * (solver.F.slider_travel - constant.F.droop)
        )  # Calculate front contanct point
    else:
        solver.F.wheel_contact = (
            solver.F.hub[z] - constant.F.tire_radius
        )  # Calculate front contanct point

    if (constant.F.LF[z] - solver.F.LA[z]) / (constant.F.LF[x] - solver.F.LA[x]) == (
        constant.F.UF[z] - solver.F.UA[z]
    ) / (
        constant.F.UF[x] - solver.F.UA[x]
    ):  # If slope of the front lower links is the same as the slope of the front upper links
        solver.F.IC[x] = solver.F.hub[x] + (
            constant.F.LF[x] - solver.F.LA[x]
        )  # Define point on wheel contact to infinite IC line
        solver.F.IC[z] = solver.F.wheel_contact + (
            constant.F.LF[z] - solver.F.LA[z]
        )  # Define point on wheel contact to infinite IC line
    else:
        solver.F.IC[x], solver.F.IC[z] = LineIntersect(
            constant.F.LF[x],
            constant.F.LF[z],
            solver.F.LA[x],
            solver.F.LA[z],
            constant.F.UF[x],
            constant.F.UF[z],
            solver.F.UA[x],
            solver.F.UA[z],
        )  # Find intersection of upper and lower links in side view

    solver.side_view_sqr = (
        constant.F.shock1.chassis_mount[x] - solver.F.susp_mount[x]
    ) ** 2 + (constant.F.shock1.chassis_mount[z] - solver.F.susp_mount[z]) ** 2
    solver.F.inboard_factor = sqrt(solver.side_view_sqr) / sqrt(
        solver.side_view_sqr + solver.F.shock1.delta_y**2
    )
    solver.F.distance_factor = dis2D(
        solver.F.IC[x], solver.F.IC[z], solver.F.susp_mount[x], solver.F.susp_mount[z]
    ) / dis2D(solver.F.IC[x], solver.F.IC[z], solver.F.hub[x], solver.F.hub[z])
    solver.F.shock_angle_factor = sin(
        point_angle(
            constant.F.shock1.chassis_mount[x],
            constant.F.shock1.chassis_mount[z],
            solver.F.susp_mount[x],
            solver.F.susp_mount[z],
            solver.point3[x],
            solver.point3[z],
        )
    )
    solver.F.shock_wheel_factor = cos(
        point_angle(
            solver.F.hub[x],
            solver.F.hub[z],
            solver.F.IC[x],
            solver.F.IC[z],
            solver.F.hub[x],
            solver.F.IC[z],
        )
    )
    solver.F.IR = (
        constant.F.shock1.link_factor
        * solver.F.inboard_factor
        * solver.F.distance_factor
        * solver.F.shock_angle_factor
        * solver.F.shock_wheel_factor
    )

    while (
        travel.R.shock1.length[S.sample_points]
        + constant.R.slider_stop
        - solver.R.slider_shock_length
        > 0.0001
    ):
        solver.R.UA[x], solver.R.UA[z], solver.R.LA[x], solver.R.LA[z] = travel_solve(
            solver.R.slider_travel,
            constant.R.UA[x],
            constant.R.UA[z],
            constant.R.UF[x],
            constant.R.UF[z],
            constant.R.LA[x],
            constant.R.LA[z],
            constant.R.LF[x],
            constant.R.LF[z],
            constant.R.U_length_2D,
            constant.R.L_length_2D,
            constant.R.A_sep_2D,
            constant.R.F_sep_2D,
        )  # Calculate front arm arcs
        solver.R.pinion_rad = pinion_angle_change(
            constant.R.UA[x],
            constant.R.UA[z],
            solver.R.UA[x],
            solver.R.UA[z],
            constant.R.LA[x],
            constant.R.LA[z],
            solver.R.LA[x],
            solver.R.LA[z],
        )  # Calculate front pinion angle change

        if constant.R.shock1.location == 0:  # Front shock 1 axle mounted
            solver.R.susp_mount[x], solver.R.susp_mount[z] = on_axle_movement(
                constant.R.shock1.susp_mount[x],
                constant.R.shock1.susp_mount[z],
                constant.R.LA[x],
                constant.R.LA[z],
                solver.R.LA[x],
                solver.R.LA[z],
                solver.R.pinion_rad,
            )
            solver.point3 = solver.R.IC
        elif constant.R.shock1.location == 1:  # Front shock 1 uppper link mounted
            solver.link_angle = atan2(
                solver.R.UA[z] - constant.R.UF[z], [solver.R.UA[x] - constant.R.UF[x]]
            )
            solver.R.susp_mount[x], solver.R.susp_mount[z] = rotate(
                constant.R.UF[x],
                constant.R.UF[z],
                constant.R.shock1.susp_mount[x],
                constant.R.shock1.susp_mount[z],
                solver.link_angle - solver.R.U_ride_angle_rad,
            )
            solver.point3 = constant.R.UF
        elif constant.R.shock1.location == 2:  # Front shock 1 lower link mounted
            solver.link_angle = atan2(
                solver.R.LA[z] - constant.R.LF[z], [solver.R.LA[x] - constant.R.LF[x]]
            )
            solver.R.susp_mount[x], solver.R.susp_mount[z] = rotate(
                constant.R.LF[x],
                constant.R.LF[z],
                constant.R.shock1.susp_mount[x],
                constant.R.shock1.susp_mount[z],
                solver.link_angle - solver.R.L_ride_angle_rad,
            )
            solver.point3 = constant.R.LF

        solver.R.slider_shock_length = dis3D(
            solver.R.susp_mount[x],
            solver.R.susp_mount[y],
            solver.R.susp_mount[z],
            constant.R.shock1.chassis_mount[x],
            constant.R.shock1.chassis_mount[y],
            constant.R.shock1.chassis_mount[z],
        )
        solver.R.slider_travel = (
            solver.R.slider_travel
            + travel.R.shock1.length[S.sample_points]
            + constant.R.slider_stop
            - solver.R.slider_shock_length
        )

    solver.R.hub[x], solver.R.hub[z] = on_axle_movement(
        constant.R.hub[x],
        constant.R.hub[z],
        constant.R.LA[x],
        constant.R.LA[z],
        solver.R.LA[x],
        solver.R.LA[z],
        solver.R.pinion_rad,
    )  # Calculate front hub center movement
    if S.simulate_tire_loading:  # If tire loading is being simulated
        solver.R.wheel_contact = solver.R.hub[z] - (
            constant.R.tire_diameter * 0.5
            - constant.R.tire_rate * (solver.R.slider_travel - constant.R.droop)
        )  # Calculate front contanct point
    else:
        solver.R.wheel_contact = (
            solver.R.hub[z] - constant.R.tire_radius
        )  # Calculate front contanct point

    if (constant.R.LF[z] - solver.R.LA[z]) / (constant.R.LF[x] - solver.R.LA[x]) == (
        constant.R.UF[z] - solver.R.UA[z]
    ) / (
        constant.R.UF[x] - solver.R.UA[x]
    ):  # If slope of the front lower links is the same as the slope of the front upper links
        solver.R.IC[x] = solver.R.hub[x] + (
            constant.R.LF[x] - solver.R.LA[x]
        )  # Define point on wheel contact to infinite IC line
        solver.R.IC[z] = solver.R.wheel_contact + (
            constant.R.LF[z] - solver.R.LA[z]
        )  # Define point on wheel contact to infinite IC line
    else:
        solver.R.IC[x], solver.R.IC[z] = LineIntersect(
            constant.R.LF[x],
            constant.R.LF[z],
            solver.R.LA[x],
            solver.R.LA[z],
            constant.R.UF[x],
            constant.R.UF[z],
            solver.R.UA[x],
            solver.R.UA[z],
        )  # Find intersection of upper and lower links in side view

    solver.side_view_sqr = (
        constant.R.shock1.chassis_mount[x] - solver.R.susp_mount[x]
    ) ** 2 + (constant.R.shock1.chassis_mount[z] - solver.R.susp_mount[z]) ** 2
    solver.R.inboard_factor = sqrt(solver.side_view_sqr) / sqrt(
        solver.side_view_sqr + solver.R.shock1.delta_y**2
    )
    solver.R.distance_factor = dis2D(
        solver.R.IC[x], solver.R.IC[z], solver.R.susp_mount[x], solver.R.susp_mount[z]
    ) / dis2D(solver.R.IC[x], solver.R.IC[z], solver.R.hub[x], solver.R.hub[z])
    solver.R.shock_angle_factor = sin(
        point_angle(
            constant.R.shock1.chassis_mount[x],
            constant.R.shock1.chassis_mount[z],
            solver.R.susp_mount[x],
            solver.R.susp_mount[z],
            solver.point3[x],
            solver.point3[z],
        )
    )
    solver.R.shock_wheel_factor = cos(
        point_angle(
            solver.R.hub[x],
            solver.R.hub[z],
            solver.R.IC[x],
            solver.R.IC[z],
            solver.R.hub[x],
            solver.R.IC[z],
        )
    )
    solver.R.IR = (
        constant.R.shock1.link_factor
        * solver.R.inboard_factor
        * solver.R.distance_factor
        * solver.R.shock_angle_factor
        * solver.R.shock_wheel_factor
    )

    solver.F.drive_x = (
        travel.F.hub[i][x] * constant.V.drive_bias
    )  # Find front anti lift x measument point, accounting for change in wheelbase
    solver.F.brake_x = (
        travel.F.hub[i][x] * constant.V.brake_bias
    )  # Find front anti dive x measument point, accounting for change in wheelbase
    solver.R.drive_x = (
        constant.V.wheelbase - travel.R.hub[i][x]
    ) * constant.V.drive_bias + travel.R.hub[i][
        x
    ]  # Find rear anti squat x measument point, accounting for change in wheelbase
    solver.R.brake_x = (
        constant.V.wheelbase - travel.R.hub[i][x]
    ) * constant.V.brake_bias + travel.R.hub[i][
        x
    ]  # Find rear anti lift x measument point, accounting for change in wheelbase
    solver.F.drive_intersect_z = LineIntersect(
        solver.F.wheel_contact,
        travel.F.hub[i][x],
        travel.F.IC[i][x],
        travel.F.IC[i][z],
        solver.F.drive_x,
        0,
        solver.F.drive_x,
        1,
    )[
        1
    ]  # Find where anti line crosses under/over measurement point
    solver.F.brake_intersect_z = LineIntersect(
        solver.F.wheel_contact,
        travel.F.hub[i][x],
        travel.F.IC[i][x],
        travel.F.IC[i][z],
        solver.F.brake_x,
        0,
        solver.F.brake_x,
        1,
    )[
        1
    ]  # Find where anti line crosses under/over measurement point
    solver.R.drive_intersect_z = LineIntersect(
        solver.R.wheel_contact,
        travel.R.hub[i][x],
        travel.R.IC[i][x],
        travel.R.IC[i][z],
        solver.R.drive_x,
        0,
        solver.R.drive_x,
        1,
    )[
        1
    ]  # Find where anti line crosses under/over measurement point
    solver.R.brake_intersect_z = LineIntersect(
        solver.R.wheel_contact,
        travel.R.hub[i][x],
        travel.R.IC[i][x],
        travel.R.IC[i][z],
        solver.R.brake_x,
        0,
        solver.R.brake_x,
        1,
    )[
        1
    ]  # Find where anti line crosses under/over measurement point

    constant.F.slider_anti_lift[0] = (
        solver.F.drive_intersect_z - solver.F.wheel_contact
    ) / (
        constant.F.anti_CG - solver.F.wheel_contact
    )  # Calculate front anti lift
    constant.F.slider_anti_dive[0] = (
        solver.F.brake_intersect_z - solver.F.wheel_contact
    ) / (
        constant.F.anti_CG - solver.F.wheel_contact
    )  # Calculate front anti dive
    constant.R.slider_anti_squat[0] = (
        solver.R.drive_intersect_z - solver.R.wheel_contact
    ) / (
        constant.R.anti_CG - solver.R.wheel_contact
    )  # Calculate rear anti squat
    constant.R.slider_anti_lift[0] = (
        solver.R.brake_intersect_z - solver.R.wheel_contact
    ) / (
        constant.R.anti_CG - solver.R.wheel_contact
    )  # Calculate rear anti lift

    # ------------------------------------  Shock Math  --------------------------------

    constant.V.sprung_cg[x] = (
        constant.V.wheelbase * constant.V.weight_distribution * constant.V.mass
        - constant.V.wheelbase * constant.F.unsprung_mass
    ) / (constant.V.sprung_mass)

    constant.F.corner_sprung_weight = (
        (constant.V.mass - constant.F.unsprung_mass - constant.R.unsprung_mass)
        * (constant.V.sprung_cg[x] / constant.V.wheelbase)
        / 2
    )
    constant.R.corner_sprung_weight = (
        constant.V.mass
        - constant.F.unsprung_mass
        - constant.R.unsprung_mass
        - 2 * constant.F.corner_sprung_weight
    ) / 2

    if constant.V.spring_method == 1:  # Frequecncy Based
        time_to_travel_wheelbase = (
            constant.V.wheelbase * 0.0568 * constant.V.desired_speed
        )  # time to travel wheelbase, constant is conversion factor
        if constant.V.freq_approach == 0:  # Front frequrncy chosen
            solver.F.period = 1 / constant.F.freq_goal
            solver.R.period = solver.F.period + time_to_travel_wheelbase

            constant.F.target_initial_frequency = constant.F.freq_goal
            constant.R.target_initial_frequency = 1 / solver.R.period
        elif constant.V.freq_approach == 1:  # Rear frequency chosen
            solver.R.period = 1 / constant.R.freq_goal
            solver.F.period = solver.R.period - time_to_travel_wheelbase

            constant.R.target_initial_frequency = constant.R.freq_goal
            constant.F.target_initial_frequency = 1 / solver.F.period
        else:  # Front and rear chosen
            solver.F.period = 1 / constant.F.freq_goal
            solver.R.period = 1 / constant.R.freq_goal

            constant.F.target_initial_frequency = constant.F.freq_goal
            constant.R.target_initial_frequency = constant.R.freq_goal
        del time_to_travel_wheelbase

        constant.F.target_initial_wheel_rate = (
            constant.F.corner_sprung_weight
            * (2 * pi() * constant.F.target_initial_frequency)
            ^ 2
        ) / 386.088
        constant.R.target_initial_wheel_rate = (
            constant.R.corner_sprung_weight
            * (2 * pi() * constant.R.target_initial_frequency)
            ^ 2
        ) / 386.088
    else:  # Preload Based
        constant.F.target_initial_wheel_rate = constant.F.corner_sprung_weight / (
            constant.F.droop * -1
            + constant.F.preload_goal / travel.F.shock1.IR[S.sample_points]
        )
        constant.R.target_initial_wheel_rate = constant.R.corner_sprung_weight / (
            constant.R.droop * -1
            + constant.R.preload_goal / travel.R.shock1.IR[S.sample_points]
        )

    constant.F.target_final_wheel_rate = (
        constant.F.target_initial_wheel_rate * constant.F.step_up_ratio
    )
    constant.R.target_final_wheel_rate = (
        constant.R.target_initial_wheel_rate * constant.R.step_up_ratio
    )

    constant.F.target_final_frequency = sqrt(
        (386.088 * constant.F.target_final_wheel_rate) / constant.F.corner_sprung_weight
    ) / (2 * pi)
    constant.R.target_final_frequency = sqrt(
        (386.088 * constant.R.target_final_wheel_rate) / constant.R.corner_sprung_weight
    ) / (2 * pi)

    constant.F.target_initial_spring_rate = constant.F.target_initial_wheel_rate / (
        travel.F.shock1.IR[S.sample_points] ** 2
    )
    if constant.F.slider_stop >= 0:
        constant.F.target_main_spring_rate = (
            constant.F.target_initial_spring_rate * constant.F.step_up_ratio
        )
    else:
        constant.F.target_main_spring_rate = constant.F.target_initial_spring_rate
    constant.F.target_tender_spring_rate = (
        constant.F.step_up_ratio
        * constant.F.target_initial_spring_rate
        / (constant.F.step_up_ratio - 1)
    )
    constant.R.target_initial_spring_rate = constant.R.target_initial_wheel_rate / (
        travel.R.shock1.IR[S.sample_points] ** 2
    )
    if constant.R.slider_stop >= 0:
        constant.R.target_main_spring_rate = (
            constant.R.target_initial_spring_rate * constant.R.step_up_ratio
        )
    else:
        constant.R.target_main_spring_rate = constant.R.target_initial_spring_rate
    constant.R.target_tender_spring_rate = (
        constant.R.step_up_ratio
        * constant.R.target_initial_spring_rate
        / (constant.R.step_up_ratio - 1)
    )
    # ------------------------------------------- Pick closest spring rate ------------------------------------------
    match str(constant.F.coil_size):
        case "2.0":
            solver.F.main_spring_list = constant.springs.s20[
                str(constant.F.main_spring_length)
            ]
        case "2.5":
            solver.F.main_spring_list = constant.springs.s25[
                str(constant.F.main_spring_length)
            ]
        case "3.0":
            solver.F.main_spring_list = constant.springs.s30[
                str(constant.F.main_spring_length)
            ]
    match str(constant.F.coil_size):
        case "2.0":
            solver.F.tender_spring_list = constant.springs.s20[
                str(constant.F.tender_spring_length)
            ]
        case "2.5":
            solver.F.tender_spring_list = constant.springs.s25[
                str(constant.F.tender_spring_length)
            ]
        case "3.0":
            solver.F.tender_spring_list = constant.springs.s30[
                str(constant.F.tender_spring_length)
            ]

    match str(constant.R.coil_size):
        case "2.0":
            solver.R.main_spring_list = constant.springs.s20[
                str(constant.R.main_spring_length)
            ]
        case "2.5":
            solver.R.main_spring_list = constant.springs.s25[
                str(constant.R.main_spring_length)
            ]
        case "3.0":
            solver.R.main_spring_list = constant.springs.s30[
                str(constant.R.main_spring_length)
            ]
    match str(constant.R.coil_size):
        case "2.0":
            solver.R.tender_spring_list = constant.springs.s20[
                str(constant.R.tender_spring_length)
            ]
        case "2.5":
            solver.R.tender_spring_list = constant.springs.s25[
                str(constant.R.tender_spring_length)
            ]
        case "3.0":
            solver.R.tender_spring_list = constant.springs.s30[
                str(constant.R.tender_spring_length)
            ]

    constant.F.closest_match_main_spring = solver.F.main_spring_list[
        min(
            range(len(solver.F.main_spring_list)),
            key=lambda idx: abs(
                solver.F.main_spring_list[idx] - constant.F.target_main_spring_rate
            ),
        )
    ]
    constant.F.closest_match_tender_spring = solver.F.tender_spring_list[
        min(
            range(len(solver.F.tender_spring_list)),
            key=lambda idx: abs(
                solver.F.tender_spring_list[idx] - constant.F.target_tender_spring_rate
            ),
        )
    ]
    constant.R.closest_match_main_spring = solver.R.main_spring_list[
        min(
            range(len(solver.R.main_spring_list)),
            key=lambda idx: abs(
                solver.R.main_spring_list[idx] - constant.R.target_main_spring_rate
            ),
        )
    ]
    constant.R.closest_match_tender_spring = solver.R.tender_spring_list[
        min(
            range(len(solver.R.tender_spring_list)),
            key=lambda idx: abs(
                solver.R.tender_spring_list[idx] - constant.R.target_tender_spring_rate
            ),
        )
    ]

    # ------------------------------------------- Wheel rates and force math ----------------------------------------

    for i in range(0, 2 * S.sample_points + 1):
        if travel.F.travel_dist[i] - travel.F.travel_dist[0] <= constant.F.slider_stop:
            travel.F.wheel_rate_closest[i] = (
                travel.F.shock1.IR[i] ** 2 * constant.F.closest_match_Ki
            )
            travel.F.wheel_rate_chosen[i] = (
                travel.F.shock1.IR[i] ** 2 * constant.F.used_Ki
            )

            travel.F.spring_force_closest[i] = constant.F.closest_match_Ki * (
                constant.F.used_preload
                + constant.F.shock1.length_extended
                - travel.F.shock1.length[i]
            )
            travel.F.spring_force_chosen[i] = constant.F.used_Ki * (
                constant.F.used_preload
                + constant.F.shock1.length_extended
                - travel.F.shock1.length[i]
            )

            solver.F.stop_insert = i + 1
        else:
            travel.F.wheel_rate_closest[i] = (
                travel.F.shock1.IR[i] ** 2 * constant.F.closest_match_main_spring
            )
            travel.F.wheel_rate_chosen[i] = (
                travel.F.shock1.IR[i] ** 2 * constant.F.used_main_spring
            )

            travel.F.spring_force_closest[i] = constant.F.closest_match_Ki * (
                constant.F.used_preload
                + constant.F.shock1.length_extended
                - solver.F.slider_shock_length
            ) + constant.F.closest_match_main_spring * (
                travel.F.shock1.length[i] - solver.F.slider_shock_length
            )
            travel.F.spring_force_chosen[i] = constant.F.used_Ki * (
                constant.F.used_preload
                + constant.F.shock1.length_extended
                - solver.F.slider_shock_length
            ) + constant.F.used_main_spring * (
                travel.F.shock1.length[i] - solver.F.slider_shock_length
            )

        if travel.R.travel_dist[i] - travel.R.travel_dist[0] <= constant.R.slider_stop:
            travel.R.wheel_rate_closest[i] = (
                travel.R.shock1.IR[i] ** 2 * constant.R.closest_match_Ki
            )
            travel.R.wheel_rate_chosen[i] = (
                travel.R.shock1.IR[i] ** 2 * constant.R.used_Ki
            )

            travel.R.spring_force_closest[i] = constant.R.closest_match_Ki * (
                constant.R.used_preload
                + constant.R.shock1.length_extended
                - travel.R.shock1.length[i]
            )
            travel.R.spring_force_chosen[i] = constant.R.used_Ki * (
                constant.R.used_preload
                + constant.R.shock1.length_extended
                - travel.R.shock1.length[i]
            )

            solver.R.stop_insert = i + 1
        else:
            travel.R.wheel_rate_closest[i] = (
                travel.R.shock1.IR[i] ** 2 * constant.R.closest_match_main_spring
            )
            travel.R.wheel_rate_chosen[i] = (
                travel.R.shock1.IR[i] ** 2 * constant.R.used_main_spring
            )

            travel.R.spring_force_closest[i] = constant.R.closest_match_Ki * (
                constant.R.used_preload
                + constant.R.shock1.length_extended
                - solver.R.slider_shock_length
            ) + constant.R.closest_match_main_spring * (
                travel.R.shock1.length[i] - solver.R.slider_shock_length
            )
            travel.R.spring_force_chosen[i] = constant.R.used_Ki * (
                constant.R.used_preload
                + constant.R.shock1.length_extended
                - solver.R.slider_shock_length
            ) + constant.R.used_main_spring * (
                travel.R.shock1.length[i] - solver.R.slider_shock_length
            )

        travel.F.wheel_force_closest[i] = (
            travel.F.spring_force_closest[i] * travel.F.shock1.IR[i] ** 2
        )
        travel.R.wheel_force_closest[i] = (
            travel.R.spring_force_closest[i] * travel.R.shock1.IR[i] ** 2
        )

        travel.F.wheel_force_chosen[i] = (
            travel.F.spring_force_chosen[i] * travel.F.shock1.IR[i] ** 2
        )
        travel.R.wheel_force_chosen[i] = (
            travel.R.spring_force_chosen[i] * travel.F.shock1.IR[i] ** 2
        )

    #
    travel.F.wheel_rate_closest = np.insert(
        travel.F.wheel_rate_closest,
        solver.F.stop_insert,
        solver.F.slider_stop_IR**2 * constant.F.closest_match_Ki,
    )
    travel.F.wheel_rate_closest = np.insert(
        travel.F.wheel_rate_closest,
        solver.F.stop_insert + 1,
        solver.F.slider_stop_IR**2 * constant.F.closest_match_main_spring,
    )
    travel.R.wheel_rate_closest = np.insert(
        travel.R.wheel_rate_closest,
        solver.R.stop_insert,
        solver.R.slider_stop_IR**2 * constant.R.closest_match_Ki,
    )
    travel.R.wheel_rate_closest = np.insert(
        travel.R.wheel_rate_closest,
        solver.R.stop_insert + 1,
        solver.R.slider_stop_IR**2 * constant.R.closest_match_main_spring,
    )

    travel.F.wheel_rate_chosen = np.insert(
        travel.F.wheel_rate_chosen,
        solver.F.stop_insert,
        solver.F.slider_stop_IR**2 * constant.F.used_Ki,
    )
    travel.F.wheel_rate_chosen = np.insert(
        travel.F.wheel_rate_chosen,
        solver.F.stop_insert + 1,
        solver.F.slider_stop_IR**2 * constant.F.used_main_spring,
    )
    travel.R.wheel_rate_chosen = np.insert(
        travel.R.wheel_rate_chosen,
        solver.R.stop_insert,
        solver.R.slider_stop_IR**2 * constant.R.used_Ki,
    )
    travel.R.wheel_rate_chosen = np.insert(
        travel.R.wheel_rate_chosen,
        solver.R.stop_insert + 1,
        solver.R.slider_stop_IR**2 * constant.R.used_main_spring,
    )

    travel.F.wheel_force_closest = np.insert(
        travel.F.wheel_force_closest,
        solver.F.stop_insert,
        constant.F.closest_match_Ki
        * (
            constant.F.used_preload
            + travel.F.shock1.length[0]
            - solver.F.slider_shock_length
        )
        * travel.F.shock1.IR[i] ** 2,
    )
    travel.R.wheel_force_closest = np.insert(
        travel.R.wheel_force_closest,
        solver.R.stop_insert,
        constant.R.closest_match_Ki
        * (
            constant.R.used_preload
            + travel.R.shock1.length[0]
            - solver.R.slider_shock_length
        )
        * travel.R.shock1.IR[i] ** 2,
    )

    travel.F.wheel_force_chosen = np.insert(
        travel.F.wheel_force_chosen,
        solver.F.stop_insert,
        constant.F.used_Ki
        * (
            constant.F.used_preload
            + travel.F.shock1.length[0]
            - solver.F.slider_shock_length
        )
        * travel.F.shock1.IR[i] ** 2,
    )
    travel.R.wheel_force_chosen = np.insert(
        travel.R.wheel_force_chosen,
        solver.F.stop_insert,
        constant.R.used_Ki
        * (
            constant.R.used_preload
            + travel.R.shock1.length[0]
            - solver.R.slider_shock_length
        )
        * travel.R.shock1.IR[i] ** 2,
    )

    travel.F.spring_force_closest = np.insert(
        travel.F.spring_force_closest,
        solver.F.stop_insert,
        constant.F.closest_match_Ki
        * (
            constant.F.used_preload
            + travel.F.shock1.length[0]
            - solver.F.slider_shock_length
        ),
    )
    travel.R.spring_force_closest = np.insert(
        travel.R.spring_force_closest,
        solver.R.stop_insert,
        constant.R.closest_match_Ki
        * (
            constant.R.used_preload
            + travel.R.shock1.length[0]
            - solver.R.slider_shock_length
        ),
    )

    travel.F.spring_force_chosen = np.insert(
        travel.F.spring_force_chosen,
        solver.F.stop_insert,
        constant.F.used_Ki
        * (
            constant.F.used_preload
            + travel.F.shock1.length[0]
            - solver.F.slider_shock_length
        ),
    )
    travel.R.spring_force_chosen = np.insert(
        travel.R.spring_force_chosen,
        solver.R.stop_insert,
        constant.R.used_Ki
        * (
            constant.R.used_preload
            + travel.R.shock1.length[0]
            - solver.R.slider_shock_length
        ),
    )
    #
    constant.F.slider_anti_lift[1] = solver.F.stop_insert
    constant.F.slider_anti_dive[1] = solver.F.stop_insert
    constant.R.slider_anti_squat[1] = solver.R.stop_insert
    constant.R.slider_anti_lift[1] = solver.R.stop_insert

    constant.F.closest_match_Ki = (
        constant.F.closest_match_main_spring
        * constant.F.closest_match_tender_spring
        / (
            constant.F.closest_match_main_spring
            + constant.F.closest_match_tender_spring
        )
    )
    if solver.F.stop_insert > S.sample_points:
        constant.F.closest_match_WRi = travel.F.wheel_rate_closest[S.sample_points]
    else:
        constant.F.closest_match_WRi = travel.F.wheel_rate_closest[S.sample_points + 2]
    if solver.F.stop_insert > S.sample_points * 2 + 1:
        constant.F.closest_match_WRf = travel.F.wheel_rate_closest[
            S.sample_points * 2 + 1
        ]
    else:
        constant.F.closest_match_WRf = travel.F.wheel_rate_closest[
            S.sample_points * 2 + 1 + 2
        ]
    constant.F.closest_match_SUR = (
        constant.F.closest_match_main_spring / constant.F.closest_match_Ki
    )
    constant.F.closest_match_Fni = sqrt(
        386.088 * constant.F.closest_match_WRi / constant.F.corner_sprung_weight
    ) / (2 * pi)
    constant.F.closest_match_Fnf = sqrt(
        386.088 * constant.F.closest_match_WRf / constant.F.corner_sprung_weight
    ) / (2 * pi)
    constant.F.closest_match_preload = (
        constant.F.corner_sprung_weight / constant.F.closest_match_WRi
        + constant.F.droop
    ) * travel.F.shock1.IR[2 * S.sample_points]
    constant.F.shock1.bump_length = travel.F.shock1.length[2 * S.sample_points]
    constant.F.shock2.bump_length = travel.F.shock2.length[2 * S.sample_points]
    constant.F.shock1.ride_length = travel.F.shock1.length[S.sample_points]
    constant.F.shock2.ride_length = travel.F.shock1.length[S.sample_points]
    constant.F.shock1.droop_length = travel.F.shock1.length[0]
    constant.F.shock2.droop_length = travel.F.shock1.length[0]
    constant.F.shock1.travel_used = (
        constant.F.shock1.droop_length - constant.F.shock1.bump_length
    )
    constant.F.shock2.travel_used = (
        constant.F.shock2.droop_length - constant.F.shock2.bump_length
    )
    constant.F.shock1.travel_used_percent = constant.F.shock1.travel_used / (
        constant.F.shock1.length_extended - constant.F.shock1.length_compressed
    )
    constant.F.shock2.travel_used_percent = constant.F.shock2.travel_used / (
        constant.F.shock1.length_extended - constant.F.shock1.length_compressed
    )
    constant.F.shock1.travel_ride_percent = (
        constant.F.shock1.ride_length - constant.F.shock1.bump_length
    ) / constant.F.shock1.travel_used
    constant.F.shock2.travel_ride_percent = (
        constant.F.shock2.ride_length - constant.F.shock2.bump_length
    ) / constant.F.shock2.travel_used
    constant.F.used_Ki = (
        constant.F.used_main_spring
        * constant.F.used_tender_spring
        / (constant.F.used_main_spring + constant.F.used_tender_spring)
    )
    constant.F.used_WRi = constant.F.used_Ki * (
        travel.F.shock1.IR[S.sample_points] ** 2
    )
    constant.F.used_WRf = constant.F.used_main_spring * (
        travel.F.shock1.IR[2 * S.sample_points] ** 2
    )
    constant.F.used_SUR = constant.F.used_main_spring / constant.F.used_Ki
    constant.F.used_Fni = sqrt(
        386.088 * constant.F.used_WRi / constant.F.corner_sprung_weight
    ) / (2 * pi)
    constant.F.used_Fnf = sqrt(
        386.088 * constant.F.used_WRf / constant.F.corner_sprung_weight
    ) / (2 * pi)
    constant.F.used_preload = (
        constant.F.corner_sprung_weight / constant.F.used_WRi + constant.F.droop
    ) * travel.F.shock1.IR[2 * S.sample_points]
    constant.F.shock1.distance_to_body_roll_axis = LineSeperation(
        constant.F.shock1.chassis_mount[x],
        constant.F.shock1.chassis_mount[y],
        constant.F.shock1.chassis_mount[z],
        constant.F.shock1.susp_mount[x],
        constant.F.shock1.susp_mount[y],
        constant.F.shock1.susp_mount[z],
        constant.V.wheelbase,
        0,
        travel.F.roll_center[S.sample_points],
        0,
        0,
        travel.R.roll_center[S.sample_points],
    )
    if constant.F.shock2.exists:
        constant.F.shock2.distance_to_body_roll_axis = LineSeperation(
            constant.F.shock2.chassis_mount[x],
            constant.F.shock2.chassis_mount[y],
            constant.F.shock2.chassis_mount[z],
            constant.F.shock2.susp_mount[x],
            constant.F.shock2.susp_mount[y],
            constant.F.shock2.susp_mount[z],
            constant.V.wheelbase,
            0,
            travel.F.roll_center[S.sample_points],
            0,
            0,
            travel.R.roll_center[S.sample_points],
        )

    constant.R.closest_match_Ki = (
        constant.R.closest_match_main_spring
        * constant.R.closest_match_tender_spring
        / (
            constant.R.closest_match_main_spring
            + constant.R.closest_match_tender_spring
        )
    )
    if solver.R.stop_insert > S.sample_points:
        constant.R.closest_match_WRi = travel.R.wheel_rate_closest[S.sample_points]
    else:
        constant.R.closest_match_WRi = travel.R.wheel_rate_closest[S.sample_points + 2]
    if solver.R.stop_insert > S.sample_points * 2 + 1:
        constant.R.closest_match_WRf = travel.R.wheel_rate_closest[S.sample_points * 2]
    else:
        constant.R.closest_match_WRf = travel.R.wheel_rate_closest[
            S.sample_points * 2 + 2
        ]
    constant.R.closest_match_SUR = (
        constant.R.closest_match_main_spring / constant.R.closest_match_Ki
    )
    constant.R.closest_match_Fni = sqrt(
        386.088 * constant.R.closest_match_WRi / constant.R.corner_sprung_weight
    ) / (2 * pi)
    constant.R.closest_match_Fnf = sqrt(
        386.088 * constant.R.closest_match_WRf / constant.R.corner_sprung_weight
    ) / (2 * pi)
    constant.R.closest_match_preload = (
        constant.R.corner_sprung_weight / constant.R.closest_match_WRi
        + constant.R.droop
    ) * travel.R.shock1.IR[2 * S.sample_points]
    constant.R.shock1.bump_length = travel.R.shock1.length[2 * S.sample_points]
    constant.R.shock2.bump_length = travel.R.shock1.length[2 * S.sample_points]
    constant.R.shock1.ride_length = travel.R.shock1.length[S.sample_points]
    constant.R.shock2.ride_length = travel.R.shock1.length[S.sample_points]
    constant.R.shock1.droop_length = travel.R.shock1.length[0]
    constant.R.shock2.droop_length = travel.R.shock1.length[0]
    constant.R.shock1.travel_used = (
        constant.R.shock1.droop_length - constant.R.shock1.bump_length
    )
    constant.R.shock2.travel_used = (
        constant.R.shock2.droop_length - constant.R.shock2.bump_length
    )
    constant.R.shock1.travel_used_percent = constant.R.shock1.travel_used / (
        constant.R.shock1.length_extended - constant.R.shock1.length_compressed
    )
    constant.R.shock2.travel_used_percent = constant.R.shock2.travel_used / (
        constant.R.shock2.length_extended - constant.R.shock2.length_compressed
    )
    constant.R.shock1.travel_ride_percent = (
        constant.R.shock1.ride_length - constant.R.shock1.bump_length
    ) / constant.R.shock1.travel_used
    constant.R.shock2.travel_ride_percent = (
        constant.R.shock2.ride_length - constant.R.shock2.bump_length
    ) / constant.R.shock2.travel_used
    constant.R.used_Ki = (
        constant.R.used_main_spring
        * constant.R.used_tender_spring
        / (constant.R.used_main_spring + constant.R.used_tender_spring)
    )
    constant.R.used_WRi = constant.R.used_Ki * (
        travel.R.shock1.IR[S.sample_points] ** 2
    )
    constant.R.used_WRf = constant.R.used_main_spring * (
        travel.R.shock1.IR[2 * S.sample_points] ** 2
    )
    constant.R.used_SUR = constant.R.used_main_spring / constant.R.used_Ki
    constant.R.used_Fni = sqrt(
        386.088 * constant.R.used_WRi / constant.R.corner_sprung_weight
    ) / (2 * pi)
    constant.R.used_Fnf = sqrt(
        386.088 * constant.R.used_WRf / constant.R.corner_sprung_weight
    ) / (2 * pi)
    constant.R.used_preload = (
        constant.R.corner_sprung_weight / constant.R.used_WRi + constant.R.droop
    ) * travel.R.shock1.IR[2 * S.sample_points]
    constant.R.shock1.distance_to_body_roll_axis = LineSeperation(
        constant.R.shock1.chassis_mount[x],
        constant.R.shock1.chassis_mount[y],
        constant.R.shock1.chassis_mount[z],
        constant.R.shock1.susp_mount[x],
        constant.R.shock1.susp_mount[y],
        constant.R.shock1.susp_mount[z],
        constant.V.wheelbase,
        0,
        travel.F.roll_center[S.sample_points],
        0,
        0,
        travel.R.roll_center[S.sample_points],
    )
    if constant.R.shock2.exists:
        constant.R.shock2.distance_to_body_roll_axis = LineSeperation(
            constant.R.shock2.chassis_mount[x],
            constant.R.shock2.chassis_mount[y],
            constant.R.shock2.chassis_mount[z],
            constant.R.shock2.susp_mount[x],
            constant.R.shock2.susp_mount[y],
            constant.R.shock2.susp_mount[z],
            constant.V.wheelbase,
            0,
            travel.F.roll_center[S.sample_points],
            0,
            0,
            travel.R.roll_center[S.sample_points],
        )

    solver.F.closest_match_period = 1 / constant.F.closest_match_Fni
    solver.F.used_period = 1 / constant.F.used_Fni
    solver.R.closest_match_period = 1 / constant.R.closest_match_Fni
    solver.R.used_period = 1 / constant.R.used_Fni

    constant.V.closest_match_speed = (
        0.0568
        * constant.V.wheelbase
        / (solver.F.closest_match_period - solver.R.closest_match_period)
    )
    constant.V.used_match_speed = (
        0.0568 * constant.V.wheelbase / (solver.F.used_period - solver.R.used_period)
    )

    constant.F.shock1.percent_bump_reminaing = (
        constant.F.shock1.length_compressed - constant.F.shock1.ride_length
    ) / (constant.F.shock1.length_extended)
    constant.F.shock2.percent_bump_reminaing = (
        constant.F.shock2.length_compressed - constant.F.shock2.ride_length
    ) / (constant.F.shock2.length_extended)
    constant.R.shock1.percent_bump_reminaing = (
        constant.R.shock1.length_compressed - constant.R.shock1.ride_length
    ) / (constant.R.shock1.length_extended)
    constant.R.shock2.percent_bump_reminaing = (
        constant.R.shock2.length_compressed - constant.R.shock2.ride_length
    ) / (constant.R.shock2.length_extended)

    output_processing_shocks()
