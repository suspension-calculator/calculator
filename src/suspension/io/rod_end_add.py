# src/suspension/io/rod_end_add.py


def add_rod_end(name, radial_load, weight, hole_diameter, shank_diameter, thread):
    from suspension.io.rod_ends import load_rod_ends
    from suspension.io.variables import constant

    if name not in constant.rod_ends.name:
        new_line = "\n{},{},{},{},{},{}".format(
            name, radial_load, weight, hole_diameter, shank_diameter, thread
        )
        with open("Lists/rod ends.txt", "a") as f_object:
            f_object.write(new_line)
            f_object.close()
        load_rod_ends()
