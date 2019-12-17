import numpy as np 
import matplotlib.pyplot as plt 
import os
from settings import *

def BackTrans(i,E_range, N_range, alpha_range, centre_param):
	n_N = len(N_range)
	n_alpha = len(alpha_range)
	alpha = str(alpha_range[int(i)%n_alpha])
	Ni  = N_range[(int(i)//(n_alpha))%n_N]
	E = E_range[(int(i)//(n_alpha*n_N))]
	return 'E:{}:NiM:{}:Alpha:{}'.format(str(E+centre_param[0]),str(Ni+centre_param[1]),alpha)

def GridPlot2(grid_folder_path):
    os.chdir(grid_folder_path)
    varyAlpha = []
    varyNiM = []
    varyEnergy = []
    i = 0
    for file in os.listdir(grid_folder_path):
        label = BackTrans(int(file),E_range, NiM_range, alpha_range,[Energy_center,Nickel_mass_center])
        x = label.split(':')

        if x[1] == str(Energy_center) and x[3] == str(Nickel_mass_center):
            varyAlpha.append([file,label])
        if x[1] == str(Energy_center) and x[5] == '0.5':
            varyNiM.append([file,label])
        if x[3] == str(Nickel_mass_center) and x[5] == '0.5':
            varyEnergy.append([file,label])
        i += 1
    plotter(varyAlpha,grid_folder_path, 'alpha')
    plotter(varyNiM,grid_folder_path, 'NiM')
    plotter(varyEnergy,grid_folder_path, 'Energy')

def plotter(points,grid_folder_path, vary):
    days = []
    files = [item[0] for item in points]
    labels = [item[1] for item in points]
    for i in range(len(files)):

        data = np.loadtxt(grid_folder_path + "/" + files[i] + "/data/lum_observed.dat")
        if days == []:
            seconds = data[:,0]
            days = [i / (24 * 60 * 60) for i in seconds]

        luminosity = data[:,1]
        log_luminosity = [np.log10(i) for i in luminosity]
        plt.plot(days, log_luminosity, label=labels[i])
    plt.legend()
    plt.xlabel('days since explosion')
    plt.ylabel('luminosity (log10)')
    plt.savefig(path + '/vary_{}'.format(vary))

GridPlot2(path + '/old_output2')