# VariablesIO/material_add.py

def add_material(name,yield_strength,modulus_elasticity,density,notes):
    from suspension.io.materials import load_materials
    from suspension.io.variables import constant
    if not(name in constant.materials.name):
        new_line = "\n{},{},{},{},{}".format(name,modulus_elasticity,yield_strength,density,notes)
        with open('Lists/materials.txt','a') as f_object:
            f_object.write(new_line)
            f_object.close()
        load_materials()