import numpy as np 
import os
import fileinput
import shutil

owd = os.getcwd

### Set values ###

Energy_guess = 10**52
Nickel_mass = 10**-0.75
alpha = 0.95
Nickel_boundary_mass = 11.83 + (15.541415935387822955 - 11.83)*alpha

# range = [-0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3]
# alpha_range = [0.1, 0.3, 0.5, 0.7, 0.9]

range = [-0.3, 0.3]
alpha_range = [0.1, 0.9]

permutations = []

for i in range:
    for j in range:
        for k in alpha_range:

            permutations.append([i,j,k])

for i in permutations:

    ### Makes directory ~/output/index of number, and then copies in a parameter file into there

    os.mkdir('output/' + str(permutations.index(i)))
    shutil.copy('original_parameters', 'output/' + str(permutations.index(i)))

    ### changes directorty into the index number directory and opens the parameter file to edit
    os.chdir('output/' + str(permutations.index(i)))
    parameters_file = open('original_parameters', 'r+')

    ### Edits line for that grid parameter
    for line in parameters_file:
        if line.split(None, 1)[0] == 'final_energy':
            line.replace(line, 'final_energy = ' + str(Energy_guess + i[0]))
            parameters_file.write(line)
        
        elif line.split(None, 1)[0] == 'Ni_mass':
            line.replace(line, 'Ni_mass = ' + str( Nickel_mass + i[1]))
            parameters_file.write(line)            

        elif line.split(None, 1)[0] == 'Ni_boundary_mass':
            line.replace(line, 'Ni_boundary_mass = ' + str(11.83 + (15.541415935387822955 - 11.83)*i[2]))
            parameters_file.write(line)
    
    parameters_file.close()
    os.chdir(owd)

    




