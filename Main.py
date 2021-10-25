import os

#function to calculate shielding
#parameters: list of dimensions (int[])
#returns: the amount of shielding required for that set of dimensions (int)
def calc_shielding(dimensions):
    return (3*dimensions[0]*dimensions[1]) + (2*dimensions[1]*dimensions[2]) + (2*dimensions[0]*dimensions[2])

#function to calculate wiring
#parameters: list of dimensions (int[])
#returns: the amount of wiring required for that set of dimensions (int)
def calc_wiring(dimesions):
    return (dimensions[0]*dimensions[1]*dimesions[2]) + 2*(dimesions[0]+dimesions[1])

#initialise realtive path location for example files
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "examples");

dimensions = [];

#iterate over each example file in  "examples" directory
for examplefile in os.listdir(filename):
    #reset variables between files
    totalshielding = 0;
    totalwiring = 0;

    #iterate over each line of the current file
    with open(filename + "\\" + examplefile) as file:
        for line in file:
            #convert line from file to int list and assign values to list variable
            dimensions = list(map(int, line.split("x")));

            #sort list into ascending order
            dimensions.sort();

            #sum totals of calculations
            totalshielding += calc_shielding(dimensions);
            totalwiring += calc_wiring(dimensions);

    #print outputs after completing each file
    print(examplefile + " total shielding required = " + str(totalshielding));
    print(examplefile + " total wiring required = " + str(totalwiring));