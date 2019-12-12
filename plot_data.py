import numpy as np 
import matplotlib.pyplot as plt 

for i in range(0,244):

    data = open('/output/' + str(i) + '/data/lum_observed.dat')

    seconds = data[:,0]
    luminosity = data[:,1]

    days = [i / (24 * 60 * 60) for i in seconds]
    log_luminosity = [np.log10(i) for i in luminosity]

    plt.plot(days, log_luminosity)

plt.show()