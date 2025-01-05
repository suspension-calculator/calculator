# VariablesIO/rod_end_add.py

def add_rod_end(name,radial_load,weight,hole_diameter,shank_diameter,thread):
    from VariableIO.rod_ends import load_rod_ends
    from VariableIO.variables import constant
    if not(name in constant.rod_ends.name):
        new_line = "\n{},{},{},{},{},{}".format(name,radial_load,weight,hole_diameter,shank_diameter,thread)
        with open('Lists/rod ends.txt','a') as f_object:
            f_object.write(new_line)
            f_object.close()
        load_rod_ends()