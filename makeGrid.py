import numpy as np 
import os
import fileinput
import shutil
from settings import *

permutations = []

for i in E_range:
    for j in NiM_range:
        for k in alpha_range:

            permutations.append([i,j,k])

for i in permutations:

    ### Makes directory ~/output/index of number, and then copies in a parameter file into there
    original = open('original_parameters','r')
    os.chdir('output')
    os.mkdir(str(permutations.index(i)))

    ### changes directorty into the index number directory and opens the parameter file to edit
    os.chdir(str(permutations.index(i)))
    os.mkdir('data')

    parameters_file = open('parameters', 'w+')

    ### Edits line for that grid parameter
    line_num = 0
    for line in original:
        line_num += 1

        if line_num == 19:
            newline = 'final_energy = ' + str(format(10**(Energy_center + i[0]), '.6e'))
            parameters_file.write(newline)
            parameters_file.write('\n')
        elif line_num == 49:
            newline = 'Ni_mass = ' + str(format(10**(Nickel_mass_center + i[1]), '.6e'))
            parameters_file.write(newline)
            parameters_file.write('\n')
        elif line_num == 50:
            newline = 'Ni_boundary_mass = ' + str( format( (excised + (total_mass - excised)*i[2]), '.6e' ) )
            parameters_file.write(newline)
            parameters_file.write('\n')
        else:
            parameters_file.write(line)
    
    parameters_file.close()
    original.close()
    os.chdir('/nesi/nobackup/uoa00094/CURVEPOPS3b/2017ein')

    




