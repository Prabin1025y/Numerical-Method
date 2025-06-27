import numpy as np
import scipy.linalg as slg

n = int(input("Enter the no of variables: "))
A = []
for i in range(n):
    A.append(list(map(float, input(f"Enter {i+1}th row of Coefficient matrix: ").split())))
A = np.array(A)
print("The Coefficient matrix A is: ")
print(np.matrix(A))

B = np.array(list(map(float, input("Enter the constant terms: ").split())))
print("TThe constant terms is: ")
print(np.matrix(B))

P, L, U = slg.lu(A)
lum = slg.lu_factor(A)
print("The lower triangular matrix is L: \n", L)
print("The upper triangular matrix is U: \n", U)
print("The permutation triangular matrix is P: \n", P)

x = slg.lu_solve(lum, B)
print("The solution is : \n", x)