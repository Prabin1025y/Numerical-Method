# To evaluate integration by simpsons 1/3 rule.
import numpy as np
import matplotlib.pyplot as plt

a = float(input("Enter the lower limit of integral: "))
b = float(input("Enter the lower limit of integral: "))
n = int(input("Enter the number of partitions: "))
assert n % 2 == 0, "n should be even"

h = (b - a) / n
func = input("Input the integrant function in x using python syntax: ")


def f(x, func):
    return eval(func)


def y(x):
    return f(x, func)


x = np.linspace(a, b, n + 1)
sum_odd = 0
sum_even = 0

for i in range(1, n):
    if i % 2 == 0:
        sum_even += y(x[i])
    else:
        sum_odd += y(x[i])

integral = (h / 3) * (y(x[0]) + 4 * sum_odd + 2 * sum_even + y(x[n]))
print(f"Approximate integral by Simpson's 1/3 method is {integral}")

x_val = np.linspace(a - 10, b + 10, 1000)
y_val = [y(value) for value in x_val]
y_points = [y(value) for value in x]
plt.plot(x_val, y_val, color="red")
plt.scatter(x, y_points, color="blue")

for i in range(0, n, 2):
    x_vertices = x[i : i + 3]
    y_vertices = y_points[i : i + 3]
    plt.fill_between(x_vertices, y_vertices, color="pink", edgecolor="black", alpha=0.8)

plt.axhline(0, 0)
plt.axvline(0, 0)
plt.show()
