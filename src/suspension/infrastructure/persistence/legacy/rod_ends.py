# src/suspension/io/rod_ends.py


def load_rod_ends():
    # This function loads rod end data
    import csv
    from suspension.io.variables import constant

    constant.rod_ends.name = []
    constant.rod_ends.radial_load = []
    constant.rod_ends.weight = []
    constant.rod_ends.hole_diameter = []
    constant.rod_ends.shank_diameter = []
    constant.rod_ends.thread = []

    with open("resources/data/rod ends.txt", mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            constant.rod_ends.name.append(row[csv_reader.fieldnames[0]])
            constant.rod_ends.radial_load.append(float(row[csv_reader.fieldnames[1]]))
            constant.rod_ends.weight.append(float(row[csv_reader.fieldnames[2]]))
            constant.rod_ends.hole_diameter.append(
                row[csv_reader.fieldnames[3]].replace(" ", "")
            )
            constant.rod_ends.shank_diameter.append(
                float(row[csv_reader.fieldnames[4]])
            )
            constant.rod_ends.thread.append(
                row[csv_reader.fieldnames[5]].replace(" ", "")
            )
