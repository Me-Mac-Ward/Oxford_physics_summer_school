import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

BOHR_MAGNETON = 9.27 * 10**-24
PLANCK_CONSTANT = 6.63 * 10**-34
GYROMAGNETIC_FACTOR = 2.00





# H = \mu_B g (S_x B_0 sin\theta + S_z B_0 cos\theta)
def create_matrix(title):
    ARows = int(input(f"Enter the number of rows of the {title} matrix: "))
    ACols = int(input(f"Enter the number of columns of the {title} matrix: "))

    AMatrix = []
    print("Enter the matrix row by row, space separated\n")
    for i in range(ARows):
        row = list(map(complex, input(f"Row{i+1}: ").split()))
        if len(row) != ACols:
            print("Invalid, retry")
            exit()
        AMatrix.append(row)

    A = np.array(AMatrix)
    return A


S_x = create_matrix("S_x")
S_z = create_matrix("S_z")
# B_0 = float(input("Enter value of B_0: ")) could replace defining the frequency
frequency = 9.7 * 10**9
theta = float(input("Enter value of theta: "))

energy_change = PLANCK_CONSTANT * frequency

hamiltonian_NO_B_0 = (S_x * np.sin(theta) + S_z * np.cos(theta)) * BOHR_MAGNETON * GYROMAGNETIC_FACTOR


intervals = 1000
coordinates1 = []
coordinates2 = []
difference = []
for i in range(0, intervals):
    B_0val = i/intervals
    
    hamiltonian = hamiltonian_NO_B_0 * B_0val
    (eigenvalue1, eigenvalue2), (eigenvector1, eigenvector2) = np.linalg.eig(hamiltonian)

    coordinates1.append([B_0val, np.real(eigenvalue1/PLANCK_CONSTANT)])
    coordinates2.append([B_0val, np.real(eigenvalue2/PLANCK_CONSTANT)])

    difference.append([B_0val, abs(np.real(eigenvalue1/PLANCK_CONSTANT)-np.real(eigenvalue2/PLANCK_CONSTANT))])

npCoordinates1 = np.asarray(coordinates1)
x1,y1 = npCoordinates1.T

plt.plot(x1,y1)

npCoordinates2 = np.asarray(coordinates2)
x2,y2 = npCoordinates2.T

plt.plot(x2,y2)
plt.show()


npDifference = np.asarray(difference)
xDif, yDif = npDifference.T
plt.plot(xDif,yDif)
plt.show()
