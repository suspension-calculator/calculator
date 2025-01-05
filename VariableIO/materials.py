def load_materials():
    # This function loads material properties data
    import csv
    from VariableIO.variables import constant

    constant.materials.name = []
    constant.materials.yield_strength = []
    constant.materials.modulus_elasticity = []
    constant.materials.density = []
    constant.materials.notes = []

    with open('Lists/materials.txt', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            constant.materials.name.append(row[csv_reader.fieldnames[0]])
            constant.materials.modulus_elasticity.append(float(row[csv_reader.fieldnames[1]]))
            constant.materials.yield_strength.append(float(row[csv_reader.fieldnames[2]]))
            constant.materials.density.append(float(row[csv_reader.fieldnames[3]]))
            constant.materials.notes.append(row[csv_reader.fieldnames[4]])