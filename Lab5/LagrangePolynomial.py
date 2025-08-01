import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

X = np.array(list(map(float, input("Enter all x-data:").split())))
Y = np.array(list(map(float, input("Enter all y-data:").split())))
n=len(X)

x = sp.symbols('x')
lg_polynomial = 0

for i in range(n):
  lbp = 1
  for j in range(n):
    if i != j:
      lbp *= (x - X[j]) / (X[i] -X[j])
  lg_polynomial += Y[i] * lbp

lg_polynomial = sp.simplify(lg_polynomial)
print("Required lagrange interpolation polynomial is \n", lg_polynomial)

poly = sp.lambdify(x, lg_polynomial, 'numpy')
x_val_graph = np.linspace(min(X) - 1, max(X) + 1, 1000)
y_val_graph = poly(x_val_graph)


xp = float(input('Enter the value to interpolate: '))
int_value = lg_polynomial.subs(x, xp)
print(f"The interpolated value of {xp} is {int_value}")

plt.plot(x_val_graph, y_val_graph, color='blue')
plt.scatter(X, Y, color='red', label="Data Points")
plt.axvline(x=xp, color='green', linestyle='--', label=f"Inerpolated x = {xp}")
plt.scatter(xp, float(int_value), color='black', label=f"Interpolated y = {float(int_value):.2f}")

plt.title("Lagrange Interpolation")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()