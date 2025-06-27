import numpy as np
import pandas as pd

n = int(input("Enter the no of variables: "))
A = []
for i in range(n):
    A.append(list(map(float, input(f"Enter {i+1}th row of augmented matrix: ").split())))
A = np.array(A)
print("The augmented matrix A is: ")
print(np.matrix(A))

def inv(A):
    try:
        return np.linalg.inv(A)
    except:
        print("Matrix is singular")

B = np.array(inv(A))

x = np.array(list(map(float, input("Enter the initial vector: ").split())))
print("The initial vector is x: ")
print(np.matrix(x))

e = float(input("Enter the tolerable error: "))
N = int(input("Enter the maximum number of iterations: "))
iter = 1

Table = []

oldev = 0
while iter <= N:
    Y = np.dot(B,x)
    maxev = abs(max(Y, key=abs))
    for i in range(n):
        x = Y/maxev
    err = abs(maxev - oldev)
    Table.append([iter, maxev] + [x[i] for i in range(n)])
    if(err < e):
        break
    oldev = maxev
    iter += 1

if iter > N:
    print("No dominant eigen value found in {N} iterations.")
else:
    Table = pd.DataFrame(Table, columns=['Iter', "maxev"] + [f'x{i+1}' for i in range(n)]).to_string(index=False)
    print(Table)
    print(f"The Least eigen value is {1/maxev} in {iter} iterations")
    print("Corresponding eigen vector is: \n", np.matrix(x))