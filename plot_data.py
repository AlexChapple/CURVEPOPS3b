### This file fits the mahuika data to the observed data


import numpy as np 
import matplotlib.pyplot as plt
import os

### Best approximate variables
best_chi_squared = 100
best_day = []
best_lumonisty = []
directory = 0

### Observed data
observed = np.loadtxt('2017ein_observed.txt')
observed_days = observed[:,0] 
observed_lum = observed[:,1]

### Finding best fit

for i in range(0,244):

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

    ### Compares chi-squared value
    if chi_squared < best_chi_squared:
        best_chi_squared = chi_squared
        best_day = observed_days
        best_lumonisty = log_luminosity2
        directory = i

### Finds the parameters file for best fit

print('The best chi-squared value is ' + str(best_chi_squared))
print('The directory of the best fit is in '+ str(directory))

os.chdir('output/' + str(directory) + '/data')
parameter_file = open('parameters')
for line in parameter_file:
    print(line)
parameter_file.close()
os.chdir('/nesi/nobackup/uoa00094/CURVEPOPS3b/2017ein')

### Plotting and saving
plt.plot(observed_days, best_lumonisty, label='best guess')
plt.plot(observed_days, observed_lum, label='observed')
plt.xlabel('Day since explosion')
plt.ylabel('log L')
plt.title(best_chi_squared)
plt.legend()

plt.savefig('/nesi/nobackup/uoa00094/CURVEPOPS3b/2017ein/figure.png')