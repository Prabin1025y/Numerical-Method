# To evaluate integration by trapezoidal rule
import numpy as np
import matplotlib.pyplot as plt

a = float(input("Enter the lower limit of integral: "))
b = float(input("Enter the lower limit of integral: "))
n = int(input("Enter the number of partitions: "))
h = (b - a) / n

func = input("Input the integrant function in x using python syntax: ")
def f(x, func):
    return eval(func)
def y(x):
    return f(x, func)

x = np.linspace(a, b, n + 1)
integral = 0
sum = 0

for i in range(1, n):
    sum += y(x[i])

integral = (h / 2) * (y(x[0]) + 2 * sum + y(x[n]))
print(f"Approximate integral by trapezoidal method is {integral}")

x_val = np.linspace(a-10, b+10, 1000)
y_val = [y(value) for value in x_val]
y_points = [y(value) for value in x]
plt.plot(x_val, y_val, color='red')
plt.scatter(x, y_points, color='blue')

for i in range(n):
    x_vertices = [x[i], x[i], x[i+1], x[i+1]]
    y_vertices = [0, y_points[i], y_points[i+1], 0]
    plt.fill(x_vertices, y_vertices, color='pink', edgecolor='black', alpha=0.8)

plt.axhline(0,0)
plt.axvline(0,0)
plt.show()

