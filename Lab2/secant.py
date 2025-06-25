import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

eqn = input("Enter the eqn in x using python syntax: ")

def f(x):
    return eval(eqn)

a = float(input("Enter the first approximation: "))
b = float(input("Enter the second approximation: "))

if f(a) == f(b):
    print("Division by zero; Chamge the initial parameters: ")
else:
    e_tol = float(input("Enter the tolerable error: "))
    max_iter = int(input("Enter the maximum number of iterations: "))
    iter = 1

    history = []
    approx = []

    while iter <= max_iter:
        c = ((a * f(b)) - (b * f(a))) / (f(b) - f(a))

        approx.append(c)

        error = abs(f(c))
        history.append([iter, a, b, c, f(a), f(b), f(c)])

        if error < e_tol:
            df = pd.DataFrame(history, columns=["iterations",'a','b','c','f(a)','f(b)','f(c)'])
            print(df.to_string(index=False))
            print(f"Approx root is {c} in {iter} iterations.")
            break

        a,b = b,c
        if f(a) == f(b):
            print("Division by zero; Change the initial parameters: ")

        iter += 1
    
    if iter > max_iter:
        print(f"Solution didn't converge in iterations {max_iter}. Best is {c}")
    
x = np.linspace(-5, 5, 1000)
plt.plot(x, f(x), color='red', label=eqn)

plt.axhline(0,0,color='black')
plt.axvline(0,0,color='black')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title("Falsi method")
plt.legend()
# plt.scatter(approx, f(approx))
for i, value in enumerate(approx):
    plt.text(value, f(value), f'{i}')
plt.show()