import os

def calc_shielding(dimensions):
    return (3*dimensions[0]*dimensions[1]) + (2*dimensions[1]*dimensions[2]) + (2*dimensions[0]*dimensions[2])

def calc_wiring(dimesions):
    return (dimensions[0]*dimensions[1]*dimesions[2]) + 2*(dimesions[0]+dimesions[1])

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "examples");
dimensions = [];
for examplefile in os.listdir(filename):
    totalshielding = 0;
    totalwiring = 0;
    with open(filename+ "\\" + examplefile) as file:
        for line in file:
            dimensions = list(map(int, line.split("x")));
            dimensions.sort();
            totalshielding += calc_shielding(dimensions);
            totalwiring += calc_wiring(dimensions);
        print(examplefile + " total shielding required = " + str(totalshielding));
        print(examplefile + " total wiring required = " + str(totalwiring));






