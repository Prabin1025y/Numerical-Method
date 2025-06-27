import numpy as np
import pandas as pd

n = int(input("Enter the no of variables: "))
A = []
for i in range(n):
    A.append(list(map(float, input(f"Enter {i+1}th row of augmented matrix: ").split())))
A = np.array(A)
print("The augmented matrix A is: ")
print(np.matrix(A))

x = np.array(list(map(float, input("Enter the initial guesses: ").split())))
print("The initial guess is x: ")
print(np.matrix(x))

e = float(input("Enter the tolerable error: "))
N = int(input("Enter the maximum number of iterations: "))
iter = 1
Table = []
while iter <= N:
    x_old = np.copy(x)
    for i in range(n):
        s = 0
        for j in range(n):
            if j != i:
                s += A[i,j] * x_old[j]
        x[i] = (A[i, -1] - s) / A[i,i]
    err = np.abs(x - x_old)
    Table.append([iter] + [x[i] for i in range(n)])
    if np.all(err < e):
        break
    iter += 1

if iter > N:
    print(f"System does not converge in {N} iteration")
else:
    Table = pd.DataFrame(Table, columns=["iter"] + [f'x{i+1}' for i in range(n)]).to_string(index=False)
    print(Table)
    print("The solution is: ")
    for i in range(n):
        print(f"x{i+2} = {x[i]:.2f}")