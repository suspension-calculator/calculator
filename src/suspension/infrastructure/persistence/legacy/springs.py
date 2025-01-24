# VariablesIO/springs.py


def load_spring_rates():
    import csv
    from suspension.io.variables import constant

    with open("resources/data/springs.txt", mode="r") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            match row[0]:
                case "2.0":
                    constant.springs.s20[row[1]] = [int(i) for i in row[2:]]
                case "2.5":
                    constant.springs.s25[row[1]] = [int(i) for i in row[2:]]
                case "3.0":
                    constant.springs.s30[row[1]] = [int(i) for i in row[2:]]
        constant.springs.s20["lengths"] = list(constant.springs.s20.keys())
        constant.springs.s25["lengths"] = list(constant.springs.s25.keys())
        constant.springs.s30["lengths"] = list(constant.springs.s30.keys())
