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
    A[i] = A[i]/A[i,i]
    for j in range(n):
        if j != i:
            A[j] = A[j] - A[i] * A[j,i]
print("The Normal matrix A: ")
print(np.matrix(A))
x = A[:,-1]
print("The solution is: ")
for i in range(n):
    print(f"x{i+1} = {x[i]}")