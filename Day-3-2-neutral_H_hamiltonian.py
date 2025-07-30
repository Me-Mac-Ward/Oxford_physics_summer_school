import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

# constants used throughout
GYROMAGENTIC_RATIO_e = 1.76e11
GYROMAGENTIC_RATIO_n = 2.68e8
HYPERFINE = 1.42e9

# defining the standard spin 1/2 matrices
sigma_x = 0.5 * np.array([[0,1],[1,0]])
sigma_z = 0.5 * np.array([[1,0],[0,-1]])
I_2 = 0.5 * np.array([[1,0],[0,1]])

theta = 0 # float(input("Enter value of theta: "))


# Electron Zeeman / B_0 = \gamma_e (\sigma_x \otimes I_2 \sin\theta + \sigma_z \otimes I_2 \cos\theta
electron_component_NO_B_0 = GYROMAGENTIC_RATIO_e * (np.kron(sigma_x, I_2) * np.sin(theta) + np.kron(sigma_z, I_2) * np.cos(theta)) 
# Nuclear Zeeman / B_0 = \gamma_n (I_2 \otimes \sigma_z \sin\theta + I_2 \otimes \sigma_z \cos\theta)
nuclear_component_NO_B_0 =  GYROMAGENTIC_RATIO_n * (np.kron(I_2, sigma_x) * np.sin(theta) + np.kron(I_2, sigma_z) * np.cos(theta))
# Sum of Electron and Nuclear Zeeman
electronuclear_NO_B_0 =  electron_component_NO_B_0 + nuclear_component_NO_B_0
# A (\sigma_x \otimes \sigma_x + \sigma_z \otimes \sigma_z)
hyperfine_component = HYPERFINE * (np.kron(sigma_x, sigma_x) + np.kron(sigma_z, sigma_z))

# rows/columns of overall matrix
matrix_dimension, _ = np.shape(hyperfine_component)


lines = []
for i in range(0, matrix_dimension):
    lines.append([])

intervals = 1000
for i in range(0, intervals):
    B_0val = i/intervals
    
    hamiltonian = electronuclear_NO_B_0 * B_0val + hyperfine_component
    eigenvalues, eigenvectors = np.linalg.eig(hamiltonian)

    for j in range(0, len(eigenvalues)):
        lines[j].append([B_0val, np.real(eigenvalues[j])])

for i in range(0, matrix_dimension):
    npCoordinates = np.asarray(lines[i])
    x, y = npCoordinates.T
    y_in_GHz = y / 1e9
    plt.plot(x,y_in_GHz)

plt.xlabel("B_0 / T")
plt.ylabel("f / GHz")

plt.show()
