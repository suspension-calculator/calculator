# src/suspension/core/functions/distance_3d.py

def vectorsAngle(x1, y1, z1, x2, y2, z2):
    # Angle betwwen 2 vectors in 3D space
    # x1 is X value of vector 1
    # y1 is Y value of vector 1
    # z1 is Z value of vector 1
    # x2 is X value of vector 2
    # y2 is Y value of vector 2
    # z2 is Z value of vector 2

    from math import sqrt, acos, degrees
    x=0
    y=1
    z=2

    unit_1 = [0, 0, 0]
    unit_2 = [0, 0, 0]

    length_1 = sqrt(x1 ** 2 + y1 ** 2 + z1 ** 2)
    length_2 = sqrt(x2 ** 2 + y2 ** 2 + z2 ** 2)

    unit_1[x] = x1 / length_1
    unit_1[y] = y1 / length_1
    unit_1[z] = z1 / length_1

    unit_2[x] = x2 / length_2
    unit_2[y] = y2 / length_2
    unit_2[z] = z2 / length_2

    dot_result = unit_1[x] * unit_2[x] + unit_1[y] * unit_2[y] + unit_1[z] * unit_2[z]

    dot_limit = min(max(dot_result,-1),1)

    angle = acos(dot_limit)

    return angle