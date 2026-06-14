# src/suspension/io/material_add.py


def add_material(name, yield_strength, modulus_elasticity, density, notes):
    # IO Imports
    from tool_io.materials import load_materials
    from tool_io.variables import constant

    if name not in constant.materials.name:
        new_line = "\n{},{},{},{},{}".format(
            name, modulus_elasticity, yield_strength, density, notes
        )
        with open("Resources/materials.txt", "a") as f_object:
            f_object.write(new_line)
            f_object.close()
        load_materials()
