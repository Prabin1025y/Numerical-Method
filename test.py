import numpy as np

A=[]
n = 50
for i in range(n):
    pivot = np.argmax(np.abs(A[i:, i])) + i
    A[[i, pivot]] = A[[[pivot, i]]]
    A[i] = A[i]/A[i,i]
    for j in range(n):
        if i != j:
            A[j] = A[j] - A[i] * A[j,i]
