import numpy as np

def two_matrix_input():
    print("Kronecker Calculator \n\n\n")

    ARows = int(input("Enter the number of rows of the first matrix: "))
    ACols = int(input("Enter the number of columns of the first matrix: "))

    AMatrix = []
    print("Enter the matrix row by row, space separated\n")
    for i in range(ARows):
        row = list(map(complex, input(f"Row{i+1}: ").split()))
        if len(row) != ACols:
            print("Invalid, retry")
            exit()
        AMatrix.append(row)

    A = np.array(AMatrix)
    print(f"Here is matrix A: \n{A}")

    BRows = int(input("Enter the number of rows of the second matrix: "))
    BCols = int(input("Enter the number of columns of the second matrix: "))

    BMatrix = []
    print("Enter the matrix row by row, space separated\n")
    for i in range(BRows):
        row = list(map(complex, input(f"Row{i+1}: ").split()))
        if len(row) != BCols:
            print("Invalid, retry")
            exit()
        BMatrix.append(row)

    B = np.array(BMatrix)
    print(f"Here is matrix B: \n{B}")

    return(A,B)

def kronecker_product(A,B):
    ARows,ACols = A.shape
    BRows,BCols = B.shape

    matrix = np.full((ARows*BRows,ACols*BCols), np.nan, dtype=complex)

    for ARow in range(ARows):
        for ACol in range(ACols):
            for BRow in range(BRows):
                for BCol in range(BCols):
                    matrix[BRows*ARow+BRow, BCols*ACol+BCol] = A[ARow,ACol] * B[BRow,BCol]

    return matrix

def matrix_multiplication(A,B):
    ARows,ACols = A.shape
    BRows,BCols = B.shape

    if (ACols != BRows) or (ARows != BCols):
        print("Invalid matrix multiplication")
        exit()

    matrix = np.full((ARows, BCols), np.nan, dtype=complex)

    for ARow in range(ARows):
        for BCol in range(BCols):
            total = 0
            for ACol in range(ACols):
                total += A[ARow,ACol] * B[ACol, BCol]
            matrix[ARow,BCol] = total
    
    return matrix



A,B = two_matrix_input()
matrix = kronecker_product(A,B)
print(f"A ⊗ B = \n {matrix}")

matrix = matrix_multiplication(A,B)
print(f"AB = \n {matrix}")
