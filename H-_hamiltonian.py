import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

# constants used throughout
GYROMAGENTIC_RATIO_e = 1.76e11
GYROMAGENTIC_RATIO_n = 2.68e8
HYPERFINE = 1.42e9
MAGNETIC_ANISTROPY = 1e9

# Electron Pauli Matrices
S_x = (1/np.sqrt(2)) * np.array([[0,1,0],[1,0,1],[0,1,0]])
S_z = np.array([[1,0,0],[0,0,0],[0,0,-1]])

# Nuclear Pauli Matrices
I_x = 0.5 * np.array([[0,1],[1,0]])
I_z = 0.5 * np.array([[1,0],[0,-1]])

# Identity
I_2 = np.eye(2)
I_3 = np.eye(3)


# B_0 = float(input("Enter value of B_0: ")) could replace defining the frequency depending on goal of program
frequency = 9.7 * 10**9 # hard coded goal - typical value used
theta = 0 #float(input("Enter value of theta: "))


# Electron Zeeman / B_0 = \gamma_e (S_x \otimes I_2 \sin\theta + S_z \otimes I_2 \cos\theta)
electron_component_NO_B_0 = GYROMAGENTIC_RATIO_e * (np.kron(S_x, I_2) * np.sin(theta) + np.kron(S_z, I_2) * np.cos(theta))
# Nuclear Zeeman / B_0 = \gamma_n (I_3 \otimes I_x \sin\theta + I_3 \otimes I_z \cos\theta)
nuclear_component_NO_B_0 =  GYROMAGENTIC_RATIO_n * (np.kron(I_3, I_x) * np.sin(theta) + np.kron(I_3, I_z) * np.cos(theta))
# Sum of Electron and Nuclear Zeeman
electronuclear_NO_B_0 =  electron_component_NO_B_0 + nuclear_component_NO_B_0
# Hyperfine Component = A (\S_x \otimes I_x + S_z \otimes I_z)
hyperfine_component = HYPERFINE * (np.kron(S_x,I_x) + np.kron(S_z, I_z))
# Magnetic Anistropy Component = D (S_z^2 \otimes I_2)
magnetic_anistropy_component = MAGNETIC_ANISTROPY * (np.kron((S_z @ S_z), I_2))


# rows/columns of overall matrix
matrix_dimension, _ = np.shape(hyperfine_component)


lines = []
for i in range(0, matrix_dimension):
    lines.append([])

intervals = 1000
for i in range(0, intervals):
    B_0val = i/intervals
    
    hamiltonian = electronuclear_NO_B_0 * B_0val + hyperfine_component + magnetic_anistropy_component
    eigenvalues, eigenvectors = np.linalg.eig(hamiltonian)

    for j in range(0, len(eigenvalues)):
        lines[j].append([B_0val, eigenvalues[j]])

for i in range(0, matrix_dimension):
    npCoordinates = np.asarray(lines[i])
    x, y = npCoordinates.T
    y_in_GHz = y / 1e9
    plt.plot(x,y_in_GHz)

plt.xlabel("B_0 / T")
plt.ylabel("f / GHz")

plt.show()