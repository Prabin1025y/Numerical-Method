import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

eqn = input("Enter the eqn in x using python syntax: ")

def f(x):
    return eval(eqn)

def g(x, h=1e-10):
    return (f(x+h)-f(x-h))/(2*h)

a = float(input("Enter the first approximation: "))
approx = []

if g(a) == 0:
    print("Division by zero; Change the initial parameters: ")
else:
    e_tol = float(input("Enter the tolerable error: "))
    max_iter = int(input("Enter the maximum number of iterations: "))
    iter = 1

    history = []


    while iter <= max_iter:
        b = a - f(a)/g(a)

        approx.append(b)

        error = abs(f(b))
        history.append([iter, a, f(a), g(a), b])

        if error < e_tol:
            df = pd.DataFrame(history, columns=["iterations",'a','f(a)','f(a)', 'b'])
            print(df.to_string(index=False))
            print(f"Approx root is {b} in {iter} iterations.")
            break

        a = b
        if g(a) == 0:
            print("Division by zero; Change the initial parameters: ")
            break

        iter += 1
    
    if iter > max_iter:
        print(f"Solution didn't converge in iterations {max_iter}. Best is {b}")
    
x = np.linspace(-5, 5, 1000)
plt.plot(x, f(x), color='red', label=eqn)

approx = np.array(approx)
plt.axhline(0,0,color='black')
plt.axvline(0,0,color='black')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title("Newton Raphson method")
plt.legend()
plt.scatter(approx, f(approx))
for i, value in enumerate(approx):
    plt.text(value, f(value), f'{i}')
plt.show()