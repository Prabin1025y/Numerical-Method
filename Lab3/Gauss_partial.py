import numpy as np

n = int(input("Enter the number of variables: "))
A= []
for i in range(n):
    A.append(list(map(float,input(f"Enter {i+1}th row: ").split())))
A = np.array(A)
print("The augmented matrix is A:")
print(np.matrix(A))
for i in range(n):
    p_row = np.argmax(np.abs(A[i:,i])) + i
    A[[i, p_row]] = A[[[p_row, i]]]
    for j in range(i+1,n):
        A[j] = A[j] - A[i] * (A[j,i] / A[i,i])
print("The uppertriangularmatrix A: ")
print(np.matrix(A))
x = np.zeros(n)
for i in range(n-1, -1, -1):
    x[i] =(A[i, -1] - np.sum(A[i, i+1:n] * x[i+1:n])) / A[i,i]
print("The solution is: ")
for i in range(n):
    print(f"x{i+1} = {x[i]}")
