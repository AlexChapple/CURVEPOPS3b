import numpy as np 
import os
from settings import *
from shutil import copyfile

def make_grid(counter):

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
        os.chdir(path + '2017_master' + 'model_' + str(counter))
 

### Finds 15 solar mass input files
### Path to input is the path to all input files 
os.chdir(path_to_input)

counter = 0
for file in os.listdir(path_to_input):

    ### Select 15 solar mass from file name
    if 'comp-z014-' + init_mass in file:

        os.mkdir('model_' + str(counter))
        path_to_directory_made = '' + '/' + 'model_' + str(counter)
        copyfile(file, path_to_directory_made)

        other_file = file.replace('-comp', '')
        copyfile(other_file, path_to_directory_made)

        copyfile('original_parameters', path_to_directory_made)
        os.chdir(path_to_directory_made)
        os.mkdir('output')

        make_grid(counter)

        counter += 1
    
