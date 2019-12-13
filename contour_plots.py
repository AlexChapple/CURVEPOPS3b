import numpy as np
import matplotlib.pyplot as plt

### Plotting parameters
xaxis_parameter = 'Energy'
yaxis_parameter = 'Nickel Mass'

### Set values ###
Energy = 52
Nickel_mass = -0.75
total_mass = 15.541415935387822955
excised = 11.83

### Observed data
observed = np.loadtxt('2017ein_observed.txt')
observed_days = observed[:,0] 
observed_lum = observed[:, 1]

### Grid Range
E_range = [-0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3]
NiM_range = [-0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3]
alpha_range = [0.1, 0.3, 0.5, 0.7, 0.9]

all_values = []

for i in E_range:
    for j in NiM_range:
        for k in alpha_range:
            
            all_values.append([i, j, k])

E_NiM_array = []
E_NiMB_array = []
NiM_NiMB = []

for i in all_values:

    E_NiM_array.append([i[0], i[1]])





def findChiValue(i):

    ### Data from mahuika for each model
    data = np.loadtxt('output/' + str(i) + '/data/lum_observed.dat')

    ### Truncation 
    data = data[data[:, 0] < (observed_days[-1] * 86400)]
    data = data[data[:, 0] > (observed_days[0] * 86400)]

    seconds = data[:, 0]
    luminosity = data[:, 1]

    ### Convert data
    days = np.array([i / (24 * 60 * 60) for i in seconds])
    log_luminosity = np.array([np.log10(i) for i in luminosity])

    ### interpolate data
    log_luminosity2 = np.interp(observed_days, days, log_luminosity)

    ### Chi-squared analysis
    chi_squared = 0

    for i in range(len(observed_days)): 

        dchi = (log_luminosity2[i] - observed_lum[i])** 2 / observed_lum[i]
        chi_squared += dchi

    return chi_squared




print(E_NiM_array)