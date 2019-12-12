import numpy as np 
import matplotlib.pyplot as plt 

best_chi_squared = 1000
best_day = []
best_lumonisty = []
observed = np.loadtxt('calibrated.txt')
observed_lum = observed[:,1]

for i in range(0,244):

    data = np.loadtxt('output/' + str(i) + '/data/lum_observed.dat')

    seconds = data[:,0]
    luminosity = data[:,1]

    days = [i / (24 * 60 * 60) for i in seconds]
    log_luminosity = [np.log10(i) for i in luminosity]

    ### Chi-squared analysis
    chi_squared = 0

    for i in observed[:,0]:

        if i in days:

            index = observed.index(i)

            x = (log_luminosity[index] - observed_lum[index])**2 / observed_lum[index]

            chi_squared += x

    if chi_squared < best_chi_squared:
        best_chi_squared = chi_squared
        best_day = days
        best_lumonisty = log_luminosity

    
plt.plot(best_day, best_lumonisty)

plt.show()