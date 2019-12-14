import numpy as np
import matplotlib.pyplot as plt

### Set values ###
Energy_center = 52
Nickel_mass_center = -0.75
total_mass = 15.541415935387822955
excised = 11.83

### Observed data
observed = np.loadtxt('2017ein_observed.txt')
observed_days = observed[:, 0]
observed_lum = observed[:, 1]

### Grid Range
E_range = [-0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3]
NiM_range = [-0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3]
alpha_range = [0.1, 0.3, 0.5, 0.7, 0.9]

all_values = []

### Creates all permutations possible of Energy, Nickel Mass, and Nickel Boundary Mass
for i in E_range:
    for j in NiM_range:
        for k in alpha_range:
            
            all_values.append([i, j, k])

### Finds chi-squared value for the directory with index i
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

### Finds chi-squared value for all permutations and appends it as the 4th element
for i in range(len(all_values)):

    x = findChiValue(i)
    all_values[i].append(x)


### Plots Energy and Nickel mass contour plot
def contourf_E_NiM():

    reduced = all_values
    reduced2 = []
               
    ### reduces all_values to only the lowest chi-squared value
    for i in all_values:

        for j in reduced:

            if i[:2] == j[:2]:

                if i[3] < j[3]:

                    reduced[reduced.index(j)] = i

    ### Extracts the unique values out of temp_list 
    for i in reduced:

        if i in reduced2:
            pass
        else:
            reduced2.append(i)

    Energy_values = np.array([i[0] for i in reduced2])
    Nickel_mass = np.array([i[1] for i in reduced2])

    ### Creates mesh grid for Energy and Nickel mass
    Energy_values, Nickel_mass = np.meshgrid(Energy_values, Nickel_mass)

    ### Matrix of the same size as the Energy values and Nickel mass
    rows = len(Energy_values)
    columns = len(Energy_values[0])

    chi_squared_mesh = np.zeros((rows, columns))

    for i in range(rows):

        for j in range(columns):

            x = Energy_values[i][j]
            y = Nickel_mass[i][j]

            for k in reduced2:

                if k[0] == x and k[1] == y:

                    chi_squared_mesh[i][j] = k[3]

    ### Change to exponent form
    Energy_values = [10 ** (Energy_center + i) for i in Energy_values]
    Nickel_mass = [10 ** (i + Nickel_mass_center) for i in Nickel_mass]

    plt.figure(1)                   
    plt.contourf(Energy_values, Nickel_mass, chi_squared_mesh, 10, cmap='RdGy')
    plt.xlabel('Energy (log10)')
    plt.ylabel('Nickel Mass')
    plt.colorbar()
    print('first plot created')

### Plots Energy and Nickel boundary mass contour plot
def contourf_E_NiBM():

    reduced = all_values
    reduced2 = []
               
    ### reduces all_values to only the lowest chi-squared value
    for i in all_values:

        for j in reduced:

            if i[0] == j[0] and i[2] == j[2]:

                if i[3] < j[3]:

                    reduced[reduced.index(j)] = i

    ### Extracts the unique values out of temp_list 
    for i in reduced:

        if i in reduced2:
            pass
        else:
            reduced2.append(i)

    Energy_values = np.array([i[0] for i in reduced2])
    Nickel_boundary_mass = np.array([i[2] for i in reduced2])

    ### Creates mesh grid for Energy and Nickel mass
    Energy_values, Nickel_boundary_mass = np.meshgrid(Energy_values, Nickel_boundary_mass)

    ### Matrix of the same size as the Energy values and Nickel mass
    rows = len(Energy_values)
    columns = len(Energy_values[0])

    chi_squared_mesh = np.zeros((rows, columns))

    for i in range(rows):

        for j in range(columns):

            x = Energy_values[i][j]
            y = Nickel_boundary_mass[i][j]

            for k in reduced2:

                if k[0] == x and k[2] == y:

                    chi_squared_mesh[i][j] = k[3]

    ### Change to exponent form
    Energy_values = [10 ** (Energy_center + i) for i in Energy_values]
    Nickel_boundary_mass = [excised + (total_mass - excised)*i for i in Nickel_boundary_mass]

    plt.figure(2)                   
    plt.contourf(Energy_values, Nickel_boundary_mass, chi_squared_mesh, 10, cmap='RdGy')
    plt.xlabel('Energy (log10)')
    plt.ylabel('Nickel Boundary Mass')
    plt.colorbar()
    print('second plot created')

### Plots Nickel mass and Nickel boundary mass contour plot
def contourf_NiM_NiBM():

    reduced = all_values
    reduced2 = []
               
    ### reduces all_values to only the lowest chi-squared value
    for i in all_values:

        for j in reduced:

            if i[1] == j[1] and i[2] == j[2]:

                if i[3] < j[3]:

                    reduced[reduced.index(j)] = i

    ### Extracts the unique values out of temp_list 
    for i in reduced:

        if i in reduced2:

            pass

        else:

            reduced2.append(i)

    NiM_values = np.array([i[1] for i in reduced2])
    Nickel_boundary_mass = np.array([i[2] for i in reduced2])

    ### Creates mesh grid for Energy and Nickel mass
    NiM_values, Nickel_boundary_mass = np.meshgrid(NiM_values, Nickel_boundary_mass)

    ### Matrix of the same size as the Energy values and Nickel mass
    rows = len(NiM_values)
    columns = len(NiM_values[0])

    chi_squared_mesh = np.zeros((rows, columns))

    for i in range(rows):

        for j in range(columns):

            x = NiM_values[i][j]
            y = Nickel_boundary_mass[i][j]

            for k in reduced2:

                if k[1] == x and k[2] == y:

                    chi_squared_mesh[i][j] = k[3]

    ### Change to exponent form
    NiM_values = [10 ** (Nickel_mass_center + i) for i in NiM_values]
    Nickel_boundary_mass = [excised + (total_mass - excised)*i for i in Nickel_boundary_mass]

    plt.figure(3)                   
    plt.contourf(NiM_values, Nickel_boundary_mass, chi_squared_mesh, 7, cmap='RdGy')
    plt.xlabel('Nickel mass')
    plt.ylabel('Nickel Boundary Mass')
    plt.colorbar()
    print('third plot created')

contourf_NiM_NiBM()
contourf_E_NiM()
contourf_E_NiBM()

plt.show()

