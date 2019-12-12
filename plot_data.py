### This file fits the mahuika data to the 

import numpy as np 
import matplotlib.pyplot as plt 

### Best approximate variables
best_chi_squared = 100
best_day = []
best_lumonisty = []

### Observed data
observed = np.loadtxt('calibrated.txt')
observed_days = observed[:,0] 
observed_lum = observed[:,1]

### Finding best fit

for i in range(0,244):

    ### Data from mahuika for each model
    data = np.loadtxt('output/' + str(i) + '/data/lum_observed.dat')

    ### Truncation 
    data = data[data[:, 0] < (observed_days[-1] * 86400)]
    data = data[data[:, 0] > (observed_days[0] * 86400)]

    seconds = data[:,0]
    luminosity = data[:, 1]

    ### Convert data
    days = np.array([i / (24 * 60 * 60) for i in seconds])
    log_luminosity = np.array([np.log10(i) for i in luminosity])

    ### interpolate data
    # observed_lum2 = np.interp(days, observed_days, observed_lum)
    observed_lum2 = np.interp(days, observed_days, observed_lum)

    ### Chi-squared analysis
    chi_squared = 0

    for i in range(len(days)): 

        dchi = (log_luminosity[i] - observed_lum2[i])** 2 / observed_lum2[i]
        chi_squared += dchi

    ### Compares to best chi-squared value
    if chi_squared < best_chi_squared:
        best_chi_squared = chi_squared
        best_day = days
        best_lumonisty = log_luminosity

print(best_chi_squared)
    

### Plotting
plt.plot(best_day, best_lumonisty, label='best guess')
plt.plot(best_day, observed_lum2, label='observed')
plt.legend()

plt.show()