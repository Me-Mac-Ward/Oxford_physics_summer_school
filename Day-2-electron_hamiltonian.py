import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

# constants used throughout
BOHR_MAGNETON = 9.27 * 10**-24
PLANCK_CONSTANT = 6.63 * 10**-34
GYROMAGNETIC_FACTOR = 2.00 # made into a scalar
# defining the standard spin 1/2 matrices
S_x = 0.5 * np.array([[0,1],[1,0]])
S_z = 0.5 * np.array([[1,0],[0,-1]])


# B_0 = float(input("Enter value of B_0: ")) could replace defining the frequency depending on goal of program
frequency = 9.7 * 10**9 # hard coded goal - typical value used
theta = float(input("Enter value of theta: "))


# \hat{H} / B_0 = \mu_B g (S_x \sin\theta + S_z \sin\theta)
hamiltonian_NO_B_0 = (S_x * np.sin(theta) + S_z * np.cos(theta)) * BOHR_MAGNETON * GYROMAGNETIC_FACTOR



coordinates1 = [];coordinates2 = [];difference = []

intervals = 1000
for i in range(0, intervals):
    B_0val = i/intervals
    
    hamiltonian = hamiltonian_NO_B_0 * B_0val
    (eigenvalue1, eigenvalue2), (eigenvector1, eigenvector2) = np.linalg.eig(hamiltonian)

    coordinates1.append([B_0val, np.real(eigenvalue1/PLANCK_CONSTANT)])
    coordinates2.append([B_0val, np.real(eigenvalue2/PLANCK_CONSTANT)])

    difference.append([B_0val, abs(np.real(eigenvalue1/PLANCK_CONSTANT)-np.real(eigenvalue2/PLANCK_CONSTANT))])

# first energy level
npCoordinates1 = np.asarray(coordinates1)
x1,y1 = npCoordinates1.T
y1_in_GHz = y1 / 1e9

plt.plot(x1,y1_in_GHz)

# second energy level
npCoordinates2 = np.asarray(coordinates2)
x2,y2 = npCoordinates2.T
y2_in_GHz = y2 / 1e9

plt.plot(x2,y2_in_GHz)

plt.xlabel("B_0 / T")
plt.ylabel("f / GHz")

plt.show()


npDifference = np.asarray(difference)
xDif, yDif = npDifference.T
yDif_in_GHz = yDif / 1e9
plt.plot(xDif,yDif_in_GHz)
plt.xlabel("B_0 / T")
plt.ylabel("f / GHz")
plt.show()
