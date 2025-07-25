import numpy as np
import scipy.linalg as slg
import matplotlib.pyplot as plt

X = np.array(list(map(float, input("Enter all x-data:").split())))
Y = np.array(list(map(float, input("Enter all y-data:").split())))
n=len(X)

A = [[n, np.sum(X), np.sum(X**2)],
     [np.sum(X), np.sum(X**2),np.sum(X**3)],
     [np.sum(X**2), np.sum(X**3), np.sum(X**4)]]

B = [[np.sum(Y)], [np.sum(X*Y)], [np.sum(X**2*Y)]]
print(f"The coefficient matrix of system of normal eqn:\n {np.matrix(A)}")
print(f"The output matrix of system of normal eqn: \n {np.matrix(B)}")

coeff = slg.solve(A,B)

print(f"The curve of best fit is: {coeff[0]} + {coeff[1]}x + {coeff[2]}x^2")

x_val_graph = np.linspace(min(X)-1, max(X+1), 1000)
y_val_graph = [eval(f"{coeff[0][0]} + {coeff[1][0]}*x + {coeff[2][0]}*x**2") for x in x_val_graph]

plt.plot(x_val_graph, y_val_graph, color="blue")
plt.scatter(X, Y, color="red", label="data points")
plt.show()