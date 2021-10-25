import os

def calc_shielding(dimensions):
    dimensions.sort()
    return (3*dimensions[0]*dimensions[1]) + (2*dimensions[1]*dimensions[2]) + (2*dimensions[0]*dimensions[2])

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "examples");
dimensions = [];
print(filename)
for examplefile in os.listdir(filename):
    totalshielding = 0
    with open(filename+ "\\" + examplefile) as file:
        for line in file:
            dimensions = list(map(int, line.split("x")))
            totalshielding += calc_shielding(dimensions)
        print(examplefile + " total shielding required = " + str(totalshielding));






