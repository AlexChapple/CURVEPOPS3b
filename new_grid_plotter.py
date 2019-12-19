import numpy as np
import matplotlib.pyplot as plt
from settings import *

def create_all_permutations():

    all_values = []

    for i in E_range:
        for j in NiM_range:
            for k in alpha_range:
                
                all_values.append([i, j, k])
    
    return all_values

def E_plotter():

    all_values = create_all_permutations()
    days_list = []
    luminosity_list = []
    Energy_param_list = []

    for i in all_values:

        if i[1] == 0 and i[2] == 0.5:
            
            data = np.loadtxt('output/' + str(all_values.index(i)) + '/data/lum_observed.dat')
            
            seconds = data[:, 0]
            luminosity = data[:, 1]
            
            days = [j / 86400 for j in seconds]
            log_luminosity = [np.log10(j) for j in luminosity]

            days_list.append(days)
            luminosity_list.append(log_luminosity)
            Energy_param_list.append(i[0])

    for i in range(len(days_list)):
        plt.figure(1)
        plt.plot(days_list[i], luminosity_list[i], label='Energy: ' + str(format(10 ** (Energy_center + Energy_param_list[i]), '.1e')))
        plt.xlabel('Day since explosion')
        plt.ylabel('Luminosity (log10)')
        plt.legend()
        plt.savefig(path + '/Energy.png', dpi=300)

def NiM_plotter():

    all_values = create_all_permutations()
    days_list = []
    luminosity_list = []
    NiM_param_list = []

    for i in all_values:

        if i[0] == 0 and i[2] == 0.5:
            
            data = np.loadtxt('output/' + str(all_values.index(i)) + '/data/lum_observed.dat')
            
            seconds = data[:, 0]
            luminosity = data[:, 1]
            
            days = [j / 86400 for j in seconds]
            log_luminosity = [np.log10(j) for j in luminosity]

            days_list.append(days)
            luminosity_list.append(log_luminosity)
            NiM_param_list.append(i[1])

    for i in range(len(days_list)):
        plt.figure(2)
        plt.plot(days_list[i], luminosity_list[i], label='NiM: ' + str(format(10 ** (Nickel_mass_center + NiM_param_list[i]), '.1e')))
        plt.xlabel('Day since explosion')
        plt.ylabel('Luminosity (log10)')
        plt.legend()
        plt.savefig(path + '/NiM.png', dpi=300)


def NiBM_plotter():

    all_values = create_all_permutations()
    days_list = []
    luminosity_list = []
    NiBM_param_list = []

    for i in all_values:

        if i[0] == 0 and i[1] == 0:
            
            data = np.loadtxt('output/' + str(all_values.index(i)) + '/data/lum_observed.dat')
            
            seconds = data[:, 0]
            luminosity = data[:, 1]
            
            days = [j / 86400 for j in seconds]
            log_luminosity = [np.log10(j) for j in luminosity]

            days_list.append(days)
            luminosity_list.append(log_luminosity)
            NiBM_param_list.append(i[2])

    for i in range(len(days_list)):
        plt.figure(3)
        plt.plot(days_list[i], luminosity_list[i], label='NiBM: ' + str(NiBM_param_list[i]))
        plt.xlabel('Day since explosion')
        plt.ylabel('Luminosity (log10)')
        plt.legend()
        plt.savefig(path + '/alpha.png', dpi=300)

E_plotter()
NiM_plotter()
NiBM_plotter()



