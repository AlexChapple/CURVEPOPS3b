import numpy as np 
import os
import fileinput
import shutil

owd = os.getcwd

### Set values ###

Energy = 52
Nickel_mass = -0.75
total_mass = 15.541415935387822955
excised = 11.83

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
    original = open('original_parameters','r')
    os.chdir('output')
    os.mkdir(str(permutations.index(i)))
    #shutil.copy('original_parameters', 'output/' + str(permutations.index(i)))

    ### changes directorty into the index number directory and opens the parameter file to edit
    os.chdir('output/' + str(permutations.index(i)))
    parameters_file = open('parameters', 'r+')

    ### Edits line for that grid parameter
    line_num = 0
    for line in parameters_file:
        line_num += 1

        if line_num == 19:
            newline = 'final_energy = ' + str(format(10**(Energy + i[0]), '.6e'))
            parameters_file.write(newline)
            parameters_file.write('\n')
        elif line_num == 49:
            newline = 'Ni_mass = ' + str(format(10**(Nickel_mass + i[1]), '.6e'))
            parameters_file.write(newline)
            parameters_file.write('\n')
        elif line_num == 50:
            newline = 'Ni_boundary_mass = ' + str( format( excised + (total_mass - excised)*i[2] ) )
            parameters_file.write(newline)
            parameters_file.write('\n')
        else:
            parameters_file.write(line)
    
    parameters_file.close()
    original.close()
    os.chdir(owd)

    




